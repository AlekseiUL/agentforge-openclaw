import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class Install(unittest.TestCase):
    def test_dry_run_install_repeat_and_fixture_rollback(self):
        with tempfile.TemporaryDirectory() as td:
            home = pathlib.Path(td).resolve()
            target = home / 'workspace'
            command = [sys.executable, str(ROOT/'scripts/install.py'), '--workspace', str(target)]
            def run(*args):
                return json.loads(subprocess.check_output(command + list(args), text=True))
            self.assertFalse(run()['applied'])
            self.assertFalse(target.exists())
            self.assertEqual(len(run('--apply')['created']), 2)
            skill = target/'skills/agent-forge/SKILL.md'
            self.assertEqual(skill.read_bytes(), (ROOT/'SKILL.md').read_bytes())
            skill.write_text('user customization')
            snapshot = home/'snapshot'
            shutil.copytree(target, snapshot)
            receipt = run('--apply')
            self.assertEqual(receipt['created'], [])
            self.assertEqual(skill.read_text(), 'user customization')
            self.assertEqual(receipt['gateway_restart'], 'not_run')
            shutil.rmtree(target)
            shutil.copytree(snapshot, target)
            self.assertEqual(skill.read_text(), 'user customization')

    def test_symlink_destination_refused(self):
        with tempfile.TemporaryDirectory() as td:
            home = pathlib.Path(td)
            outside = home/'outside'; outside.mkdir()
            workspace = home/'workspace'; workspace.symlink_to(outside, target_is_directory=True)
            p = subprocess.run([sys.executable, str(ROOT/'scripts/install.py'), '--workspace', str(workspace), '--apply'], capture_output=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertEqual(list(outside.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
