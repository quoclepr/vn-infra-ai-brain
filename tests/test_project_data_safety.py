"""Regression tests use only dummy data and the Python standard library."""

import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
SENSITIVE_FILES = (
    ".env", ".env.local", "nested/.env.production", "server.pem",
    "server.key", "bundle.p12", "bundle.pfx", "id_rsa", "id_dsa", "id_ecdsa", "id_ed25519",
    ".git-credentials", ".netrc", "_netrc", ".npmrc", ".pypirc",
    "nested/api_token.txt", "nested/client_secret.json", "credentials.json",
    ".ssh/config", ".aws/config", ".azure/config", ".config/gcloud/config",
)


def run_script(name, *args):
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *map(str, args)],
        capture_output=True, text=True, encoding="utf-8",
        env={**os.environ, "PYTHONUTF8": "1"},
    )


def create_directory_link(target, link):
    if os.name == "nt":
        import _winapi
        _winapi.CreateJunction(str(target), str(link))
    else:
        link.symlink_to(target, target_is_directory=True)


class ProjectDataSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="vn_infra_safety_")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.root.mkdir()

    def write(self, relative, content="DUMMY TEST DATA"):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def initialize(self):
        result = run_script(
            "init_project_brain.py", "--target", self.root,
            "--code", "TEST-01", "--name", "Dummy project",
            "--type", "tham-tra", "--git",
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_ignored(self):
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "--stdin", "-z"], cwd=self.root,
            input=("\0".join((*SENSITIVE_FILES, "notes.md", "plan.dwg")) + "\0").encode(),
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(result.stdout.decode().rstrip("\0").split("\0")), set(SENSITIVE_FILES))

    def archive_names(self):
        result = run_script("snapshot_project.py", "--project", self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        archive, = (self.root / "_Backups").glob("*.zip")
        with zipfile.ZipFile(archive) as zf:
            return set(zf.namelist())

    def test_new_project_runs_and_ignores_sensitive_files(self):
        self.initialize()
        brain = (self.root / "GEMINI.md").read_text(encoding="utf-8")
        self.assertIn("Dummy project", brain)
        self.assertIn("TEST-01", brain)
        self.assertTrue((self.root / "00_NhatKy_QuyetDinh.md").exists())
        self.assert_ignored()

    def test_existing_ignore_rules_are_preserved_and_update_is_idempotent(self):
        original = "# custom rules\ncustom-output/\n.env\n!.env\n"
        self.write(".gitignore", original)
        self.initialize()
        first = (self.root / ".gitignore").read_text(encoding="utf-8")
        self.assertTrue(first.startswith(original))
        self.assert_ignored()
        self.initialize()
        self.assertEqual((self.root / ".gitignore").read_text(encoding="utf-8"), first)

    def test_initialize_refuses_to_write_through_a_linked_gitignore(self):
        outside = Path(self.temp.name) / "private.txt"
        outside.write_text("DUMMY PRIVATE DATA", encoding="utf-8")
        (self.root / ".gitignore").symlink_to(outside)
        result = run_script(
            "init_project_brain.py", "--target", self.root, "--code", "TEST-01",
            "--name", "Dummy project", "--type", "tham-tra", "--git",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(outside.read_text(encoding="utf-8"), "DUMMY PRIVATE DATA")

    def test_snapshot_excludes_sensitive_files_and_keeps_project_documents(self):
        for name in (*SENSITIVE_FILES, ".ENV.PROD", "nested/PRIVATE.PEM"):
            self.write(name)
        safe = {"notes.md", "nested/boq.xlsx", "nested/plan.dwg"}
        for name in safe:
            self.write(name, "Public dummy document")
        self.assertEqual(self.archive_names(), safe)

    def test_snapshot_prunes_sensitive_directories_and_old_backups(self):
        for directory in (
            "secrets", "my_tokens", "Credentials", ".ssh", ".aws", ".azure",
            ".config/gcloud", ".git", "backups", "_Backups", "node_modules", ".venv",
        ):
            self.write(f"{directory}/nested/config.txt")
        self.write("notes.md", "Public dummy document")
        self.assertEqual(self.archive_names(), {"notes.md"})

    def test_snapshot_does_not_follow_directory_links(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (outside / "private.txt").write_text("DUMMY PRIVATE DATA", encoding="utf-8")
        link = self.root / "linked_directory"
        create_directory_link(outside, link)
        self.write("notes.md", "Public dummy document")
        self.assertEqual(self.archive_names(), {"notes.md"})

    def test_snapshot_does_not_copy_a_file_link_with_an_innocent_name(self):
        outside = Path(self.temp.name) / "private.txt"
        outside.write_text("DUMMY PRIVATE DATA", encoding="utf-8")
        (self.root / "ordinary.txt").symlink_to(outside)
        self.write("notes.md", "Public dummy document")
        self.assertEqual(self.archive_names(), {"notes.md"})

    def test_snapshot_refuses_a_linked_backup_destination(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        create_directory_link(outside, self.root / "_Backups")
        self.write("notes.md", "Public dummy document")
        result = run_script("snapshot_project.py", "--project", self.root)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(list(outside.iterdir()))


if __name__ == "__main__":
    unittest.main()
