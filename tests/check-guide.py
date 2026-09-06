"""Check the handoff PDF against its Markdown source, including every copyable block."""
from pathlib import Path
import hashlib
import re
from markdown_it import MarkdownIt
from pypdf import PdfReader

root=Path(__file__).resolve().parents[1]
source=(root/'README.md').read_text()
reader=PdfReader(root/'output/pdf/claude-code-office-guide.pdf')
normalize=lambda s: re.sub(r'\s+','',s)
pages=[page.extract_text() or '' for page in reader.pages]
text=normalize('\n'.join(pages))
tokens=MarkdownIt('commonmark').enable('table').parse(source)
prompts=[t.content for t in tokens if t.type=='fence']
for number, prompt in enumerate(prompts,1):
    assert normalize(prompt) in text, f'PDF lost or changed copyable block {number}'
for i,t in enumerate(tokens):
    if t.type=='heading_open':
        assert normalize(tokens[i+1].content) in text, f'PDF missing heading: {tokens[i+1].content}'
expected=hashlib.sha256(source.encode()).hexdigest()
assert reader.metadata.subject.endswith(expected), 'PDF is stale; rebuild after editing README.md'
assert 12<=len(pages)<=24, f'PDF should remain a compact complete course: {len(pages)} pages'
assert all(len(t.strip())>150 for t in pages), 'Unexpected near-empty PDF page'
headings = {tokens[i+1].content for i,t in enumerate(tokens) if t.type=='heading_open'}
for number, page in enumerate(pages, 1):
    last_line = page.splitlines()[-1].strip()
    assert last_line not in headings, f'Stranded PDF heading on page {number}'
    assert not last_line.endswith(':'), f'Stranded PDF prompt label on page {number}'
assert len(reader.outline)>0, 'PDF needs navigation bookmarks'
assert not reader.is_encrypted, 'Learner must be able to copy PDF text'
prefs=(root/'GLOBAL-CLAUDE.md').read_text().split('```text\n')[1].split('\n```')[0]
assert prefs in source, 'Standalone global preferences differ from the course'
assert '/property-tax-workbench:' not in text
print(f'OK PDF: {len(pages)} pages, {len(prompts)} exact text blocks, all headings, bookmarks, source hash, preferences')
