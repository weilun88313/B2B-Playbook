"""Regression checks for links that differ between GitHub and the reading site."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('entrypoints', Path(__file__).with_name('sync-entrypoints.py'))
entrypoints = importlib.util.module_from_spec(spec)
spec.loader.exec_module(entrypoints)


class SiteLinks(unittest.TestCase):
    def test_platform_routes(self):
        source = 'playbooks/06-account-field-and-partner/README.md'
        examples = {
            'trade-shows.md#prepare': '/playbooks/06-account-field-and-partner/trade-shows#prepare',
            '../README.md': '/playbooks',
            '../../LICENSE': '/copyright',
            '../../assets/illustrations/trade-shows.webp': '/assets/illustrations/trade-shows.webp',
            '../../templates/README.md': '/templates/overview',
            '../../templates/demo-scorecard.xlsx': '/templates/demo-scorecard.xlsx',
            '../../SKILL.md': '/skill',
            '#start-here': '#start-here',
            'https://example.com/a?ref=b2b-playbook#b': 'https://example.com/a?ref=b2b-playbook#b',
        }
        for before, after in examples.items():
            with self.subTest(before=before):
                self.assertEqual(entrypoints.site_url(source, before), after)

    def test_mirror_preserves_copy_and_frontmatter(self):
        original = '# Chapter\n\n**Last reviewed:** 2026-08-30\n\n[Next](trade-shows.md)\n'
        previous = '---\ntitle: "Chapter"\n---\n\nOld copy\n'
        self.assertEqual(entrypoints.render_mirror('playbooks/events/README.md', original, previous),
                         '---\ntitle: "Chapter"\n---\n\n**Last reviewed:** 2026-08-30\n\n[Next](/playbooks/events/trade-shows)\n')


if __name__ == '__main__':
    unittest.main()
