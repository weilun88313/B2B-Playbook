#!/usr/bin/env node

import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const dimensions = [
  ["useCase", "Use-case fit"],
  ["budget", "Budget / operating fit"],
  ["alternative", "Alternative clarity"],
  ["trigger", "Observable trigger"],
  ["committee", "Buying-committee visibility"],
];

const actions = {
  T1: "Run one-to-one research, resolve committee unknowns, and prepare a personalized next step.",
  T2: "Test a shared trigger hypothesis in a small segment; do not spend one-to-one research time yet.",
  T3: "Keep the account out of active outbound and record the disqualifier or missing evidence.",
};

function requireScore(value, name) {
  const score = Number(value);
  if (!Number.isInteger(score) || score < 0 || score > 2) {
    throw new Error(`${name} must be 0, 1, or 2.`);
  }
  return score;
}

export function scoreAccount(input) {
  const account = {
    name: String(input.name || "Unnamed account"),
    useCase: requireScore(input.useCase, "useCase"),
    budget: requireScore(input.budget, "budget"),
    alternative: requireScore(input.alternative, "alternative"),
    trigger: requireScore(input.trigger, "trigger"),
    committee: requireScore(input.committee, "committee"),
    disqualified: input.disqualified ? String(input.disqualified) : "",
  };

  const total = dimensions.reduce((sum, [key]) => sum + account[key], 0);
  let tier;

  if (account.disqualified) tier = "T3";
  else if (total >= 7 && account.trigger >= 1) tier = "T1";
  else if (total >= 4) tier = "T2";
  else tier = "T3";

  return {
    ...account,
    total,
    tier,
    triggerGatePassed: account.trigger >= 1,
    action: actions[tier],
  };
}

function parseArgs(argv) {
  const parsed = {};
  const aliases = {
    "use-case": "useCase",
    budget: "budget",
    alternative: "alternative",
    trigger: "trigger",
    committee: "committee",
    name: "name",
    disqualified: "disqualified",
  };

  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (token === "--json" || token === "--help") {
      parsed[token.slice(2)] = true;
      continue;
    }
    if (token === "--input") {
      const path = argv[index + 1];
      if (!path) throw new Error("--input requires a JSON file path.");
      Object.assign(parsed, JSON.parse(readFileSync(resolve(path), "utf8")));
      index += 1;
      continue;
    }
    if (!token.startsWith("--") || !aliases[token.slice(2)]) {
      throw new Error(`Unknown argument: ${token}`);
    }
    const value = argv[index + 1];
    if (value === undefined) throw new Error(`${token} requires a value.`);
    parsed[aliases[token.slice(2)]] = value;
    index += 1;
  }

  return parsed;
}

function renderMarkdown(result) {
  const rows = dimensions
    .map(([key, label]) => `| ${label} | ${result[key]} |`)
    .join("\n");
  const disqualified = result.disqualified
    ? `\n**Hard disqualifier:** ${result.disqualified}\n`
    : "";

  return `# Account score — ${result.name}\n\n| Dimension | Score |\n|---|---:|\n${rows}\n\n**Total:** ${result.total}/10  \n**Tier:** ${result.tier}  \n**Trigger gate:** ${result.triggerGatePassed ? "passed" : "failed — account cannot be T1"}\n${disqualified}\n**Default next action:** ${result.action}`;
}

function help() {
  return `ICP account scorer\n\nUsage:\n  node tools/icp-account-scorer.mjs --name NAME --use-case 0|1|2 --budget 0|1|2 --alternative 0|1|2 --trigger 0|1|2 --committee 0|1|2 [--disqualified REASON] [--json]\n  node tools/icp-account-scorer.mjs --input account.json [--json]\n\nThe JSON keys are: name, useCase, budget, alternative, trigger, committee, disqualified.`;
}

const isMain = process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isMain) {
  try {
    const args = parseArgs(process.argv.slice(2));
    if (args.help) {
      console.log(help());
      process.exit(0);
    }
    const result = scoreAccount(args);
    console.log(args.json ? JSON.stringify(result, null, 2) : renderMarkdown(result));
  } catch (error) {
    console.error(`Error: ${error.message}\n\n${help()}`);
    process.exit(1);
  }
}
