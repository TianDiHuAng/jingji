# 按 YPFS 式干预工具分类 policy_response（仅关键词匹配 view 文本，不改条目）
import json,glob,collections
T=[('流动性支持',['最后贷款人','流动性','贴现窗口','紧急贷款','再贷款','注入资金','提供贷款','贷款便利']),
('资本注入与国有化',['注资','资本注入','国有化','收归国有','入股','接管']),
('担保与存款保险',['担保','存款保险','兜底']),
('救助计划与资产处置',['救助','纾困','坏账','不良资产','资产管理公司','TARP','收购']),
('银行处置与关闭',['关闭','清算','破产','重组银行','合并','并购']),
('货币政策',['降息','加息','利率','量化宽松','购债','印钞','货币供应']),
('汇率与资本管制',['贬值','汇率','钉住','资本管制','外汇管制','固定汇率','浮动']),
('财政措施',['财政','减税','支出','紧缩','预算','刺激']),
('债务重组与国际援助',['债务重组','违约','IMF','国际货币基金','援助贷款','布雷迪','减免']),
('币制改革与金本位',['货币更替','重定值','新货币','金本位','停兑','暂停兑换','兑换','美元化','取代']),
('价格与市场管制',['价格','管制','限价','熔断','暂停交易','收市','冻结','限电','限制']),
('产量与贸易措施',['产量','禁运','关税','进口','出口']),
('立法与监管改革',['法案','立法','监管','法律','改革','设立'])]
rows=[];c=collections.Counter()
for f in sorted(glob.glob('data/entries/*.json')):
    e=json.load(open(f,encoding='utf-8'))
    for p in e.get('policy_response') or []:
        v=p.get('view','');tags=[n for n,ks in T if any(k in v for k in ks)]
        rows.append(dict(id=e['id'],title=e['title'],view=v,tags=tags,sources=p.get('sources',[])))
        for t in tags or ['未归类']: c[t]+=1
json.dump(rows,open('data/policy_tools.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(rows),c.most_common())
for r in rows:
    if not r['tags']: print('-',r['id'],r['view'][:70])
