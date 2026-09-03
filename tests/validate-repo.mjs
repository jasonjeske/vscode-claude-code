#!/usr/bin/env node
// Repo lint: skill frontmatter, internal Markdown links, strict JSON, CHANGELOG shape.
// Node standard library only. No dependencies, by design.
//
// Usage: node tests/validate-repo.mjs [rootDir]
// Exit:  0 all checks pass, 1 one or more FAIL lines, 2 usage or unreadable root.

import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, dirname, resolve } from "node:path";

const root = process.argv[2] ?? ".";

if (process.argv.length > 3) {
  console.log("usage: node tests/validate-repo.mjs [rootDir]");
  process.exit(2);
}

try {
  if (!statSync(root).isDirectory()) throw new Error("not a directory");
} catch {
  console.log(`FAIL ${root}: root is not a readable directory`);
  process.exit(2);
}

const failures = [];
const warnings = [];
let checks = 0;

const fail = (path, reason) => failures.push(`FAIL ${path}: ${reason}`);
const rel = (abs) => abs.slice(resolve(root).length + 1) || abs;

function walk(dir, out = []) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === ".git") continue;
    const full = join(dir, entry.name);
    if (entry.isDirectory()) walk(full, out);
    else out.push(full);
  }
  return out;
}

// ---------------------------------------------------------------------------
// Check 1: skill frontmatter
// ---------------------------------------------------------------------------

function frontmatterLines(text) {
  const lines = text.split(/\r?\n/);
  if (lines[0].trim() !== "---") return null;
  for (let i = 1; i < lines.length; i++) {
    if (lines[i].trim() === "---") return lines.slice(1, i);
  }
  return null;
}

// Reads a scalar, or a folded/literal block (key line plus indented continuation).
function frontmatterValue(fmLines, key) {
  const idx = fmLines.findIndex((l) => l.startsWith(`${key}:`));
  if (idx === -1) return null;
  let value = fmLines[idx].slice(key.length + 1).trim();
  if (["", ">", ">-", "|", "|-"].includes(value)) {
    const parts = [];
    for (let i = idx + 1; i < fmLines.length; i++) {
      const line = fmLines[i];
      if (line.trim() === "") continue;
      if (!/^\s/.test(line)) break;
      parts.push(line.trim());
    }
    value = parts.join(" ").trim();
  }
  if (
    (value.startsWith('"') && value.endsWith('"')) ||
    (value.startsWith("'") && value.endsWith("'"))
  ) {
    value = value.slice(1, -1);
  }
  return value;
}

const skillsDir = join(root, "skills");
if (existsSync(skillsDir)) {
  for (const entry of readdirSync(skillsDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const dirName = entry.name;
    const skillPath = join(skillsDir, dirName, "SKILL.md");
    const label = `skills/${dirName}/SKILL.md`;

    checks++;
    if (!existsSync(skillPath)) {
      fail(`skills/${dirName}`, "directory contains no SKILL.md");
      continue;
    }

    const text = readFileSync(skillPath, "utf8");
    const fm = frontmatterLines(text);

    checks++;
    if (fm === null) {
      fail(label, "no YAML frontmatter delimited by --- at the start of the file");
      continue;
    }

    checks++;
    const name = frontmatterValue(fm, "name");
    if (name === null) fail(label, "frontmatter has no name key");
    else if (name !== dirName)
      fail(label, `frontmatter name "${name}" does not equal directory name "${dirName}"`);

    checks++;
    const description = frontmatterValue(fm, "description");
    if (description === null) fail(label, "frontmatter has no description key");
    else if (description === "") fail(label, "frontmatter description is empty");

    checks++;
    if (!fm.some((l) => /^disable-model-invocation:\s*true\s*$/.test(l)))
      fail(label, "frontmatter is missing the literal disable-model-invocation: true");
  }
}

// ---------------------------------------------------------------------------
// Check 2: relative Markdown link and image targets resolve
// ---------------------------------------------------------------------------

const INLINE = /!?\[[^\]]*\]\(\s*([^)\s]+)(?:\s+"[^"]*")?\s*\)/g;
const REFERENCE = /^\[[^\]]+\]:\s*(\S+)/gm;

const isExternal = (t) => /^(https?:|mailto:|#|<)/.test(t);

for (const file of walk(root).filter((f) => f.endsWith(".md"))) {
  const text = readFileSync(file, "utf8");
  const base = dirname(file);
  const targets = [];
  for (const m of text.matchAll(INLINE)) targets.push(m[1]);
  for (const m of text.matchAll(REFERENCE)) targets.push(m[1]);

  for (const raw of targets) {
    const target = raw.trim();
    if (isExternal(target)) continue;
    const path = target.split("#")[0];
    if (path === "") continue;
    checks++;
    if (!existsSync(resolve(base, path)))
      fail(rel(file), `link target does not resolve: ${target}`);
  }
}

// ---------------------------------------------------------------------------
// Check 3: strict JSON
// ---------------------------------------------------------------------------

function parseStrict(path, label) {
  checks++;
  try {
    JSON.parse(readFileSync(path, "utf8"));
  } catch (error) {
    fail(label, `not strict JSON: ${error.message}`);
  }
}

const settings = join(root, "config", "vscode-settings.json");
if (existsSync(settings)) parseStrict(settings, "config/vscode-settings.json");

const fixtures = join(root, "tests", "fixtures");
if (existsSync(fixtures)) {
  for (const name of readdirSync(fixtures).filter((f) => f.endsWith(".json")))
    parseStrict(join(fixtures, name), `tests/fixtures/${name}`);
}

// ---------------------------------------------------------------------------
// Check 4: CHANGELOG shape
// ---------------------------------------------------------------------------

const changelog = join(root, "CHANGELOG.md");
if (!existsSync(changelog)) {
  warnings.push("WARN CHANGELOG.md missing");
} else {
  const text = readFileSync(changelog, "utf8");

  checks++;
  if (!/^## \[Unreleased\]/m.test(text))
    fail("CHANGELOG.md", "no ## [Unreleased] section");

  checks++;
  const released = text
    .split(/\r?\n/)
    .filter((l) => /^## \[\d+\.\d+\.\d+\]/.test(l));
  if (released.length < 2)
    fail("CHANGELOG.md", `expected at least 2 released version sections, found ${released.length}`);
}

// ---------------------------------------------------------------------------

for (const warning of warnings) console.log(warning);
for (const failure of failures) console.log(failure);

if (failures.length > 0) process.exit(1);

console.log(`OK ${checks} checks`);
