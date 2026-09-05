// Validate the distributable instruction-only plugin and its complete skill inventory.
import assert from 'node:assert/strict';
import {readFileSync, readdirSync, existsSync} from 'node:fs';
const read = path => JSON.parse(readFileSync(path, 'utf8'));
const plugin = read('.claude-plugin/plugin.json');
const market = read('.claude-plugin/marketplace.json');
assert.equal(plugin.name, 'property-tax-workbench');
assert.match(plugin.version, /^\d+\.\d+\.\d+$/);
assert.equal(market.name, 'property-tax-learning');
assert.equal(market.plugins.length, 1);
assert.equal(market.plugins[0].name, plugin.name);
assert.equal(market.plugins[0].source, './');
const names = ['excel-workbook-review', 'financial-dashboard', 'prompt-coach',
  'property-tax-research', 'reconciliation-control-review', 'structured-work-request'];
assert.deepEqual(readdirSync('skills', {withFileTypes: true}).filter(e => e.isDirectory()).map(e => e.name).sort(), names.sort());
for (const name of names) assert.ok(existsSync(`skills/${name}/SKILL.md`));
assert.ok(existsSync('skills/property-tax-research/references/research-memo.md'));
for (const component of ['hooks', 'agents', 'commands', '.mcp.json', '.lsp.json', 'settings.json']) {
  assert.ok(!existsSync(component), `Unexpected active plugin component: ${component}`);
}
for (const field of ['hooks', 'agents', 'commands', 'mcpServers', 'lspServers', 'settings']) {
  assert.ok(!(field in plugin), `Unexpected plugin activation: ${field}`);
  assert.ok(!(field in market.plugins[0]), `Unexpected marketplace activation: ${field}`);
}
console.log('OK plugin metadata, six skills, research reference, instruction-only package');
