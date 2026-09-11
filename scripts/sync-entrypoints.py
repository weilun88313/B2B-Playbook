#!/usr/bin/env python3
"""Generate reading mirrors, coverage summaries, and chapter navigation from source files."""
import argparse
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'(!?\[[^\]]*\]\()([^\s)]+)(\))')


def site_url(source, url):
    parsed = urlsplit(url)
    if parsed.scheme or url.startswith(('/', '#')):
        return url
    target = posixpath.normpath(posixpath.join(posixpath.dirname(source), parsed.path))
    aliases = {'LICENSE': 'copyright', 'README.md': 'index', 'README.zh.md': None,
               'SKILL.md': 'skill', 'templates/README.md': 'templates/overview'}
    if target in aliases:
        if aliases[target] is None:
            return 'https://github.com/weilun88313/B2B-Playbook/blob/main/' + target
        target = aliases[target]
    elif target.endswith('/README.md'):
        target = target[:-len('/README.md')]
    elif target.endswith(('.md', '.mdx')):
        target = target.rsplit('.', 1)[0]
    return '/' + target + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')


def render_mirror(source, text, previous):
    frontmatter = re.match(r'\A---\n.*?\n---\n', previous, re.S)
    if not frontmatter:
        raise ValueError(f'Mirror for {source} needs frontmatter')
    content = re.sub(r'\A# [^\n]+\n\n', '', text)
    content = LINK.sub(lambda m: m[1] + site_url(source, m[2]) + m[3], content)
    return frontmatter[0] + '\n' + content


def synchronize(root=ROOT, check=False):
    updates = {}
    def read(name):
        return updates.get(name, (root / name).read_text())
    domains = sorted((root / 'playbooks').glob('[0-9][0-9]-*'))
    tactics = [p for d in domains for p in d.glob('*.md') if p.name not in {'README.md', 'index.md'}]
    working = [p for p in (root / 'templates').iterdir() if p.is_file() and p.name not in {'README.md', 'overview.md'}]
    tools = sum('class="tool-cell"' in line for line in read('TOOLS.md').splitlines())
    resources = len(re.findall(r'^\| \[.+?\]\(https?://', read('RESOURCES.md'), re.M))
    coverage = f'{len(tactics)} published playbooks · {len(working)} working files · {tools} curated tools · {resources} reading sources · {len(domains)} domain guides'
    for name in ['README.md', 'index.mdx']:
        updates[name] = re.sub(r'(?m)^\*\*Current coverage:\*\* .*$', '**Current coverage:** ' + coverage, read(name))
    updates['README.zh.md'] = re.sub(r'(?m)^\*\*当前覆盖：\*\* .*$', f'**当前覆盖：** {len(tactics)} 篇已发布 Playbook · {len(working)} 份工作文件 · {tools} 个精选工具 · {resources} 个阅读源 · {len(domains)} 个领域指南', read('README.zh.md'))
    pairs = [('playbooks/README.md', 'playbooks/index.md'), ('templates/README.md', 'templates/overview.md')]
    chapter_pages = {}
    for d in domains:
        name = d.relative_to(root).as_posix()
        source = name + '/README.md'
        count = sum(p.parent == d for p in tactics)
        updates[source] = re.sub(r'\d+ tactic playbooks published', f'{count} tactic playbooks published', read(source))
        pairs.append((source, name + '/index.md'))
        # The published map sets the site's chapter order; planned topics stay out.
        section = re.search(r'## Playbook map\n(.*?)(?=\n## |\Z)', read(source), re.S)
        if not section:
            raise ValueError(f'{source}: missing published map')
        targets = []
        for m in LINK.finditer(section[1]):
            target = site_url(source, m[2]).lstrip('/')
            if target.startswith(name + '/') and target not in targets:
                targets.append(target)
        expected = {p.relative_to(root).with_suffix('').as_posix() for p in tactics if p.parent == d}
        if set(targets) != expected:
            raise ValueError(f'{source}: published map does not match article files')
        chapter_pages[name] = [name + '/index'] + targets
    for source, destination in pairs:
        updates[destination] = render_mirror(source, read(source), read(destination))
    config = json.loads(read('docs.json'))
    def visit(value):
        if isinstance(value, dict):
            pages = value.get('pages', [])
            if pages and isinstance(pages[0], str) and pages[0].endswith('/index'):
                chapter = pages[0][:-len('/index')]
                if chapter in chapter_pages:
                    value['pages'] = chapter_pages[chapter]
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(config['navigation'])
    updates['docs.json'] = json.dumps(config, ensure_ascii=False, indent=2) + '\n'
    changed = [name for name, text in updates.items() if text != (root / name).read_text()]
    if not check:
        for name in changed:
            (root / name).write_text(updates[name])
    for name in changed:
        print(('STALE: ' if check else 'UPDATED: ') + name)
    return changed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail on drift without writing files')
    args = parser.parse_args()
    changed = synchronize(check=args.check)
    if args.check and changed:
        raise SystemExit(1)
    print('PASS: entrypoints are synchronized')
