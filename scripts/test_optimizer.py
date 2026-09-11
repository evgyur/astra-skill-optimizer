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

    def test_astra_root_contract(self):
        text = (ROOT / 'SKILL.md').read_text()
        required = ['references/astra-guidance.md', 'AGENTS.md', 'neighboring-task',
                    'runtime index', 'completion evidence', 'protected-effect approvals',
                    'non-Astra consumers', 'do not switch to postwriting']
        self.assertTrue(all(x in text for x in required))
        for needle in required:
            with self.subTest(removed=needle):
                mutant = text.replace(needle, '')
                self.assertFalse(all(x in mutant for x in required))

    def test_vendor_guidance_contract(self):
        text = (ROOT / 'references/astra-guidance.md').read_text()
        required = ['developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra',
                    '## 1. Trigger specificity', '## 2. Instruction surfaces',
                    '## 3. Contextual loading', '## 4. Proportional verification',
                    '## 5. Decision boundaries', '## 6. Persistence and stop conditions',
                    '## 7. Mixed-model compatibility',
                    'not rewriting that file', 'verify fixtures, endpoints and permissions',
                    'explicitly requested review checkpoints', 'not measured results']
        self.assertTrue(all(x in text for x in required))
        for needle in required:
            with self.subTest(removed=needle):
                self.assertFalse(all(x in text.replace(needle, '') for x in required))

    def test_evaluation_scenarios(self):
        text = (ROOT / 'references/evaluation.md').read_text()
        for case in ['Trigger specificity:', 'Instruction conflict:', 'Persistence:',
                     'Protected stop:', 'Proportionality:', 'Mixed-model use:']:
            with self.subTest(case=case):
                self.assertIn(case, text)
        self.assertIn('not model compliance', text)

    def test_description_budget(self):
        text = (ROOT / 'SKILL.md').read_text()
        match = re.search(r'^description: "([^"]+)"$', text, re.M)
        assert match is not None, 'Missing quoted description'
        description = match.group(1)
        self.assertLessEqual(len(description), 60)
        self.assertTrue(description.startswith('Use when optimizing skills'))

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
