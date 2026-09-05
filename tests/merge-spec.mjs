#!/usr/bin/env node
// Executable specification of setup/FULL-ONBOARDING.md Stage 4's settings merge rules.
// The prose in Stage 4 is executed by a language model and cannot be run by a script.
// What CAN be pinned is the merge semantics themselves, which this file encodes and
// checks against committed fixtures.
//
// Node standard library only. No dependencies, by design.
//
// Usage: node tests/merge-spec.mjs [fixturesDir]
// Exit:  0 all cases pass, 1 any mismatch, 2 missing or unparseable fixture.

import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join } from "node:path";

const fixturesDir = process.argv[2] ?? "tests/fixtures";

// Stage 4: "never weaken a managed setting or security control".
// Stage 4's prose states that rule but names no settings keys, so these entries are
// the blueprint's seed list plus claudeCode.initialPermissionMode, which
// config/vscode-settings.json (the file Stage 4 reads) pins to "manual" as this
// repository's approval gate. See the build report assumptions ledger.
const DENYLIST = [
  {
    key: "security.workspace.trust.enabled",
    deny: (value) => value === false,
  },
  {
    key: "security.workspace.trust.startupPrompt",
    deny: (value) => value !== "always",
  },
  {
    key: "security.workspace.trust.untrustedFiles",
    deny: (value) => value === "open",
  },
  {
    key: "claudeCode.initialPermissionMode",
    deny: (value) => value !== "manual",
  },
];

const WEAKENING_KEY = /autoApprove|skipPermissions|bypassPermissions/i;

const isPlainObject = (value) =>
  value !== null && typeof value === "object" && !Array.isArray(value);

// (a) Drop candidate entries that would weaken a managed setting, even when the key
//     is absent from the existing file. That absence is exactly why a plain
//     existing-wins merge is not sufficient on its own.
function applyDenylist(candidate) {
  const kept = {};
  for (const [key, value] of Object.entries(candidate)) {
    const rule = DENYLIST.find((entry) => entry.key === key);
    if (rule && rule.deny(value)) {
      console.log(`DROPPED ${key}`);
      continue;
    }
    if (WEAKENING_KEY.test(key) && value) {
      console.log(`DROPPED ${key}`);
      continue;
    }
    kept[key] = value;
  }
  return kept;
}

// (b) and (c): any key present in existing wins, scalars and arrays wholesale and
//     nested objects merged per key; surviving candidate-only keys are added.
function merge(existing, candidate) {
  const result = { ...existing };
  for (const [key, candidateValue] of Object.entries(candidate)) {
    if (!(key in existing)) {
      result[key] = candidateValue;
      continue;
    }
    const existingValue = existing[key];
    if (isPlainObject(existingValue) && isPlainObject(candidateValue)) {
      result[key] = merge(existingValue, candidateValue);
    }
  }
  return result;
}

function deepEqual(a, b) {
  if (a === b) return true;
  if (Array.isArray(a) || Array.isArray(b)) {
    if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) return false;
    return a.every((value, index) => deepEqual(value, b[index]));
  }
  if (isPlainObject(a) && isPlainObject(b)) {
    const keysA = Object.keys(a);
    const keysB = Object.keys(b);
    if (keysA.length !== keysB.length) return false;
    return keysA.every((key) => key in b && deepEqual(a[key], b[key]));
  }
  return false;
}

function differences(expected, actual, prefix = "", out = []) {
  const keys = new Set([...Object.keys(expected), ...Object.keys(actual)]);
  for (const key of keys) {
    const path = prefix ? `${prefix}.${key}` : key;
    const e = expected[key];
    const a = actual[key];
    if (isPlainObject(e) && isPlainObject(a)) {
      differences(e, a, path, out);
      continue;
    }
    if (!deepEqual(e, a))
      out.push(`${path}: expected ${JSON.stringify(e)}, got ${JSON.stringify(a)}`);
  }
  return out;
}

function loadJson(path) {
  if (!existsSync(path)) {
    console.log(`FAIL ${path}: fixture not found`);
    process.exit(2);
  }
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch (error) {
    console.log(`FAIL ${path}: not strict JSON: ${error.message}`);
    process.exit(2);
  }
}

if (!existsSync(fixturesDir)) {
  console.log(`FAIL ${fixturesDir}: fixtures directory not found`);
  process.exit(2);
}

const cases = readdirSync(fixturesDir)
  .filter((name) => name.endsWith("-existing.json"))
  .map((name) => name.slice(0, -"-existing.json".length))
  .sort();

if (cases.length === 0) {
  console.log(`FAIL ${fixturesDir}: no <case>-existing.json fixtures found`);
  process.exit(2);
}

let failed = 0;

for (const name of cases) {
  const existing = loadJson(join(fixturesDir, `${name}-existing.json`));
  const candidate = loadJson(join(fixturesDir, `${name}-candidate.json`));
  const expected = loadJson(join(fixturesDir, `${name}-expected.json`));

  const merged = merge(existing, applyDenylist(candidate));

  if (deepEqual(merged, expected)) {
    console.log(`PASS ${name}`);
  } else {
    failed++;
    console.log(`FAIL ${name}: ${differences(expected, merged).join("; ")}`);
  }
}

process.exit(failed > 0 ? 1 : 0);
