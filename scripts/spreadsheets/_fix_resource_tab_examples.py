"""Fix: example formulas on the resource tabs (Color Key / Using This
Workbook / Excel Formulas / Named Ranges / Data Analytics / Claude for Excel
/ Welcome) should be DISPLAYED as formula text, not EVALUATED as live
formulas. openpyxl stores any cell whose value starts with '=' as a formula.
In Excel that means "=PV(rate,...)" renders as #NAME? (or worse, an actual
number) instead of the intended teaching example.

Fix strategy: after the workbook is saved, rewrite each offending cell in
the XML from <c><f>...</f></c> formula form into inline-string form so
Excel treats it as plain text.
"""
import re, shutil, zipfile
from pathlib import Path

RESOURCE_TABS = {
    'Color Key','Using This Workbook','Excel Formulas','Named Ranges',
    'Data Analytics','Claude for Excel','Welcome',
}

def fix_workbook(src):
    src = Path(src)
    tmp = src.with_suffix('.xlsx.tmp')

    with zipfile.ZipFile(src, 'r') as zin:
        names = zin.namelist()
        buf = {n: zin.read(n) for n in names}

    # Identify which sheetX.xml corresponds to each resource tab
    wbx = buf['xl/workbook.xml'].decode('utf-8')
    rels_xml = buf['xl/_rels/workbook.xml.rels'].decode('utf-8')
    rel_target = {}
    for r in re.finditer(r'<Relationship\b[^>]*?>', rels_xml):
        tag = r.group(0)
        im = re.search(r'Id="([^"]+)"', tag); tm = re.search(r'Target="([^"]+)"', tag)
        if im and tm: rel_target[im.group(1)] = tm.group(1)

    resource_parts = []
    for m in re.finditer(r'<sheet\b[^>]*?>', wbx):
        tag = m.group(0)
        nm = re.search(r'name="([^"]+)"', tag)
        rid = re.search(r'r:id="([^"]+)"', tag)
        if nm and rid and nm.group(1) in RESOURCE_TABS:
            tgt = rel_target.get(rid.group(1), '')
            part = tgt.lstrip('/') if tgt.startswith('/') else ('xl/' + tgt)
            resource_parts.append((nm.group(1), part))

    total_fixed = 0
    for sheet_name, part in resource_parts:
        if part not in buf:
            print(f"  [skip] {sheet_name}: {part} not in archive")
            continue
        sx = buf[part].decode('utf-8')
        fixed = 0

        # Find every <c ...><f>...</f><v>...</v></c> pattern and rewrite as
        # inline string. Match both "<v>...</v>" and empty "<v></v>" forms and
        # the no-<v> case (rare but possible).
        def repl(m):
            nonlocal fixed
            head = m.group(1)  # <c r="..." s="..."
            formula = m.group(2)
            tail = m.group(3) or ''  # rest after </f>
            # Strip any <v>...</v>
            tail = re.sub(r'<v>.*?</v>', '', tail, flags=re.DOTALL)
            fixed += 1
            # inlineStr form: <c r="..." s="..." t="inlineStr"><is><t>=...</t></is></c>
            # Preserve any style or other attributes by keeping head
            # XML-escape the formula body
            esc = (formula.replace('&','&amp;')
                         .replace('<','&lt;').replace('>','&gt;'))
            # Add t="inlineStr" if not present
            head2 = head
            if 't="' in head2:
                head2 = re.sub(r't="[^"]*"', 't="inlineStr"', head2)
            else:
                head2 = head2.rstrip('>') + ' t="inlineStr">'
            return f'{head2}<is><t>={esc}</t></is></c>'

        # Pattern: <c ...><f>FORMULA</f> optional <v>VAL</v> </c>
        pattern = re.compile(
            r'(<c\b[^>]*>)<f>([^<]*)</f>([^<]*?(?:<v>[^<]*</v>)?\s*)</c>',
            re.DOTALL)
        sx_new = pattern.sub(repl, sx)

        if fixed:
            buf[part] = sx_new.encode('utf-8')
            total_fixed += fixed
            print(f"  [{sheet_name}] rewrote {fixed} formula cells as inline-string")

    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for n in names:
            zout.writestr(n, buf[n])
    shutil.move(str(tmp), str(src))
    print(f"  Total fixed in {src.name}: {total_fixed}")

for p in [
    'C:/GitHub/shidler/docs/spreadsheets/International Finance Spreadsheets.xlsx',
    'C:/GitHub/shidler/docs/spreadsheets/Corporate Finance Master Spreadsheets.xlsx',
]:
    print(f"\n=== {Path(p).name} ===")
    fix_workbook(p)
