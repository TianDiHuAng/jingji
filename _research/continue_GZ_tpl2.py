# -*- coding: utf-8 -*-
"""续作GZ：再删 2 条无信息量的 comparison（"与同类案例共享机制，差异在时期地区"）。"""
import json
import glob

DROP = ['amsterdam-crisis-1763', 'finnish-banking-1990']
for eid in DROP:
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    if d.get('comparison'):
        d.pop('comparison')
        d['pending_notes'] = (d.get('pending_notes', '')
                              + ' 【续作GZ】移除无信息量的 comparison（原文为"与同类案例共享机制，'
                                '差异在时期地区；待核实"，不含具体对照对象与分析）。')
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('删除', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
comp = sum(1 for e in es if e.get('comparison'))
print('comparison 覆盖: %d/%d = %d%%' % (comp, len(es), comp * 100 // len(es)))
