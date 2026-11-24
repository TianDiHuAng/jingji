# -*- coding: utf-8 -*-
"""round 155：timeline 年份时序与时期一致性核查。"""
import glob, json
es=[json.load(open(f,encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

UNIT_RANGE = {
 'U1': (-4000, 1699), 'U2': (1700, 1899), 'U3': (1900, 1949),
 'U4': (1950, 1999), 'U5': (2000, 2100),
}
out_of_order=[]; out_of_range=[]
for e in es:
    tl=e.get('timeline') or []
    yrs=[t.get('year') for t in tl if isinstance(t.get('year'),int)]
    # 时序
    if yrs != sorted(yrs):
        out_of_order.append((e['id'], yrs))
    # 时期范围
    pre=e['unit'][:2]
    if pre in UNIT_RANGE:
        lo,hi=UNIT_RANGE[pre]
        bad=[y for y in yrs if y!=0 and not (lo<=y<=hi)]
        if bad:
            out_of_range.append((e['id'], e['unit'], bad, yrs))
print('timeline 非时序条目:', len(out_of_order))
for x in out_of_order[:15]: print('  ', x)
print('\ntimeline 年份超出单元时期范围:', len(out_of_range))
for x in out_of_range[:25]: print('  ', x)
