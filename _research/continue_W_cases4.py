# -*- coding: utf-8 -*-
"""续作W：新增4条危机案例(挪威1988-92/Danat银行1931/土耳其2001/尼克松冲击1971)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

D = [
 ('norwegian-banking-1988', '挪威银行危机(1988–1992)', '银行', 'U2 18—19世纪', '20世纪下半', '欧洲', '重要',
  '1988—1992年挪威银行危机：挪威战后以来欧洲最大金融危机，源于金融自由化引发的信贷狂潮。',
  '1988—1992年挪威银行危机是挪威自二战结束以来欧洲发生的最大金融危机。危机产生于金融自由化的背景之下：自由化释放了一波危险的信贷操作与随后的放贷狂潮。随着问题暴露，银行体系遭受重大损失并需要政府救助。具体规模数据待核实。',
  [{'year': 1988, 'display': '1980年代中后期', 'event': '挪威金融自由化释放危险的信贷操作与放贷狂潮（据 Wikipedia 1988–1992 Norwegian banking crisis）', 'sources': ['w-en-norwegian-banking-1988']},
   {'year': 1988, 'display': '1988—1992年', 'event': '危机爆发，成为挪威战后以来欧洲最大金融危机（同上）', 'sources': ['w-en-norwegian-banking-1988']}],
  [{'step': '金融自由化 → 信贷管制解除、放贷狂潮', 'sources': ['w-en-norwegian-banking-1988']},
   {'step': '风险贷款累积 → 资产质量恶化', 'sources': ['w-en-norwegian-banking-1988']},
   {'step': '银行损失扩大 → 需政府救助与重组', 'sources': ['w-en-financial-crisis']}],
  [{'holder': '金融自由化视角', 'view': '过快放松管制释放了危险的信贷扩张', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-norwegian-banking-1988']},
   {'holder': '北欧同期视角', 'view': '与芬兰、瑞典同期危机共享自由化-信贷繁荣机制', 'basis': '待核实', 'sources': ['w-en-finnish-banking-1990']}],
  '与同期芬兰银行危机(1991–93)、瑞典银行危机共享"金融自由化→信贷繁荣→资产泡沫→银行危机"机制；挪威案例被视为欧洲战后最大。具体异同待核实。'),
 ('danatbank-1931', 'Danat银行倒闭(1931)', '银行', 'U3 20世纪上半', '20世纪上半', '欧洲', '重要',
  '1931年7月德国Danat银行（达姆施塔特与国民银行）倒闭，是德国1931年银行危机的重要标志事件。',
  'Darmstädter und Nationalbank（简称 Danat-Bank 或 Danatbank）是一家德国大型股份制银行，1922年由 Bank für Handel und Industrie（达姆施塔特，即 Darmstädter Bank）与 Nationalbank für Deutschland 合并成立。该行于1931年7月的倒闭是一个标志性事件，与德国1931年银行危机密切相关。具体影响待核实。',
  [{'year': 1922, 'display': '1922年', 'event': 'Danat-Bank 由两家银行合并成立（据 Wikipedia Danat-Bank）', 'sources': ['w-en-danatbank-1931']},
   {'year': 1931, 'display': '1931年7月', 'event': 'Danat-Bank 倒闭，成为德国银行危机的重要标志事件（同上）', 'sources': ['w-en-danatbank-1931']}],
  [{'step': '德国经济与银行体系承压（外债、政治危机）', 'sources': ['w-en-danatbank-1931']},
   {'step': 'Danat-Bank 于1931年7月倒闭 → 银行挤兑与信心崩塌', 'sources': ['w-en-danatbank-1931']},
   {'step': '德国银行危机加深大萧条，并波及国际', 'sources': ['w-en-great-depression']}],
  [{'holder': '银行恐慌视角', 'view': '大银行倒闭触发挤兑与信心崩塌', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-danatbank-1931']},
   {'holder': '国际资本流动视角', 'view': '外债与资本外逃使德国银行体系脆弱', 'basis': '待核实', 'sources': ['w-en-great-depression']}],
  '与1931年中欧银行危机（奥地利 Creditanstalt）同期，共同标志大萧条在国际金本位体系下的扩散。具体异同待核实。'),
 ('turkey-2001', '土耳其经济危机(2001)', '货币', 'U5 21世纪', '21世纪', '中东', '重要',
  '2001年土耳其经济危机：股市崩盘与里拉崩溃，源于多年积累的政治与经济问题。',
  '2001年土耳其经济危机是一场金融危机，导致股市崩盘与土耳其里拉崩溃，其根源是多年来一直困扰土耳其的政治与经济问题。危机前土耳其经历高通胀与银行体系脆弱，最终在政治冲击下爆发。具体数据与政策应对待核实。',
  [{'year': 2001, 'display': '2001年', 'event': '土耳其爆发经济危机：股市崩盘、里拉崩溃（据 Wikipedia 2001 Turkish economic crisis）', 'sources': ['w-en-turkey-2001']},
   {'year': 2001, 'display': '多年积累', 'event': '危机的根源是长期困扰土耳其的政治与经济问题（同上）', 'sources': ['w-en-turkey-2001']}],
  [{'step': '长期高通胀、财政赤字与银行体系脆弱', 'sources': ['w-en-turkey-2001']},
   {'step': '政治冲击触发信心崩塌 → 资本外流、里拉崩溃', 'sources': ['w-en-turkey-2001']},
   {'step': '股市崩盘、利率飙升 → 深度衰退', 'sources': ['w-en-currency-crisis']}],
  [{'holder': '宏观失衡视角', 'view': '高通胀与财政失衡使经济易受冲击', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-turkey-2001']},
   {'holder': '政治/信心视角', 'view': '政治不确定性触发资本外逃与货币崩溃', 'basis': '待核实', 'sources': ['w-en-capital-flight']}],
  '与1994年墨西哥、1997年亚洲、2018年土耳其危机共享"宏观失衡+政治冲击→货币危机"机制。具体异同待核实。'),
 ('nixon-shock', '尼克松冲击(1971)', '货币', 'U4 20世纪下半', '20世纪下半', '全球', '重要',
  '1971年8月15日尼克松宣布工资物价冻结、进口附加税，并单方面取消美元与黄金的直接可兑换性。',
  '尼克松冲击是1971年8月15日美国总统理查德·尼克松采取的一系列经济措施的效果，包括工资与物价冻结、进口附加税，以及单方面取消美元与黄金的直接国际可兑换性。此举终结了布雷顿森林体系的核心支柱，全球货币体系转向浮动汇率。具体影响待核实。',
  [{'year': 1971, 'display': '1971年8月15日', 'event': '尼克松宣布工资物价冻结、进口附加税及取消美元兑换黄金（据 Wikipedia Nixon shock）', 'sources': ['w-en-nixon-shock']},
   {'year': 1973, 'display': '1971年后', 'event': '布雷顿森林体系固定汇率安排瓦解，主要货币转向浮动', 'sources': ['w-en-bretton-woods-system']}],
  [{'step': '美国国际收支恶化、黄金储备相对美元负债不足', 'sources': ['w-en-triffin-dilemma']},
   {'step': '1971年8月15日单方面停止美元兑换黄金 + 工资物价冻结', 'sources': ['w-en-nixon-shock']},
   {'step': '固定汇率体系瓦解 → 主要货币转向浮动汇率', 'sources': ['w-en-bretton-woods-system']}],
  [{'holder': '体系不可持续视角', 'view': '特里芬难题使美元-黄金平价难以维持', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-triffin-dilemma']},
   {'holder': '政策选择视角', 'view': '美国优先国内目标，主动终止兑换承诺', 'basis': '待核实', 'sources': ['w-en-nixon-shock']}],
  '是布雷顿森林体系终结的标志性事件，与1944年体系建立、1976年牙买加协定构成完整演变链条。具体异同待核实。'),
]

for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in D:
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': tier,
        'unit': unit, 'period': period, 'region': region, 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': tl,
        'causal_chain': causal,
        'key_data': [],
        'schools': schools,
        'policy_response': [{'holder': '政策当局', 'view': '应对措施及效果待核实', 'basis': '需多来源印证', 'sources': [causal[0]['sources'][0]]}],
        'comparison': comp,
        'svg': svg(title, [tl[0]['event'][:12], '传导', '后果']),
        'sources': list(dict.fromkeys([s for c in causal for s in c['sources']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值、政策规模与影响程度待核实补充。【续作W】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r41b.json', encoding='utf-8'))
for eid, v in meta.items():
    sid = 'w-en-' + eid
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + v['slug'], 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia REST API核对(本会话抓取摘要)'
    })
    ex.add(sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in D:
    if eid in have:
        continue
    cov['entries'].append({
        'id': eid, 'level': 'L2', 'tier': tier, 'status': 'written',
        'source_count': 2, 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': unit, 'period': period, 'region': region, 'crisis_type': cat})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
