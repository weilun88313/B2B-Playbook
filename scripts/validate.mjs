#!/usr/bin/env node

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const ignored = new Set([".git", "node_modules"]);

function walk(directory) {
  return readdirSync(directory).flatMap((entry) => {
    if (ignored.has(entry)) return [];
    const path = join(directory, entry);
    return statSync(path).isDirectory() ? walk(path) : [path];
  });
}

function relativeMarkdownLinks(file) {
  const text = readFileSync(file, "utf8");
  return [...text.matchAll(/!?\[[^\]]*\]\(([^)]+)\)/g)]
    .map((match) => match[1].trim().split(/\s+["']/)[0].split("#")[0])
    .filter((target) => target && !/^(https?:|mailto:|#)/.test(target));
}

const markdownFiles = walk(root).filter((file) => file.endsWith(".md"));
const errors = [];

for (const file of markdownFiles) {
  const text = readFileSync(file, "utf8");
  if (file !== join(root, "README.md") && /\p{Script=Han}/u.test(text)) {
    errors.push(`${file}: Chinese text is allowed only in the root README.md`);
  }

  for (const target of relativeMarkdownLinks(file)) {
    let decoded = target;
    try {
      decoded = decodeURI(target);
    } catch {
      errors.push(`${file}: invalid URI in link ${target}`);
      continue;
    }
    if (!existsSync(resolve(dirname(file), decoded))) {
      errors.push(`${file}: broken relative link ${target}`);
    }
  }
}

for (const modulePath of [
  "playbooks/01-icp",
  "playbooks/02-positioning",
  "playbooks/03-outbound",
  "playbooks/04-events",
  "playbooks/06-sales",
]) {
  for (const required of ["README.md", "sop.md", "metrics.md"]) {
    if (!existsSync(join(root, modulePath, required))) {
      errors.push(`${modulePath}: missing ${required}`);
    }
  }
  for (const directory of ["checklists", "templates", "examples"]) {
    const path = join(root, modulePath, directory);
    if (!existsSync(path) || !readdirSync(path).some((file) => file.endsWith(".md"))) {
      errors.push(`${modulePath}: ${directory}/ needs at least one Markdown file`);
    }
  }
}

const skill = readFileSync(join(root, "SKILL.md"), "utf8");
if (!/^---\n[\s\S]*?^name:\s*[a-z0-9-]+\s*$[\s\S]*?^description:\s*\S/m.test(skill)) {
  errors.push("SKILL.md: missing valid name or description frontmatter");
}

if (errors.length) {
  console.error(`Validation failed with ${errors.length} error(s):\n- ${errors.join("\n- ")}`);
  process.exit(1);
}

console.log(`Validated ${markdownFiles.length} Markdown files, relative links, module contracts, the English-only content policy, and SKILL.md frontmatter.`);
