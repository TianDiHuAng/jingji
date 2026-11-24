# -*- coding: utf-8 -*-
"""round 140：审计 deep_svg 的元素坐标是否落在 viewBox 内（防裁剪）。"""
import glob, json, re
import xml.etree.ElementTree as ET

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
bad = []
for e in es:
    s = e.get('deep_svg')
    if not s:
        continue
    m = re.search(r'viewBox="([\d\.\-\s,]+)"', s)
    if not m:
        bad.append((e['id'], 'no viewBox')); continue
    vb = [float(x) for x in re.split(r'[\s,]+', m.group(1).strip())]
    if len(vb) != 4:
        bad.append((e['id'], 'viewBox格式: ' + m.group(1))); continue
    vx, vy, vw, vh = vb
    try:
        root = ET.fromstring(s)
    except Exception as ex:
        bad.append((e['id'], 'XML错误')); continue
    issues = []
    for el in root.iter():
        tag = el.tag.split('}')[-1]
        # rect: x,y,width,height ; text: x,y ; line: x1,y1,x2,y2
        for attr in ('x', 'x1', 'x2', 'cx'):
            if attr in el.attrib:
                try:
                    v = float(el.attrib[attr])
                    if v < vx - 1 or v > vx + vw + 1:
                        issues.append((tag, attr, v))
                except ValueError:
                    pass
        for attr in ('y', 'y1', 'y2', 'cy'):
            if attr in el.attrib:
                try:
                    v = float(el.attrib[attr])
                    if v < vy - 1 or v > vy + vh + 1:
                        issues.append((tag, attr, v))
                except ValueError:
                    pass
    if issues:
        bad.append((e['id'], 'viewBox=%s 越界: %s' % (vb, issues[:4])))
print('deep_svg 越界/异常:', len(bad))
for b in bad:
    print('  %-28s %s' % b)
