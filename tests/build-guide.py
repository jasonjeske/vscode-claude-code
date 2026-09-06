"""Generate the learner PDF from the single Markdown course. Maintainer use only."""
from pathlib import Path
import hashlib
import re
import textwrap
from html import escape
from urllib.parse import urljoin

from markdown_it import MarkdownIt
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    XPreformatted, KeepTogether, CondPageBreak,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'output/pdf/claude-code-office-guide.pdf'
BASE = 'https://github.com/jasonjeske/vscode-claude-code/blob/main/'
source = (ROOT / 'README.md').read_text()
source_hash = hashlib.sha256(source.encode()).hexdigest()
md = MarkdownIt('commonmark').enable('table')
tokens = md.parse(source)
ink = colors.HexColor('#243b43')
accent = colors.HexColor('#22606a')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle('BodyCourse', fontName='Helvetica', fontSize=10.5,
    leading=15, textColor=ink, spaceAfter=8))
styles.add(ParagraphStyle('TitleCourse', fontName='Helvetica-Bold', fontSize=27,
    leading=32, textColor=accent, spaceAfter=18))
styles.add(ParagraphStyle('LessonCourse', fontName='Helvetica-Bold', fontSize=21,
    leading=26, textColor=accent, spaceAfter=14, keepWithNext=True))
styles.add(ParagraphStyle('SectionCourse', fontName='Helvetica-Bold', fontSize=13,
    leading=18, textColor=ink, spaceBefore=8, spaceAfter=8, keepWithNext=True))
styles.add(ParagraphStyle('LabelCourse', parent=styles['BodyCourse'],
    fontName='Helvetica-Bold', keepWithNext=True, spaceAfter=6))
styles.add(ParagraphStyle('TableCourse', parent=styles['BodyCourse'], fontSize=9,
    leading=12, spaceAfter=0))
styles.add(ParagraphStyle('PromptCourse', fontName='Courier', fontSize=9.2,
    leading=13.2, textColor=ink, backColor=colors.HexColor('#f2f5f5'),
    borderColor=colors.HexColor('#cedbde'), borderWidth=0.6, borderPadding=10,
    spaceBefore=4, spaceAfter=14))


def slug(s):
    return re.sub(r'[^\w\-\s]', '', s.lower()).replace(' ', '-')


def inline(items):
    out = []
    for t in items or []:
        if t.type in ('text', 'code_inline'):
            text = escape(t.content)
            out.append('<font name="Courier">'+text+'</font>' if t.type == 'code_inline' else text)
        elif t.type in ('softbreak', 'hardbreak'):
            out.append(' ' if t.type == 'softbreak' else '<br/>')
        elif t.type in ('strong_open', 'strong_close', 'em_open', 'em_close'):
            out.append({'strong_open':'<b>','strong_close':'</b>',
                        'em_open':'<i>','em_close':'</i>'}[t.type])
        elif t.type == 'link_open':
            href = t.attrGet('href')
            target = href if href.startswith('#') else urljoin(BASE, href)
            out.append(f'<a href="{escape(target, quote=True)}" color="#22606a">')
        elif t.type == 'link_close':
            out.append('</a>')
        elif t.type == 'html_inline':
            out.append(escape(t.content))
        elif t.type == 'image':
            raise ValueError('Course prompts must not be images')
    return ''.join(out)


class GuideDoc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'course_heading'):
            title, key, level = flowable.course_heading
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=level, closed=False)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#c7d5d7'))
    canvas.line(48, 41, 564, 41)
    canvas.setFillColor(accent)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(48, 27, 'CLAUDE CODE IN VS CODE  |  OFFICE WORK PRACTICE')
    canvas.drawRightString(564, 27, str(doc.page))
    canvas.restoreState()

