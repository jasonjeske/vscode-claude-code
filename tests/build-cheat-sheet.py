"""Build the separate, selectable-text beginner reference PDF. Maintainer use only."""
from pathlib import Path
from html import escape
import re

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'output/pdf/claude-code-vscode-cheat-sheet.pdf'
NAVY = colors.HexColor('#142E39')
TEAL = colors.HexColor('#087E82')
PALE = colors.HexColor('#EDF6F5')
GRAY = colors.HexColor('#52646C')
CORAL = colors.HexColor('#DA6A48')
styles = {
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.5, leading=14, textColor=NAVY, spaceAfter=6),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.3, leading=11.3, textColor=GRAY, spaceAfter=5),
    'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=12.2, leading=16, textColor=TEAL, spaceBefore=7, spaceAfter=5, keepWithNext=True),
    'prompt': ParagraphStyle('prompt', fontName='Helvetica', fontSize=10.4, leading=14.2, textColor=NAVY),
    'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=9.8, leading=13.2, textColor=NAVY),
}
story = []
prompts = []
titles = []

def p(text, style='body'):
    return Paragraph(text, styles[style])

def body(text):
    story.append(p(text))

def heading(text):
    story.append(p(text, 'heading'))

def prompt(label, text):
    prompts.append(text)
    box = Table([[p(escape(text).replace('\n', '<br/>'), 'prompt')]], colWidths=[528])
    box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PALE),
        ('LINEBEFORE', (0, 0), (0, -1), 2.5, TEAL),
        ('LEFTPADDING', (0, 0), (-1, -1), 11),
        ('RIGHTPADDING', (0, 0), (-1, -1), 11),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(KeepTogether([p(label, 'heading'), box, Spacer(1, 5)]))

def rows(data, widths=(130, 398)):
    table = Table([[p(c, 'cell') for c in row] for row in data], colWidths=widths, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.HexColor('#F3F6F7'), colors.white]),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(table)

def source(items):
    story.append(Spacer(1, 7))
    story.append(p('Reference: ' + ' | '.join(f'<a href="{url}" color="#087E82">{name}</a>' for name, url in items), 'small'))

def page(title, subtitle):
    if titles:
        story.append(PageBreak())
    titles.append((title, subtitle))

page('Your desk-side Claude Code guide', '01 / START HERE     VS Code extension first. No coding course required.')
body('<b>Keep this PDF beside VS Code.</b> Copy a shaded request into Claude\'s message box, change the details, and send it. These are ordinary words, not programming. Try one task at a time.')
heading('Three places, three different jobs')
rows([
    ('<b>Explorer</b>', 'VS Code\'s file list. Your project is simply a folder of related work.'),
    ('<b>Claude message box</b>', 'Ask questions, attach file references, and request saved outputs.'),
    ('<b>Command Palette</b>', 'A search box for VS Code actions. Press <b>Ctrl+Shift+P</b> (Mac: <b>Cmd+Shift+P</b>). Do not paste work prompts here.'),
])
heading('First session: open, connect, point to your files')
body('<b>1.</b> Open VS Code. Choose <b>File &gt; Open Folder</b> and select your practice folder. Use your company-approved storage for real work.')
body('<b>2.</b> Open Extensions: <b>Ctrl+Shift+X</b> (Mac: <b>Cmd+Shift+X</b>). Find <b>Claude Code</b> by <b>Anthropic</b>, then Install. Follow your employer\'s sign-in/setup instructions.')
body('<b>3.</b> In the Command Palette, search <b>Claude Code: Open in New Tab</b>. Complete Sign in if shown. The chat panel is your main workspace.')
body('<b>4.</b> Put practice files in this folder using Windows File Explorer or Mac Finder. In Claude, type <b>@</b> and select a file or folder suggestion. A file reference tells Claude where to look.')
prompt('First request - paste into Claude', 'I am new to Claude Code. Look at this project folder. Explain what is here in plain English and suggest one small practice task. Do not change any files yet.')
heading('Keyboard basics')
rows([
    ('<b>Copy / paste / save</b>', 'Windows: <b>Ctrl+C / Ctrl+V / Ctrl+S</b><br/>Mac: <b>Cmd+C / Cmd+V / Cmd+S</b>'),
    ('<b>Send / new line</b>', '<b>Enter</b> sends by default. <b>Shift+Enter</b> adds a line. Click inside Claude\'s message box first.'),
])
source([('VS Code interface', 'https://code.visualstudio.com/docs/getstarted/userinterface'), ('Official extension guide', 'https://code.claude.com/docs/en/vs-code')])

