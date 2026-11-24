# -*- coding: utf-8 -*-
"""round 140b：审计 deep_svg 元素坐标越界（正确处理单引号属性）。"""
import glob, json, re
import xml.etree.ElementTree as ET

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
bad = []
for e in es:
    s = e.get('deep_svg')
    if not s:
        continue
    m = re.search(r"viewBox\s*=\s*['\"]([\d\.\-\s,]+)['\"]", s)
    if not m:
        bad.append((e['id'], 'no viewBox')); continue
    vb = [float(x) for x in re.split(r'[\s,]+', m.group(1).strip())]
    if len(vb) != 4:
        bad.append((e['id'], 'viewBox bad')); continue
    vx, vy, vw, vh = vb
    try:
        root = ET.fromstring(s)
    except Exception:
        bad.append((e['id'], 'XML错误')); continue
    issues = []
    for el in root.iter():
        tag = el.tag.split('}')[-1]
        for attr in ('x', 'x1', 'x2', 'cx', 'width'):
            if attr in el.attrib:
                try:
                    v = float(el.attrib[attr])
                    if attr != 'width' and (v < vx - 1 or v > vx + vw + 1):
                        issues.append((tag, attr, v))
                except ValueError:
                    pass
        for attr in ('y', 'y1', 'y2', 'cy', 'height'):
            if attr in el.attrib:
                try:
                    v = float(el.attrib[attr])
                    if attr != 'height' and (v < vy - 1 or v > vy + vh + 1):
                        issues.append((tag, attr, v))
                except ValueError:
                    pass
    if issues:
        bad.append((e['id'], 'vb=%s 越界:%s' % (vb, issues[:4])))
print('deep_svg 越界:', len(bad))
for b in bad:
    print('  %-28s %s' % b)
# 打印 viewBox 尺寸分布
sizes = []
for e in es:
    s=e.get('deep_svg')
    if not s: continue
    m=re.search(r"viewBox\s*=\s*['\"]([\d\.\-\s,]+)['\"]", s)
    if m:
        vb=[float(x) for x in re.split(r'[\s,]+', m.group(1).strip())]
        if len(vb)==4: sizes.append((vb[2],vb[3]))
from collections import Counter
print('\nviewBox 尺寸分布:', dict(Counter(sizes)))