story = []
i = 0
lists = []
item_prefix = None
while i < len(tokens):
    t = tokens[i]
    if t.type == 'heading_open':
        content = tokens[i+1]
        title = content.content
        level = int(t.tag[1])
        if level == 2 and re.match(r'\d+\.', title):
            story.extend([CondPageBreak(285), Spacer(1, 14)])
        style = 'TitleCourse' if level == 1 else 'LessonCourse' if level == 2 else 'SectionCourse'
        para = Paragraph(inline(content.children), styles[style])
        if level <= 2:
            para.course_heading = (title, slug(title), 0 if level == 1 else 1)
        story.append(para)
        i += 3
        continue
    if t.type == 'paragraph_open':
        token = tokens[i+1]
        body = inline(token.children)
        prefix = item_prefix or ''
        item_prefix = None
        label = token.content.startswith(('**Copy', '**Then copy', '**Follow-up', '**Only in', '**Now, inside'))
        style = styles['LabelCourse' if label else 'BodyCourse']
        if lists:
            style = ParagraphStyle('ListCourse', parent=style,
                leftIndent=14*len(lists), firstLineIndent=-12, spaceAfter=5)
        para = Paragraph(prefix+body, style)
        para.course_prompt_label = token.content.rstrip('*').endswith(':')
        story.append(para)
        i += 3
        continue
    if t.type == 'fence':
        lines = []
        for line in t.content.rstrip('\n').splitlines():
            lines.extend(textwrap.wrap(line, width=83, replace_whitespace=False,
                drop_whitespace=True, break_long_words=False, break_on_hyphens=False) or [''])
        code = XPreformatted(escape('\n'.join(lines)), styles['PromptCourse'])
        following = []
        if i+3 < len(tokens) and tokens[i+1].type == 'paragraph_open' and tokens[i+2].content.startswith(('**Check', '**Open and check')):
            following.append(Paragraph(inline(tokens[i+2].children), styles['BodyCourse']))
            i += 3
        label = []
        while story and isinstance(story[-1], Paragraph) and (
            getattr(story[-1], 'course_prompt_label', False) or
            getattr(story[-1].style, 'keepWithNext', False)
        ):
            label.insert(0, story.pop())
        story.append(KeepTogether(label+[code]+following))
    elif t.type in ('bullet_list_open', 'ordered_list_open'):
        lists.append({'ordered':t.type == 'ordered_list_open', 'next':int(t.attrGet('start') or 1)})
    elif t.type in ('bullet_list_close', 'ordered_list_close'):
        lists.pop()
    elif t.type == 'list_item_open':
        group = lists[-1]
        item_prefix = f'{group["next"]}. ' if group['ordered'] else '&#8226; '
        group['next'] += 1
    elif t.type == 'table_open':
        rows = []
        row = []
        j = i+1
        while tokens[j].type != 'table_close':
            tt = tokens[j]
            if tt.type == 'tr_open': row = []
            elif tt.type == 'inline': row.append(Paragraph(inline(tt.children),styles['TableCourse']))
            elif tt.type == 'tr_close': rows.append(row)
            j += 1
        count = len(rows[0])
        widths = [240,276] if count == 2 else [196,266,54] if count == 3 else [516/count]*count
        table = Table(rows, colWidths=widths, repeatRows=1, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e6eff0')),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f7f9f9')]),
            ('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#d2dcde')),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
            ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
        ]))
        story.extend([KeepTogether([table]) if count == 2 and rows[0][0].getPlainText() == 'Lesson' else table, Spacer(1,12)])
        i=j
    elif t.type == 'hr':
        story.append(Spacer(1,12))
    i += 1

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = GuideDoc(str(OUTPUT), pagesize=letter, leftMargin=48,rightMargin=48,
    topMargin=45,bottomMargin=56, title='Claude Code in VS Code: your everyday Office assistant',
    author='vscode-claude-code course', subject='Full course from README.md; SHA256 '+source_hash,
    pageCompression=1, invariant=1)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print('Built',OUTPUT.relative_to(ROOT))
