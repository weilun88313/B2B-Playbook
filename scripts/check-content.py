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
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit, parse_qs
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from reading_safety import unsafe_currency_lines

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
    for line in unsafe_currency_lines(text):
        check(False, f"{name}:{line}: unescaped currency may become math; use &#36; outside code")
    if name not in {"README.md", "README.zh.md"}:
        check(not re.search(r'[\u3400-\u9fff]', text), f"{name}: unexpected Chinese")
    for url in links(text):
        u = urlsplit(url)
        if u.scheme in {"http", "https"}:
            owned = (u.hostname == "github.com" and
                     (u.path == "/weilun88313/B2B-Playbook" or u.path.startswith("/weilun88313/B2B-Playbook/")))
            owned |= u.hostname in {"b2-b-playbook.mintlify.app", "b2-b-playbook.mintlify.site"}
            if u.hostname in {"b2-b-playbook.mintlify.app", "b2-b-playbook.mintlify.site"}:
                target = resolve(name, u.path or "/index")
                check(target is not None, f"{name}: missing reading-site target {url}")
                if target and u.fragment and target.suffix in {".md", ".mdx"}:
                    check(unquote(u.fragment) in anchors(target.read_text()), f"{name}: missing reading-site anchor {url}")
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

illustrations = list((ROOT / "assets/illustrations").glob("*.webp"))
# Only publish final reading assets; generators and source files stay outside Git.
for p in (ROOT / "assets/illustrations").iterdir():
    check(p.suffix == ".webp" or p.name == "ATTRIBUTION.txt", f"{p.name}: unexpected illustration source/build file")
referenced_images = set()
for name, text in DOCS.items():
    for url in links(text):
        if "assets/illustrations/" in url and not urlsplit(url).scheme:
            target = resolve(name, url)
            if target:
                referenced_images.add(target.resolve())
    for alt, url in MD_LINK.findall(text):
        if "assets/illustrations/" in url:
            check(bool(alt.strip()), f"{name}: illustration needs meaningful alternative text")
for p in illustrations:
    check(p.resolve() in referenced_images, f"{p.name}: unreferenced illustration")
for name, text in DOCS.items():
    for number, line in enumerate(text.splitlines(), 1):
        check(not re.search(r"(?i)(?:for this library, preserve|this knowledge base's article illustrations|do not paste .+ into this repo|the playbook wins until|python(?:3)? scripts/build-working-files\.py)", line),
              f"{name}:{number}: maintainer instruction in reader content")

def webp_dimensions(data):
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("not a WebP image")
    offset = 12
    while offset + 8 <= len(data):
        kind = data[offset:offset + 4]
        size = int.from_bytes(data[offset + 4:offset + 8], "little")
        payload = data[offset + 8:offset + 8 + size]
        if kind == b"VP8 " and payload[3:6] == b"\x9d\x01\x2a":
            return (int.from_bytes(payload[6:8], "little") & 0x3fff,
                    int.from_bytes(payload[8:10], "little") & 0x3fff)
        if kind == b"VP8X":
            return (1 + int.from_bytes(payload[4:7], "little"),
                    1 + int.from_bytes(payload[7:10], "little"))
        if kind == b"VP8L" and payload[0] == 0x2f:
            bits = int.from_bytes(payload[1:5], "little")
            return (1 + (bits & 0x3fff), 1 + ((bits >> 14) & 0x3fff))
        offset += 8 + size + (size % 2)
    raise ValueError("missing image dimensions")

for p in illustrations:
    try:
        check(webp_dimensions(p.read_bytes()) == (1600, 900), f"{p.name}: expected 1600x900 (16:9)")
        check(p.stat().st_size < 250_000, f"{p.name}: reading asset exceeds 250 KB")
    except (ValueError, IndexError) as error:
        check(False, f"{p.name}: invalid WebP: {error}")

# Keep the selected reading theme consistent across the site and owned artwork.
check(CONFIG.get("theme") == "luma", "docs.json: expected the selected Luma theme")
check(CONFIG.get("fonts", {}).get("family") == "Geist", "docs.json: expected Geist typography")
retired_colors = {"#2f6e63", "#9bd0b7", "#24443b", "#f6f3ea", "#fcfaf5"}
brand_assets = list((ROOT / "assets/brand").glob("*.svg"))
for asset in brand_assets + [ROOT / "docs.json", ROOT / "style.css"]:
    palette = set(re.findall(r'#[0-9a-f]{6}\b', asset.read_text().lower()))
    check(not palette & retired_colors, f"{asset.name}: retired green/paper palette")
for p in brand_assets:
    try:
        svg = ET.fromstring(p.read_text())
        ns = "{http://www.w3.org/2000/svg}"
        check(svg.tag == ns + "svg" and "viewBox" in svg.attrib, f"{p.name}: invalid scalable SVG")
        check(all(e.tag not in {ns + "script", ns + "foreignObject"} for e in svg.iter()),
              f"{p.name}: unexpected active SVG content")
    except ET.ParseError as error:
        check(False, f"{p.name}: malformed SVG: {error}")

def nav_pages(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "pages":
                for page in child:
                    if isinstance(page, str):
                        yield page
                    else:
                        yield from nav_pages(page)
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
print(f"PASS: {len(illustrations)} 1600x900 WebP illustrations; all retained images are referenced; illustrations are optional.")
