"""Markdown reading safeguards, without changing code samples or link targets."""
import re

CURRENCY = re.compile(r'(?<![\\$])\$(?!\$)(?=\d|[XY]\b)')
INLINE_CODE = re.compile(r'(`+)(.*?)(?<!`)\1(?!`)', re.S)

def prose_lines(text):
    """Yield prose line numbers/text; fenced code remains untouched."""
    fence = None
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            run = marker[1]
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield number, line

def transform_prose(line, transform):
    # Protect inline code, Markdown destinations, and HTML attributes.
    protected = re.compile(r'(`+).*?(?<!`)\1(?!`)|\]\([^\n]*?\)|\b(?:href|src)=["\'][^"\']*["\']')
    parts=[]; start=0
    for match in protected.finditer(line):
        parts.extend([transform(line[start:match.start()]), match[0]])
        start=match.end()
    parts.append(transform(line[start:]))
    return ''.join(parts)

def unsafe_currency_lines(text):
    return [n for n,line in prose_lines(text)
            if transform_prose(line, lambda s: CURRENCY.sub('&#36;',s)) != line]

def escape_currency(text):
    lines=text.splitlines(keepends=True)
    for n,line in prose_lines(text):
        lines[n-1]=transform_prose(line,lambda s:CURRENCY.sub('&#36;',s))
    return ''.join(lines)
