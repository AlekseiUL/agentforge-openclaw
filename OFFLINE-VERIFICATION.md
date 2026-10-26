# Offline verification boundary

Additive dry-run installer and preservation/symlink/fixture-rollback checks for the documented two-file skill copy.

## Reproduce

`python3 scripts/install.py --workspace <workspace>; python3 -m unittest discover -s tests -v`

--apply is explicit; existing files are preserved. Updates need a reviewed diff and snapshot. No automatic gateway restart or destructive uninstall; rollback tests remove only a disposable fixture tree.

## Rollback

Review the commit diff and use a new checkout of the pre-change commit for source rollback. Keep user data and live installations untouched. A source rollback is not permission to restore unsafe network exposure or bypass approval.
