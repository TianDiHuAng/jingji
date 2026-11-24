# -*- coding: utf-8 -*-
"""续作KS：修复扩写时新增的"见 xxx"未接线（check_pages 报出）。"""
import json
import subprocess
import sys

FIX = {
    'mortgage-backed-security': ['tranche', 'spv', 'collateralized-debt-obligation'],
    'resource-curse': ['rent-seeking', 'dutch-disease', 'twin-crises'],
}
for eid, add in FIX.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    rel = d.setdefault('related', [])
    for a in add:
        if a not in rel:
            rel.append(a)
    d['related'] = sorted(set(rel))
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, 'related +', add)

r = subprocess.run([sys.executable, '-X', 'utf8', 'tools/check_pages.py'],
                   capture_output=True, text=True, encoding='utf-8', errors='replace')
print((r.stdout or '').strip().splitlines()[-1])