page('Add skills once. Then just ask.', '02 / SKILLS     A reusable procedure Claude can choose for your task.')
body('<b>A skill</b> is a set of instructions and sometimes supporting files. <b>A plugin</b> bundles capabilities. <b>A marketplace</b> lists plugins you can install. Adding the list does not install its plugins.')
heading('Install through the extension GUI')
body('<b>1.</b> In Claude, click <b>/ &gt; Customize &gt; Plugins</b> (or Manage plugins). You can also type <b>/plugins</b> to open the dialog.')
body('<b>2.</b> Select <b>Marketplaces</b>. Paste one source below into the repository field and click <b>Add</b>. Repeat for the second source.')
rows([
    ('<b>Office source</b>', '<font name="Courier">anthropics/skills</font>'),
    ('<b>Course source</b>', '<font name="Courier">jasonjeske/vscode-claude-code</font>'),
])
body('<b>3.</b> Select <b>Plugins</b>. Find and Install <b>document-skills</b> from Anthropic and <b>property-tax-workbench</b> from property-tax-learning. Choose <b>Install locally</b> for this practice repository, or <b>Install for you</b> for all your projects if allowed.')
body('<b>4.</b> Follow the restart banner if shown. Confirm both plugins are enabled. Use page 6 if the panel needs refreshing.')
heading('Your small starter toolkit')
rows([
    ('<b>Office</b>', '<b>xlsx</b>: spreadsheet work. <b>docx</b>: Word documents. <b>pptx</b>: slides. <b>pdf</b>: PDF reading and creation.'),
    ('<b>Property-tax workbench</b>', 'Workbook review, reconciliation checks, tax research, financial dashboards, prompt coaching, and structured work requests.'),
    ('<b>Optional course helpers</b>', 'Writing together, creating skills, guided learning, organizing files, and research writing. Add these when useful; the course lists the selected sources.'),
])
prompt('Check readiness', 'Which installed skills can help with Excel, Word, PowerPoint, PDFs, and reconciliation? Separate what is available from what needs setup. Suggest one tiny test using invented data.')
body('<b>Use normal language.</b> Claude can select relevant skills from their descriptions; automatic selection is not guaranteed. If needed, ask it to check its available skills. No long skill command is required.')
body('<b>Getting more:</b> use the <a href="https://github.com/jasonjeske/vscode-claude-code/blob/main/practice/STARTER-SKILLS.md" color="#087E82">course\'s five-helper checklist</a>. Keep complete skill folders and licenses. Skills do not supply Office licenses, browser control, or access to company systems.')
source([('Plugin installation', 'https://code.claude.com/docs/en/discover-plugins'), ('Anthropic skills', 'https://github.com/anthropics/skills'), ('Skill behavior', 'https://code.claude.com/docs/en/skills')])

page('Talk to Claude like a colleague', '03 / PROMPTS     Outcome + files + rules + deliverable + checks.')
body('<b>Be specific about the result, not the technology.</b> Say who will read it, which files to use, what must stay unchanged, and how you will know it is right. Replace words in [brackets] before sending.')
prompt('The reusable work request', 'Help me [outcome] for [audience]. Use [file or folder]. Keep the originals unchanged. Save [deliverable] in outputs. Check [totals, counts, or other success measure]. First explain your approach and ask only questions that would change the result.')
prompt('When you do not know what to ask', 'Help me turn this into a clear request: [describe the task in your own words]. Ask me up to three essential questions, one at a time. Then give me a prompt I can review and use.')
heading('Useful follow-ups - say exactly what you need')
rows([
    ('<b>Learn</b>', 'Explain that as if this is my first day. Give me one example and one small exercise.'),
    ('<b>Plan</b>', 'Break this into three steps. Tell me what each step will produce.'),
    ('<b>Proceed</b>', 'Proceed with that plan. Preserve the source files and save new outputs.'),
    ('<b>Correct</b>', 'Use tax year 2026, not 2025. Recheck every output affected by that change.'),
    ('<b>Verify</b>', 'Show the source file, sheet, and row behind each total. Flag anything you could not verify.'),
    ('<b>Simplify</b>', 'Make this shorter and easier to read. Keep the numbers and qualifications.'),
    ('<b>Improve</b>', 'What is the weakest part of this result? Fix it and explain the change.'),
    ('<b>Finish</b>', 'List the files you saved, the checks that passed, and what still needs my review.'),
])
prompt('Save a longer request instead of repeatedly pasting it', 'Save our agreed task, source files, output names, and success checks in TASK.md. Use plain English. Next time I want to ask you to read TASK.md and continue.')
body('<b>.md means Markdown:</b> an ordinary text document you can edit in VS Code. Chat history is useful, but a saved task file gives the next session a clear starting point.')

