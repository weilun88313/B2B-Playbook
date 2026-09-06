#!/usr/bin/env python3
"""Validate reader links, coverage, mirrors and assets; standard library only."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from html import unescape
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit, parse_qs
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
MD_LINK = re.compile(r'!?\[([^\]]*)\]\(([^)\s]+)\)')
HTML_LINK = re.compile(r'\b(?:href|src)=["\']([^"\']+)["\']')
CONFIG = json.loads((ROOT / "docs.json").read_text())
REDIRECTS = {x["source"]: x["destination"] for x in CONFIG.get("redirects", [])}
DOCS = {p.relative_to(ROOT).as_posix(): p.read_text() for p in ROOT.rglob("*")
        if p.suffix in {".md", ".mdx"} and ".git" not in p.parts
        and "node_modules" not in p.parts and ".github" not in p.parts
        and p.name != "AGENTS.md"}

def check(ok, message):
    if not ok:
        ERRORS.append(message)

def body(text):
    return re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)

def links(text):
    text = re.sub(chr(96)*3 + '.*?' + chr(96)*3, '', text, flags=re.S)
    return [unescape(m[1]) for m in MD_LINK.findall(text)] + [unescape(x) for x in HTML_LINK.findall(text)]

def resolve(source, url):
    raw = unquote(urlsplit(url).path)
    if not raw:
        return ROOT / source
    if raw.startswith("/"):
        seen = set()
        while raw in REDIRECTS:
            if raw in seen:
                return None
            seen.add(raw)
            raw = REDIRECTS[raw]
        base = ROOT / raw.lstrip("/")
    else:
        base = (ROOT / source).parent / raw
    for p in [base, Path(str(base)+".md"), Path(str(base)+".mdx"),
              base / "README.md", base / "index.md", base / "index.mdx"]:
        if p.is_file() and p.resolve().is_relative_to(ROOT.resolve()) and p.name in {x.name for x in p.parent.iterdir()}:
            return p
    return None

def anchors(text):
    found = set(re.findall(r'\bid=["\']([^"\']+)', text))
    counts = Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+)$', body(text), re.M):
        heading = MD_LINK.sub(lambda m: m[1], heading)
        slug = re.sub(r'[^\w\s-]', '', heading.lower()).replace(" ", "-")
        count = counts[slug]
        counts[slug] += 1
        found.add(slug + (f"-{count}" if count else ""))
    return found

external = set()
for name, text in DOCS.items():
    if name not in {"README.md", "README.zh.md"}:
        check(not re.search(r'[\u3400-\u9fff]', text), f"{name}: unexpected Chinese")
    for url in links(text):
        u = urlsplit(url)
        if u.scheme in {"http", "https"}:
            owned = (u.hostname == "github.com" and
                     (u.path == "/weilun88313/B2B-Playbook" or u.path.startswith("/weilun88313/B2B-Playbook/")))
            owned |= u.hostname in {"b2-b-playbook.mintlify.app", "b2-b-playbook.mintlify.site"}
            if not owned:
                check(parse_qs(u.query).get("ref") == ["b2b-playbook"], f"{name}: missing/duplicate ref: {url}")
                external.add(url)
        elif not u.scheme:
            target = resolve(name, url)
            check(target is not None, f"{name}: missing local target {url}")
            if target and u.fragment and target.suffix in {".md", ".mdx"}:
                check(unquote(u.fragment) in anchors(target.read_text()), f"{name}: missing anchor {url}")

domains = sorted((ROOT / "playbooks").glob("[0-9][0-9]-*"))
tactics = [p for d in domains for p in d.glob("*.md") if p.name not in {"README.md", "index.md"}]
working = [p for p in (ROOT / "templates").iterdir() if p.is_file() and p.name not in {"README.md", "overview.md"}]
tools = [line for line in DOCS["TOOLS.md"].splitlines() if 'class="tool-cell"' in line]
resources = [line for line in DOCS["RESOURCES.md"].splitlines() if re.match(r'^\| \[.+?\]\(https?://', line)]
expected = [len(tactics), len(working), len(tools), len(resources), len(domains)]
for name in ["README.md", "README.zh.md", "index.mdx"]:
    line = next((x for x in DOCS[name].splitlines() if "**Current coverage:**" in x or "**当前覆盖：" in x), "")
    check([int(x) for x in re.findall(r'\d+', line)] == expected, f"{name}: coverage must be {expected}")
    for n in re.findall(r'(\d+)-source directory', DOCS[name]):
        check(int(n) == len(resources), f"{name}: stale reading-source count")
check(len(re.findall(r'^## \d\d ·', DOCS["TOOLS.md"], re.M)) ==
      int(re.search(r'(\d+) operating categories', DOCS["TOOLS.md"])[1]), "TOOLS: category count")
names = [re.search(r'<a href="[^"]+">([^<]+)</a>', line)[1] for line in tools]
check(len(names) == len(set(names)), "TOOLS: duplicate product")
icons = [re.search(r'src="([^"]+)"', line)[1] for line in tools]
check(len(set(icons)) == len(tools), "TOOLS: duplicate favicon")
check(set(icons) == {p.relative_to(ROOT).as_posix() for p in (ROOT/"assets/tool-favicons").iterdir()}, "TOOLS: orphan/missing favicon")
check("vendelux" not in DOCS["TOOLS.md"].lower(), "TOOLS: excluded competitor")
check("Owner product" in next(x for x in tools if ">Lensmor<" in x), "TOOLS: owner disclosure")

def normal(text):
    text = re.sub(r'^# .+\n', '', body(text), count=1)
    return re.sub(r'\s+', ' ', MD_LINK.sub(lambda m: m[1], text)).strip()

for d in domains:
    a, b = (d/"README.md").read_text(), (d/"index.md").read_text()
    check(normal(a) == normal(b), f"{d.name}: README/index mirror drift")
    count = len([p for p in tactics if p.parent == d])
    for text in [a, b]:
        check(f"{count} tactic playbooks published" in text, f"{d.name}: stale tactic count")
for p in tactics:
    text = p.read_text()
    check(bool(re.search(r'\*\*Last reviewed:\*\* \d{4}-\d{2}-\d{2}', text)), f"{p.name}: missing review date")
    check("## Sources" in text and "## What to read next" in text, f"{p.name}: missing evidence/next reading")
    check("Copyright © 2026 Ivan Xu" in text, f"{p.name}: missing copyright")

def nav_pages(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "pages":
                yield from (x for x in child if isinstance(x, str))
            else:
                yield from nav_pages(child)
    elif isinstance(value, list):
        for child in value:
            yield from nav_pages(child)

pages = list(nav_pages(CONFIG["navigation"]))
check(len(pages) == len(set(pages)), "docs.json: duplicate navigation page")
for page in pages:
    check(any((ROOT/(page+ext)).is_file() for ext in [".md", ".mdx"]), f"docs.json: missing {page}")
for p in tactics:
    check(p.relative_to(ROOT).with_suffix("").as_posix() in pages, f"{p.name}: not in site navigation")
for source in REDIRECTS:
    check(resolve("index.mdx", source) is not None, f"docs.json: broken redirect {source}")

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--external", action="store_true", help="Check third-party URLs; bot blocks/timeouts are warnings.")
args = parser.parse_args()
if args.external:
    def visit(url):
        try:
            with urlopen(Request(url, headers={"User-Agent": "B2B-Playbook-link-check"}), timeout=15) as response:
                return url, response.status
        except HTTPError as error:
            return url, error.code
        except Exception:
            return url, "unverified"
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, status in pool.map(visit, sorted(external)):
            if status in {404, 410}:
                ERRORS.append(f"external {status}: {url}")
            elif not isinstance(status, int) or status >= 400:
                print(f"WARNING external {status}: {url}")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR {error}")
    sys.exit(1)
print(f"PASS: {len(DOCS)} pages; {len(tactics)} playbooks; {len(working)} working files; {len(tools)} tools; {len(resources)} sources; {len(pages)} navigation entries.")
print(f"PASS: local links/anchors, domain mirrors, coverage, favicons, {len(external)} unique third-party ref URLs.")
