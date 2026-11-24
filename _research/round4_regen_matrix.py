# -*- coding: utf-8 -*-
"""轮次4：从 coverage.json 重算覆盖矩阵（不覆盖 scope.md）。"""
import json
from collections import defaultdict
cov=json.load(open('coverage.json',encoding='utf-8'))
entries=cov['entries']
periods=['早期—17世纪','18—19世纪','20世纪上半','20世纪下半','21世纪','理论制度']
regions=['欧洲','北美','拉美','亚洲','非洲','中东','大洋洲','全球']
ctypes=['银行','货币','债务','泡沫','恶性通胀','其他','制度','理论']

def norm_period(e): return e['period']
def matrix(rv_fn, cv_fn, R, C, rtitle, ctitle):
    grid=defaultdict(int)
    for e in entries:
        grid[(rv_fn(e),cv_fn(e))]+=1
    out=[f'| {rtitle} \\ {ctitle} | '+' | '.join(C)+' | 合计 |',
         '|'+'---|'*(len(C)+2)]
    for r in R:
        row=[str(grid.get((r,c),0)) for c in C]
        out.append(f'| {r} | '+' | '.join(row)+' | '+str(sum(grid.get((r,c),0) for c in C))+' |')
    out.append('| 合计 |'+''.join(f' {sum(grid.get((r,c),0) for r in R)} |' for c in C)+f' {len(entries)} |')
    return out

m=['# 覆盖矩阵','','每轮报告空白格子。单元格=条目数；0为空白。','','## 矩阵A：时期 × 危机类型','']
m+=matrix(norm_period, lambda e:e['crisis_type'], periods, ctypes,'时期','类型')
m+=['','## 矩阵B：时期 × 地区','']
m+=matrix(norm_period, lambda e:e['region'], periods, regions,'时期','地区')
m+=['','## 矩阵C：地区 × 危机类型','']
m+=matrix(lambda e:e['region'], lambda e:e['crisis_type'], regions, ctypes,'地区','类型')
m+=['','## 空白格子清单（当前）','']
grid=defaultdict(int)
for e in entries: grid[(e['period'],e['crisis_type'])]+=1
for p in periods:
    for t in ctypes:
        if grid.get((p,t),0)==0: m.append(f'- {p} × {t}')
open('COVERAGE_MATRIX.md','w',encoding='utf-8').write('\n'.join(m)+'\n')
print('矩阵重算完成，条目',len(entries))
