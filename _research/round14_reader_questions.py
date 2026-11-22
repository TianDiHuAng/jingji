# -*- coding: utf-8 -*-
"""轮次14 方法4：读者问题清单 — 20个典型问题，检查站内是否有对应条目。"""
import json, glob
entries={}
for f in glob.glob('data/entries/*.json'):
    d=json.load(open(f,encoding='utf-8'))
    entries[d['id']]=d['title']
alltext=' '.join(entries.values())

# (问题, 应命中的关键词组)
QUESTIONS=[
 ('什么是金融危机？', ['金融危机']),
 ('什么是银行挤兑？', ['银行挤兑','擠兌','bank run']),
 ('恶性通胀是怎么发生的？', ['恶性通胀','惡性通貨膨脹']),
 ('1929大萧条是怎么回事？', ['1929','大萧条','大蕭條']),
 ('2008次贷危机的成因？', ['次贷','次貸','2008']),
 ('1997亚洲金融危机？', ['亚洲金融','亞洲金融']),
 ('为什么荷兰会发生郁金香狂热？', ['郁金香','鬱金香']),
 ('南海泡沫是什么？', ['南海泡沫','南海']),
 ('阿根廷为什么反复债务违约？', ['阿根廷']),
 ('欧债危机的根源？', ['欧债','歐債','欧元区','欧元']),
 ('日本泡沫经济怎么崩溃的？', ['日本泡沫','日本资產','日本资产']),
 ('互联网泡沫何时破灭？', ['互联网泡沫','互聯網泡沫','dotcom']),
 ('金本位制是什么？', ['金本位']),
 ('中央银行的作用？', ['中央银行','中央銀行']),
 ('布雷顿森林体系为何崩溃？', ['布雷顿','布雷頓']),
 ('什么是明斯基时刻？', ['明斯基','Minsky']),
 ('1987年黑色星期一？', ['黑色星期一','Black Monday']),
 ('希腊债务危机？', ['希腊','希臘']),
 (' Zimbabwe 恶性通胀？', ['津巴布韦','Zimbabwe']),
 ('石油危机如何影响经济？', ['石油危机','石油危機']),
]

report=['# 读者问题清单覆盖检查（轮次14，方法4）','',
        '设想初学者/学生/爱好者/从业者会问的20个典型问题，检查站内是否有对应条目。','']
covered=0; uncovered=[]
for q, kws in QUESTIONS:
    hit=[t for t in entries.values() if any(k in t for k in kws)]
    if hit:
        covered+=1
        report.append(f'- ✅ {q} → {hit[0][:30]}')
    else:
        uncovered.append(q)
        report.append(f'- ❌ {q} → 无对应条目')
report += ['', f'覆盖：{covered}/{len(QUESTIONS)}','']
if uncovered:
    report.append('## 未覆盖问题（潜在缺口）')
    for q in uncovered: report.append(f'- {q}')
else:
    report.append('## 结论：20个典型问题站内均可找到答案，无缺口。')
open('READER_QUESTIONS.md','w',encoding='utf-8').write('\n'.join(report))
print('\n'.join(report))