page('From spreadsheets to a meeting', '04 / OFFICE WORK     Request it. Open it. Check it. Improve it.')
body('Use a practice folder with <b>inputs</b> for source copies and <b>outputs</b> for results. Tell Claude your actual folder name if it differs. Run these requests separately; review each result before the next.')
prompt('1 / Combine Excel files and reconcile', 'Inspect the Excel files in inputs. Identify sheets, columns, tax years, and matching keys before combining. Keep parcel IDs as text and originals unchanged. Save outputs/reconciliation.xlsx with source references, duplicates, unmatched items, differences, and a Checks sheet. Reconcile counts and totals back to every input. Separate net difference from total absolute differences.')
body('<b>Your check:</b> open the workbook in Excel. Read Checks, inspect exceptions, and trace one record to each input. Ask Claude to explain failed checks before moving on.')
prompt('2 / Turn checked results into a dashboard', 'Use outputs/reconciliation.xlsx to create outputs/dashboard.html for our review meeting. Show book total, bill total, net difference, exception count, and reconciliation status. Add a state comparison chart and useful filters. Explain metric definitions and check every number and filter total against the workbook. Make it readable on a meeting screen and label it with the data date.')
body('<b>Your check:</b> open the HTML file in a browser. Compare headline totals and one filtered view with Excel. The report is a snapshot; ask Claude to rebuild it when inputs change.')
prompt('3 / Prepare the meeting pack', 'Use the checked workbook to save outputs/briefing.docx and outputs/meeting.pptx. Make a one-page briefing and five slides: summary, state comparison, exceptions, decisions needed, next actions. Use consistent numbers, readable charts, and clear source notes. Separate verified findings from unresolved items.')
body('<b>Your check:</b> open the files in Word and PowerPoint. Check page breaks, chart labels, readability, and agreement with Excel. VS Code is for project files and instructions; use Office to review Office layouts.')
prompt('4 / Extract a PDF into Excel', 'Read the PDF I reference. Extract its property identifiers and amounts into outputs/pdf-extract.xlsx. Include the PDF page for every row. Flag unclear text or scanned pages; do not guess. Reconcile extracted amounts to printed totals where available.')
body('<b>Your check:</b> compare a few extracted rows and the totals against the original PDF. If tools or dependencies are missing, ask Claude what is needed and use your approved setup process.')

page('Research, remember, reuse', '05 / BUILD GOOD HABITS     Save evidence and successful procedures.')
prompt('Research property tax with a useful saved result', 'Research [question] for [state and county], [property type], and [tax year]. Use current official government sources. Separate enacted rules from proposals and explain applicability. Save outputs/research.md with findings, exact source links, supporting sections, dates checked, and unresolved questions. If browsing is unavailable, tell me; do not invent current rules.')
prompt('Bring reviewed research into your work', 'Use outputs/research.md to add a Research sheet to a new copy of our workbook. Include finding, jurisdiction/year, source link, date checked, and review status. Add a short research note to the dashboard. Keep financial totals unchanged unless I approve a specific, supported adjustment.')
body('<b>Before relying on a deadline or rule:</b> open its official source and confirm the jurisdiction, year, property type, and applicable exceptions. Mark unresolved interpretations for professional review.')
heading('Turn a successful routine into a skill')
body('Project skills live in <font name="Courier">.claude/skills/name/SKILL.md</font>. Personal skills normally live under <font name="Courier">~/.claude/skills</font>; <b>~</b> means your home folder. Claude can create the folder and file for you.')
prompt('Create a small skill - no coding required', 'Save our successful procedure as .claude/skills/monthly-review/SKILL.md. Include a YAML header with name and description explaining when to use it automatically, then a short checklist, output names, and checks. Exclude client data. Test on invented data and show the result.')
prompt('Improve an existing skill', 'Add a duplicate parcel-ID check to our monthly-review skill, scoped by jurisdiction and tax year. Back up the skill and show the change. Test one duplicate and one valid repeat across years. Preserve the upstream plugin.')
body('Keep supporting files with the skill. Modern Claude Code detects many edits automatically. Restart if a new skills directory is not recognized; then try a normal work request.')
heading('Keep preferences separate from procedures')
body('<b>CLAUDE.md</b> holds project instructions; <b>~/.claude/CLAUDE.md</b> holds personal instructions across projects. Ask Claude to merge your preferences, preserve existing instructions, and show the file for review. Do not paste prose into settings.json. Keep detailed procedures in skills.')
source([('Create and update skills', 'https://code.claude.com/docs/en/skills'), ('CLAUDE.md and memory', 'https://code.claude.com/docs/en/memory')])

