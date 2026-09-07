import re
import tempfile
import unittest
from pathlib import Path
from measure import measure
ROOT = Path(__file__).resolve().parents[1]
NEEDLES = ['## Safety', '## Output Contract', 'old/new', 'No new provider spend', 'not tokens', 'profile', 'needs_more_tests']


def validate(text):
    return all(n in text for n in NEEDLES) and all((ROOT / p).is_file() for p in re.findall(r'\]\((references/[^)]+|scripts/[^)]+)\)', text))


class Checks(unittest.TestCase):
    def test_contract(self):
        text = (ROOT / 'SKILL.md').read_text()
        self.assertTrue(validate(text))
        self.assertLess(len(text.encode()), 8000)

    def test_safety_mutation(self):
        self.assertFalse(validate((ROOT / 'SKILL.md').read_text().replace('No new provider spend', '')))

    def test_link_mutation(self):
        self.assertFalse(validate((ROOT / 'SKILL.md').read_text() + '\n[x](references/missing.md)'))

    def test_measure(self):
        result = measure(ROOT)
        self.assertIsNone(result['tokens'])
        self.assertEqual(result['instruction_bytes'], sum(r['bytes'] for r in result['files']))

    def test_missing_root(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                measure(d)

    def test_escape(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as o:
            p = Path(d)
            (p / 'SKILL.md').write_text('safe')
            (p / 'references').mkdir()
            target = Path(o) / 'secret.md'
            target.write_text('no')
            (p / 'references/escape.md').symlink_to(target)
            with self.assertRaises(ValueError):
                measure(p)

if __name__ == '__main__':
    unittest.main()
