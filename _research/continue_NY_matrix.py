# -*- coding: utf-8 -*-
"""续作NY：用当前数据重生成 COVERAGE_MATRIX.md（matrix.html 的数据源，之前陈旧为 592 条）。"""
import glob
import json
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

UNITS = ['U1 早期—17世纪', 'U2 18—19世纪', 'U3 20世纪上半', 'U4 20世纪下半', 'U5 21世纪', 'U6 理论与制度']
UNAME = {'U1 早期—17世纪': '早期—17世纪', 'U2 18—19世纪': '18—19世纪',
         'U3 20世纪上半': '20世纪上半', 'U4 20世纪下半': '20世纪下半',
         'U5 21世纪': '21世纪', 'U6 理论与制度': '理论制度'}
TYPES = ['银行', '货币', '债务', '泡沫', '恶性通胀', '其他', '制度', '理论']
REGIONS = ['欧洲', '北美', '拉美', '亚洲', '非洲', '中东', '大洋洲', '全球']

def short_u(u):
    for k in UNITS:
        if u.startswith(k.split(' ')[0]):
            return k
    return u

ct = Counter((short_u(e['unit']), e['crisis_type']) for e in es)
cr = Counter((short_u(e['unit']), e['region']) for e in es)
rc = Counter((e['region'], e['crisis_type']) for e in es)
ut = Counter(short_u(e['unit']) for e in es)
print('总数', len(es), '| 按单元', {UNAME[u]: ut[u] for u in UNITS})

L = []
L.append('# 覆盖矩阵')
L.append('')
L.append('每轮报告空白格子。单元格=条目数；0为空白。')
L.append('')

def matrix(title, rowkey, rowvals, colkey, colvals, cnt, rowname, colname):
    L.append('## ' + title)
    L.append('')
    L.append('| %s \\ %s | %s | 合计 |' % (rowname, colname, ' | '.join(colvals)))
    L.append('|' + '---|' * (len(colvals) + 2))
    colsum = Counter()
    for rv in rowvals:
        cells = []
        rowtot = 0
        for cv in colvals:
            n = cnt.get((rv, cv), 0)
            cells.append(str(n)); rowtot += n; colsum[cv] += n
        L.append('| %s | %s | %d |' % (rv, ' | '.join(cells), rowtot))
    L.append('| 合计 | %s | %d |' % (' | '.join(str(colsum[c]) for c in colvals), sum(colsum.values())))
    L.append('')

matrix('矩阵A：时期 × 危机类型', None, [UNAME[u] for u in UNITS], None, TYPES,
       {(UNAME[u], t): ct.get((u, t), 0) for u in UNITS for t in TYPES}, '时期', '类型')
matrix('矩阵B：时期 × 地区', None, [UNAME[u] for u in UNITS], None, REGIONS,
       {(UNAME[u], r): cr.get((u, r), 0) for u in UNITS for r in REGIONS}, '时期', '地区')
matrix('矩阵C：地区 × 危机类型', None, REGIONS, None, TYPES,
       {(r, t): rc.get((r, t), 0) for r in REGIONS for t in TYPES}, '地区', '类型')

# 空白格子（矩阵A 中为 0 的格子）
L.append('## 空白格子清单（当前）')
L.append('')
blank = ['%s × %s' % (UNAME[u], t) for u in UNITS for t in TYPES if ct.get((u, t), 0) == 0]
for b in blank:
    L.append('- ' + b)
L.append('')

open('COVERAGE_MATRIX.md', 'w', encoding='utf-8').write('\n'.join(L))
print('已生成 COVERAGE_MATRIX.md，空白格子', len(blank), '个')