page('Commands, recovery, and tomorrow', '06 / QUICK REFERENCE     Use the GUI first; short commands are optional.')
body('Type <b>/</b> in Claude to browse commands, or use <b>Customize &gt; Slash commands</b> in newer versions. A terminal icon opens that action in the terminal. Availability varies by version and company setup.')
rows([
    ('<b>/plugins</b>', 'Open the extension\'s plugin manager.'),
    ('<b>/compact</b>', 'Summarize a long conversation to free context while continuing the task. Save important decisions first.'),
    ('<b>/btw</b>', 'Ask a side question. Example: <font name="Courier">/btw What is a reconciliation?</font>'),
    ('<b>/usage</b>', 'Account and usage details when signed in through Claude.ai. Not offered on third-party provider connections.'),
    ('<b>More, if listed</b>', '<b>/help</b>: help. <b>/skills</b>: available skills. <b>/context</b>: context use. <b>/clear</b>: fresh conversation, not a file rollback. Use GUI controls if a command is absent.'),
])
heading('Daily GUI controls')
body('<b>Plan first:</b> use the mode selector below the message box and choose Plan. Choose Manual when you want approval prompts while working. <b>New task:</b> Command Palette &gt; Claude Code: Open in New Tab. <b>Resume:</b> Session history. <b>Model:</b> click the model name or use Switch model in the command menu.')
heading('Stop, close, refresh: they are different')
body('<b>Stop:</b> click Stop and wait. Existing file changes remain. <b>Close:</b> after work stops and files are saved, click the tab\'s X. Closing a tab is not a reliable way to cancel work.')
body('<b>Refresh a stuck panel or missing installation:</b><br/>1. Save edited files with <b>Ctrl+S</b> (Mac: <b>Cmd+S</b>).<br/>2. Open the Command Palette: <b>Ctrl+Shift+P</b> (Mac: <b>Cmd+Shift+P</b>).<br/>3. Search <b>Developer: Reload Window</b> and press Enter.<br/>4. Reopen Claude Code. Resume through Session history, or open a new conversation to check the installed skills.')
body('<b>Still stuck?</b> Quit and reopen VS Code: Windows <b>File &gt; Exit</b>; Mac <b>Code &gt; Quit Visual Studio Code</b>. Reopen your project. For sign-in or company connection errors, send IT the error text with credentials and private content removed.')
prompt('Before you finish for the day', 'Save NEXT-STEPS.md with our goal, input and output paths, verified checks, unresolved items, and the next action. Tomorrow I will ask you to read it and continue.')
body('<b>Optional terminal:</b> Command Palette &gt; <b>Claude Code: Open in Terminal</b>. Once Claude starts, use the same ordinary prompts. <b>Ctrl+C</b> interrupts; <b>Ctrl+D</b> exits. Using <font name="Courier">claude</font> in a plain shell requires the standalone CLI.')
source([('Extension controls', 'https://code.claude.com/docs/en/vs-code'), ('Command reference', 'https://code.claude.com/docs/en/commands'), ('Terminal keys', 'https://code.claude.com/docs/en/interactive-mode')])

class CheatSheet(SimpleDocTemplate):
    def beforePage(self):
        canvas = self.canv
        n = self.page
        if n > len(titles):
            raise ValueError('Content overflowed its designed page; shorten or reflow it')
        title, subtitle = titles[n - 1]
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, 710, 612, 82, fill=1, stroke=0)
        canvas.setFillColor(CORAL)
        canvas.rect(42, 764, 24, 3, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont('Helvetica-Bold', 21)
        canvas.drawString(42, 738, title)
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(colors.HexColor('#C6E0E2'))
        canvas.drawString(42, 722, subtitle)
        canvas.setStrokeColor(colors.HexColor('#D7E1E4'))
        canvas.line(42, 35, 570, 35)
        canvas.setFillColor(GRAY)
        canvas.setFont('Helvetica', 8)
        canvas.drawString(42, 22, 'CLAUDE CODE / WORKDAY CHEAT SHEET')
        canvas.drawRightString(570, 22, f'Checked 07 Sep 2026  |  {n} / 6')
        canvas.bookmarkPage(f'page-{n}')
        canvas.addOutlineEntry(title, f'page-{n}', level=0)
        canvas.restoreState()

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = CheatSheet(str(OUTPUT), pagesize=letter, leftMargin=42, rightMargin=42,
    topMargin=96, bottomMargin=45, title='Claude Code in VS Code - Workday Cheat Sheet',
    author='Claude Code Office Course', subject='Beginner GUI reference and copyable workplace prompts',
    pageCompression=1, invariant=1)
doc.build(story)

reader = PdfReader(OUTPUT)
assert len(reader.pages) == 6, f'Expected six designed pages, got {len(reader.pages)}'
normalized = lambda value: re.sub(r'\s+', '', value)
extracted = [normalized(page.extract_text()) for page in reader.pages]
for request in prompts:
    assert any(normalized(request) in text for text in extracted), 'A copyable request was lost or split across pages'
for index, (title, _) in enumerate(titles):
    assert normalized(title) in extracted[index], f'Wrong title on page {index + 1}'
assert len(reader.outline) == 6
assert not reader.is_encrypted
print(f'Created {OUTPUT}: 6 pages, {len(prompts)} complete selectable requests, six bookmarks')
