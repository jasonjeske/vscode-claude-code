// Maintainer checks. No package installation needed.
import assert from 'node:assert/strict';
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { resolve, dirname, relative, extname } from 'node:path';
const root = process.cwd();
function walk(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap(e => {
    if (e.name === '.git') return [];
    const path = resolve(dir, e.name);
    return e.isDirectory() ? walk(path) : [path];
  });
}
const files = walk(root);
const read = path => readFileSync(path, 'utf8');
const markdown = files.filter(p => extname(p) === '.md' && !p.endsWith('/CHANGELOG.md'));
function anchors(path) {
  const seen = new Map();
  return [...read(path).matchAll(/^#{1,6}\s+(.+)$/gm)].map(m => {
    let slug = m[1].toLowerCase().replace(/[^\p{L}\p{N}_\-\s]/gu, '').replace(/ /g, '-');
    const count = seen.get(slug) ?? 0;
    seen.set(slug, count + 1);
    return count ? `${slug}-${count}` : slug;
  });
}
let links = 0;
for (const path of markdown) {
  const source = read(path);
  for (const m of source.matchAll(/!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)/g)) {
    if (/^[a-z][a-z0-9+.-]*:/i.test(m[1])) continue;
    const [target, hash] = m[1].split('#');
    const dest = target ? resolve(dirname(path), decodeURIComponent(target)) : path;
    assert(existsSync(dest), `Broken link in ${relative(root, path)}: ${m[1]}`);
    if (hash && extname(dest) === '.md') assert(anchors(dest).includes(decodeURIComponent(hash)), `Missing anchor: ${m[1]}`);
    links++;
  }
}
for (const path of files.filter(p => extname(p) === '.json')) JSON.parse(read(path));
const manifest = JSON.parse(read(resolve(root, '.claude-plugin/plugin.json')));
const market = JSON.parse(read(resolve(root, '.claude-plugin/marketplace.json')));
assert.equal(market.plugins[0].name, manifest.name);
assert.equal(market.plugins[0].source, './');
assert.match(manifest.version, /^\d+\.\d+\.\d+$/);
const skills = readdirSync(resolve(root, 'skills'), { withFileTypes: true })
  .filter(entry => entry.isDirectory())
  .map(entry => entry.name);
for (const name of skills) {
  const skill = read(resolve(root, 'skills', name, 'SKILL.md'));
  assert.match(skill, new RegExp(`^---\\nname: ${name}\\n`));
  assert.match(skill, /\ndescription: .+\n/);
  assert(!skill.includes('TODO'), `Unfinished skill ${name}`);
  assert(!/disable-model-invocation:\s*true/.test(skill), `Automatic selection disabled: ${name}`);
}
// The learner workflow must work without memorizing plugin command names.
for (const path of markdown.filter(p => p.includes('/lessons/') || /\/(README|HELP)\.md$/.test(p))) {
  assert(!/\/property-tax-workbench:/.test(read(path)), `Explicit skill command in learner path: ${path}`);
}
// Prompts must remain real copyable text in the beginner reading path.
const learnerFiles = markdown.filter(p => p.includes('/lessons/') || /\/(README|HELP|GLOBAL-CLAUDE)\.md$/.test(p));
for (const path of learnerFiles) {
  assert(!/!\[[^\]]*\]\(/.test(read(path)), `Prompt image in learner path: ${path}`);
  assert(!/^> /m.test(read(path)), `Use a fenced block for copyable requests: ${path}`);
}
const course = read(resolve(root, 'README.md'));
for (const name of [...skills, 'xlsx', 'docx', 'pptx', 'pdf', 'doc-coauthoring', 'file-organizer', 'content-research-writer', 'academy-guide', 'skill-creator']) {
  assert(course.includes(name), `Skill missing from course: ${name}`);
}
assert(course.includes('```text\n'), 'Course needs copyable prompt blocks');
console.log(`OK: ${links} local links, ${skills.length} discoverable skills, copyable course, JSON manifests`);
