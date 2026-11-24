# -*- coding: utf-8 -*-
"""续作GY：删除 57 条模板化 comparison。

这些段落内容形如"与同为「X」类的其他案例共享相似传导机制，差异在于时期、地区与制度环境；
具体异同待核实"——对所有同类条目都成立，因此不含信息量。

依据项目原则：宁可页面不显示某区块，也不显示对所有条目都成立、因而毫无信息量的话。
删除后这些条目的"与其他案例的相似与不同"区块不再显示；
读者仍可通过"相关条目"（自动生成的同类条目）找到对照对象。
"""
import glob
import json
import re

TPL = re.compile(r'^与同为「[^」]*」类(的|案例)')

removed = []
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    c = d.get('comparison') or ''
    if TPL.match(c.strip()) or '与同为「' in c and '共享' in c and '待核实' in c and len(c) < 120:
        removed.append((d['id'], c[:70]))
        d.pop('comparison', None)
        d['pending_notes'] = (d.get('pending_notes', '')
                              + ' 【续作GY】移除模板化 comparison（原文为"与同为某类共享传导机制…"的通用表述，'
                                '对同类条目均成立、不含信息量）；待有具体对照分析时再补。')
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('删除模板化 comparison:', len(removed))
for r in removed[:8]:
    print('  %-26s %s' % (r[0], r[1]))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
have = sum(1 for e in es if e.get('comparison'))
print('\ncomparison 覆盖: %d/%d = %d%%' % (have, len(es), have * 100 // len(es)))
# 检查是否还有可疑模板
rest = [(e['id'], e['comparison'][:70]) for e in es
        if '与同为「' in (e.get('comparison') or '')]
print('仍含"与同为「"的:', len(rest))
for r in rest[:5]:
    print('  ', r)
