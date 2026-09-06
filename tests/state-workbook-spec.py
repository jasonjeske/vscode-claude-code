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
