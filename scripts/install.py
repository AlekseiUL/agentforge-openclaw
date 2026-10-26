"""Copy the two documented skill files; default dry-run, never restart a gateway."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    destination = Path(args.workspace).expanduser() / 'skills/agent-forge'
    files = ['SKILL.md', 'references/agent-templates.md']
    created, preserved = [], []
    for name in files:
        target = destination / name
        if target.is_symlink() or any(p.is_symlink() for p in target.parents):
            parser.error('symlink destination refused')
        if target.exists():
            preserved.append(name)
            continue
        if args.apply:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as output:
                output.write((root / name).read_bytes())
        created.append(name)
    print(json.dumps({'applied': args.apply, 'created' if args.apply else 'would_create': created,
                      'preserved': preserved, 'gateway_restart': 'not_run'}))


if __name__ == '__main__':
    main()
