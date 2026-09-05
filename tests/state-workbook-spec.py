"""Read the shipped XLSX with Python's standard library; verify course facts independently."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

NS = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
book = Path(__file__).resolve().parents[1] / "state-project/inputs/state-practice.xlsx"
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
