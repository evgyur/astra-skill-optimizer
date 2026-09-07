"""Read-only instruction measurement; no token estimates."""
import argparse
import hashlib
import json
from pathlib import Path


def measure(root):
    root = Path(root).resolve()
    entry = root / 'SKILL.md'
    if not entry.is_file():
        raise ValueError('SKILL.md required')
    refs = root / 'references'
    if refs.is_symlink():
        raise ValueError('symlink references unsupported')
    paths = [entry] + (sorted(refs.rglob('*.md')) if refs.is_dir() else [])
    rows = []
    for p in paths:
        if p.is_symlink() or any((root / parent).is_symlink() for parent in p.relative_to(root).parents):
            raise ValueError('symlink input unsupported')
        if not p.resolve().is_relative_to(root):
            raise ValueError('path escapes root')
        if not p.is_file() or p.stat().st_size > 2000000:
            raise ValueError('unsupported file or size above 2MB')
        data = p.read_bytes()
        rows.append({'path': str(p.relative_to(root)), 'bytes': len(data), 'characters': len(data.decode('utf-8')), 'sha256': hashlib.sha256(data).hexdigest()})
    return {'files': rows, 'instruction_bytes': sum(r['bytes'] for r in rows), 'tokens': None, 'scope': 'root and references markdown only; no performance inference'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill_dir')
    print(json.dumps(measure(parser.parse_args().skill_dir), indent=2))
