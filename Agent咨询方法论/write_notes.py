import json, re, shutil, zipfile
from lxml import etree

PPTX = 'Agent智能体咨询方法论.pptx'
TMP = '_tmp_out.pptx'
notes = json.load(open('notes.json', encoding='utf-8'))

A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
P = 'http://schemas.openxmlformats.org/presentationml/2006/main'

def build_sp(text, sid):
    parts = []
    paras = text.split('\n')
    for para in paras:
        if not para.strip():
            parts.append('<a:p><a:endParaRPr lang="zh-CN"/></a:p>')
        else:
            esc = (para.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
            parts.append('<a:p><a:r><a:rPr lang="zh-CN" sz="1200" dirty="0"/><a:t>%s</a:t></a:r></a:p>' % esc)
    return (
        '<p:sp><p:nvSpPr>'
        '<p:cNvPr id="%d" name="Notes Placeholder %d"/>'
        '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
        '<p:nvPr><p:ph type="body" idx="1"/></p:nvPr>'
        '</p:nvSpPr>'
        '<p:spPr><a:xfrm><a:off x="685800" y="4343400"/><a:ext cx="5486400" cy="4114800"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>'
        '<p:txBody><a:bodyPr wrap="square"><a:normAutofit/></a:bodyPr><a:lstStyle/>%s</p:txBody>'
        '</p:sp>' % (sid, sid, ''.join(parts))
    )

zin = zipfile.ZipFile(PPTX, 'r')
names = zin.namelist()

# 建立 slide -> notesSlide 映射（按 rels 指向）
slide_notes = {}
for rel in [n for n in names if n.startswith('ppt/slides/_rels/')]:
    sn = int(re.search(r'slide(\d+)\.xml\.rels$', rel).group(1))
    xml = zin.read(rel).decode('utf-8')
    m = re.search(r'Target="\.\./notesSlides/(notesSlide\d+\.xml)"', xml)
    if m:
        slide_notes[sn] = 'ppt/notesSlides/' + m.group(1)

zout = zipfile.ZipFile(TMP, 'w', zipfile.ZIP_DEFLATED)
written = 0
for item in zin.infolist():
    data = zin.read(item.filename)
    tgt = None
    m = re.match(r'ppt/notesSlides/(notesSlide\d+)\.xml$', item.filename)
    if m:
        tgt = int(re.search(r'notesSlide(\d+)', m.group(1)).group(1))
    if tgt:
        # 找对应页号
        page = None
        for sn, nn in slide_notes.items():
            if nn == item.filename:
                page = sn
        key = '%02d' % page if page else None
        if key and key in notes:
            xml = data.decode('utf-8')
            # 先移除既有备注占位符，保证可重复执行
            xml = re.sub(r'<p:sp><p:nvSpPr><p:cNvPr id="\d+" name="Notes Placeholder \d+"/>.*?</p:sp>', '', xml, flags=re.S)
            sp = build_sp(notes[key], 2)
            new = xml.replace('</p:spTree>', sp + '</p:spTree>')
            data = new.encode('utf-8')
            written += 1
    zout.writestr(item, data)
zout.close(); zin.close()
shutil.move(TMP, PPTX)
print('notes parts written:', written)

# ---- 校验 ----
z = zipfile.ZipFile(PPTX)
xmls = sorted([n for n in z.namelist() if re.match(r'ppt/notesSlides/notesSlide\d+\.xml$', n)],
              key=lambda s: int(re.search(r'notesSlide(\d+)', s).group(1)))
print('notes parts total:', len(xmls))
bad = 0; total = 0
for i, n in enumerate(xmls, 1):
    txt = ''.join(re.findall(r'<a:t>(.*?)</a:t>', z.read(n).decode('utf-8'), re.S))
    total += len(txt)
    for kw in ['讲述要点', '怎么讲', '时长', '本页', '这页', '要点一', '讲稿', '页码']:
        if kw in txt:
            print('VIOLATION p%d' % i, kw); bad += 1
    if '[' in txt or ']' in txt:
        print('BRACKET p%d' % i); bad += 1
    if len(txt) < 100:
        print('TOO SHORT p%d' % i, len(txt)); bad += 1
    if '\ufffd' in txt:
        print('ENCODING p%d' % i); bad += 1
print('total chars:', total, 'avg:', total // max(1, len(xmls)))
print('violations:', bad)
