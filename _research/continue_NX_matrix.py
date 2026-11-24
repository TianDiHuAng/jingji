# -*- coding: utf-8 -*-
"""round 141：核验 matrix.html 三张矩阵的合计与单元格是否与实际案例数据一致。"""
import glob, json, re
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]

def unit_short(u):
    return u.split('·')[0].strip() if '·' in u else u
# 实际计数
ct_ur = Counter((e['unit'], e['region']) for e in cases)
ct_uc = Counter((e['unit'], e['crisis_type']) for e in cases)
ct_rc = Counter((e['region'], e['crisis_type']) for e in cases)
print('案例总数:', len(cases))
print('时期合计:', dict(Counter(e['unit'] for e in cases)))
print('类型合计:', dict(Counter(e['crisis_type'] for e in cases)))
print('地区合计:', dict(Counter(e['region'] for e in cases)))

# 解析 matrix.html 所有表格，取"合计"行/列
t = open('site/matrix.html', encoding='utf-8').read()
tables = re.findall(r'<table.*?</table>', t, re.S)
print('\n表格数:', len(tables))
for i, seg in enumerate(tables):
    rows = re.findall(r'<tr>(.*?)</tr>', seg, re.S)
    print('\n--- 表%d 行数=%d ---' % (i, len(rows)))
    for r in rows:
        cells = [re.sub(r'<[^>]+>','',c).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
        print('   ', ' | '.join(cells))
