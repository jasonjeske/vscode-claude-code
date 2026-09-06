"""Read the shipped XLSX with Python's standard library; verify course facts independently."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

NS = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
book = Path(__file__).resolve().parents[1] / "practice/practice.xlsx"
populations = []
with ZipFile(book) as archive:
    assert not any("vbaProject" in name or "externalLinks/" in name for name in archive.namelist())
    wb = ET.fromstring(archive.read("xl/workbook.xml"))
    assert [s.attrib["name"] for s in wb.findall("x:sheets/x:sheet", NS)] == ["Book", "Bill"]
    for number, expected in [(1, 1000), (2, 1100)]:
        sheet = ET.fromstring(archive.read(f"xl/worksheets/sheet{number}.xml"))
        cells = {cell.attrib["r"]: cell for cell in sheet.findall("x:sheetData/x:row/x:c", NS)}
        def value(address):
            return cells[address].find("x:v", NS).text
        rows = {}
        for row in range(4, 8):
            assert value(f"A{row}") == "OH" and value(f"B{row}") == "2026"
            key = value(f"C{row}")
            assert cells[f"C{row}"].attrib["t"] == "str"
            assert len(key) == 6 and key.startswith("00")
            assert key not in rows
            rows[key] = int(value(f"D{row}"))
        assert sum(rows.values()) == expected == int(value("D9"))
        assert cells["D9"].find("x:f", NS).text == "SUM(D4:D7)"
        assert not any(c.attrib.get("t") == "e" for c in cells.values())
        populations.append(rows)
a, b = populations
common = a.keys() & b.keys()
assert common == {"001101", "001102", "001103"}
diffs = {key: b[key] - a[key] for key in common}
assert diffs == {"001101": 0, "001102": 10, "001103": -10}
assert sum(diffs.values()) == 0 and sum(map(abs, diffs.values())) == 20
assert a.keys() - b.keys() == {"001104"} and b.keys() - a.keys() == {"001105"}
assert a["001104"] == 400 and b["001105"] == 500
assert sum(b.values()) - sum(a.values()) == sum(diffs.values()) + 500 - 400 == 100
print("OK shipped XLSX: text IDs, formulas/caches, full populations, offsetting differences, bridge")

# The two consolidation sources must remain independently auditable and preserve text IDs.
combined = []
for state, ids, amounts in [("OH", ["000101", "000102"], [100, 200]),
                            ("TX", ["000201", "000202"], [300, 400])]:
    with ZipFile(book.parent / f"{state}-bills.xlsx") as archive:
        assert not any("vbaProject" in n or "externalLinks/" in n for n in archive.namelist())
        wb = ET.fromstring(archive.read("xl/workbook.xml"))
        assert [s.attrib["name"] for s in wb.findall("x:sheets/x:sheet", NS)] == ["Bills"]
        sheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        cells = {c.attrib["r"]: c for c in sheet.findall("x:sheetData/x:row/x:c", NS)}
        def value(address):
            return cells[address].find("x:v", NS).text
        for row, key, amount in zip([5, 6], ids, amounts):
            assert value(f"A{row}") == state and value(f"B{row}") == "2026"
            assert cells[f"C{row}"].attrib["t"] == "str" and value(f"C{row}") == key
            assert int(value(f"D{row}")) == amount
            combined.append((state, key, amount))
        assert int(value("D8")) == sum(amounts)
        assert cells["D8"].find("x:f", NS).text == "SUM(D5:D6)"
        assert not any(c.attrib.get("t") == "e" for c in cells.values())
assert len(combined) == 4 and len({key for _, key, _ in combined}) == 4
assert sum(amount for _, _, amount in combined) == 1000
print("OK consolidation sources: 4 detail rows, text IDs, OH 300 + TX 700 = 1000; total rows excluded")

# The larger meeting workshop is separate from the tiny fixtures above.
# Read both inline and shared strings so native Excel saves remain verifiable.
def xlsx_cells(archive, sheet_path):
    shared=[]
    if 'xl/sharedStrings.xml' in archive.namelist():
        shared=[''.join(si.itertext()) for si in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
    result={}
    for c in ET.fromstring(archive.read(sheet_path)).findall('x:sheetData/x:row/x:c',NS):
        kind=c.attrib.get('t')
        assert kind!='e', f'Formula error in {sheet_path}: {c.attrib["r"]}'
        raw=c.find('x:v',NS)
        value=raw.text if raw is not None else None
        if kind=='s': value=shared[int(value)]
        elif kind=='inlineStr': value=''.join(c.find('x:is',NS).itertext())
        elif value is not None and kind not in ('str','b'): value=float(value)
        result[c.attrib['r']]=(value,kind,c.find('x:f',NS))
    return result

meeting={}
for state in ('OH','TX'):
    for side in ('book','bills'):
        with ZipFile(book.parent/'meeting-inputs'/f'{state}-{side}.xlsx') as archive:
            cells=xlsx_cells(archive,'xl/worksheets/sheet1.xml')
            rows={}
            for row in range(5,11):
                key,kind,_=cells[f'C{row}']
                assert isinstance(key,str) and len(key)==6 and key.startswith('0')
                assert key not in rows and cells[f'A{row}'][0]==state and int(cells[f'B{row}'][0])==2026
                rows[key]=cells[f'E{row}'][0]
            assert cells['E12'][2].text=='SUM(E5:E10)'
            meeting[state,side]=rows
expected_totals={('OH','book'):90000,('OH','bills'):92000,('TX','book'):100000,('TX','bills'):101200}
assert {k:sum(v.values()) for k,v in meeting.items()}==expected_totals
book_rows={k:v for (st,side),rows in meeting.items() if side=='book' for k,v in rows.items()}
bill_rows={k:v for (st,side),rows in meeting.items() if side=='bills' for k,v in rows.items()}
common=book_rows.keys() & bill_rows.keys()
differences=[bill_rows[k]-book_rows[k] for k in common]
assert len(book_rows.keys()|bill_rows.keys())==13 and len(common)==11
assert sum(d==0 for d in differences)==8
assert sum(differences)==1200 and sum(map(abs,differences))==2200
assert sum(bill_rows.values())-sum(book_rows.values())==3200==1200+16000-14000
with ZipFile(book.parent/'meeting-results/meeting-reconciliation.xlsx') as archive:
    names=[s.attrib['name'] for s in ET.fromstring(archive.read('xl/workbook.xml')).findall('x:sheets/x:sheet',NS)]
    totals=xlsx_cells(archive,f'xl/worksheets/sheet{names.index("State totals")+1}.xml')
    checks=xlsx_cells(archive,f'xl/worksheets/sheet{names.index("Checks")+1}.xml')
    assert all(checks[f'D{row}'][0]=='OK' for row in range(5,17)), 'Native Excel caches must contain 12 OK checks'
    assert [totals[a][0] for a in ('D9','D19','D20','D23')]==[3200,1200,2200,3200]
print('OK meeting workshop: four sources, text IDs, 13 keys, five exceptions, bridge, native Excel cached checks')

# Research must preserve the five financial sheets; PDF extraction must retain units.
with ZipFile(book.parent/'meeting-results/meeting-reconciliation.xlsx') as base, ZipFile(book.parent/'meeting-results/meeting-with-research.xlsx') as revised:
    for n in range(1,6):
        a=xlsx_cells(base,f'xl/worksheets/sheet{n}.xml')
        b=xlsx_cells(revised,f'xl/worksheets/sheet{n}.xml')
        for key,(value,kind,formula) in a.items():
            assert b[key][0]==value, f'Research changed {n}!{key}'
            assert (b[key][2].text if b[key][2] is not None else None)==(formula.text if formula is not None else None)
with ZipFile(book.parent/'meeting-results/pdf-summary.xlsx') as archive:
    cells=xlsx_cells(archive,'xl/worksheets/sheet1.xml')
    expected=[(90000,100000,190000),(92000,101200,193200),(2000,1200,3200),(7,6,13),(3,5,8),(4,1,5),(0,1200,1200),(1000,1200,2200)]
    for row,values in enumerate(expected,5):
        assert tuple(cells[f'{col}{row}'][0] for col in 'DEF')==values
        assert cells[f'A{row}'][0]==1
        assert cells[f'C{row}'][0]==('count' if row in (8,9,10) else 'USD')
    checks=xlsx_cells(archive,'xl/worksheets/sheet2.xml')
    assert all(checks[f'G{r}'][0]=='OK' for r in range(5,29))
print('OK research preserves financial cells; PDF extraction has 24 verified values, units and page references')
