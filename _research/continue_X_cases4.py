# -*- coding: utf-8 -*-
"""续作X：新增4条(阿根廷2018/西班牙2008-14/LDI策略/Creditanstalt)。"""
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
 ('argentina-2018', '阿根廷货币危机(2018–)', '货币', 'U5 21世纪', '21世纪', '美洲', '重要',
  '2018年至今阿根廷比索持续严重贬值，由高通胀与本币购买力信心下降等因素驱动。',
  '2018年至今的阿根廷货币危机是一场持续中的比索严重贬值过程，由高通胀、本币在当地 perceived 价值急剧下降（购买力不断流失）以及其他国内与国际因素共同造成。阿根廷历史上多次经历货币与债务危机，本轮危机具有持续性。具体汇率与通胀数据待核实。',
  [{'year': 2018, 'display': '2018年起', 'event': '阿根廷比索开始严重贬值，货币危机持续至今（据 Wikipedia 2018–present Argentine monetary crisis）', 'sources': ['w-en-argentina-2018']},
   {'year': 2018, 'display': '持续过程', 'event': '高通胀与本币购买力流失、叠加国内外因素，形成持续贬值压力（同上）', 'sources': ['w-en-argentina-2018']}],
  [{'step': '高通胀与财政/货币失衡 → 比索购买力持续流失', 'sources': ['w-en-argentina-2018']},
   {'step': '本币信心下降 → 居民与企业转向外币、资本外流', 'sources': ['w-en-capital-flight']},
   {'step': '比索持续贬值 → 通胀与债务负担进一步恶化', 'sources': ['w-en-currency-crisis']}],
  [{'holder': '货币/通胀视角', 'view': '高通胀与货币失衡是本币贬值根源', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-argentina-2018']},
   {'holder': '信心/美元化视角', 'view': '对本币信心丧失推动货币替代与资本外流', 'basis': '待核实', 'sources': ['w-en-dollarization']}],
  '与阿根廷2001年危机、2018年土耳其危机共享"高通胀+外债+信心崩塌"机制，但本轮为持续性慢性危机而非单次崩盘。具体异同待核实。'),
 ('spain-2008', '西班牙金融危机(2008–2014)', '银行', 'U5 21世纪', '21世纪', '欧洲', '重要',
  '2008—2014年西班牙金融危机（西班牙大衰退）：2012年因无力救助金融部门而成为欧元区危机的晚参与者。',
  '2008—2014年西班牙金融危机（亦称西班牙大衰退或西班牙大萧条）始于2008年全球金融危机期间。2012年，由于该国无法自行救助其金融部门、不得不寻求外部支持，西班牙成为欧元区危机的较晚参与者。危机的核心是房地产泡沫破裂与银行体系坏账。具体数据待核实。',
  [{'year': 2008, 'display': '2008年', 'event': '西班牙金融危机在经济危机期间开始（据 Wikipedia 2008–2014 Spanish financial crisis）', 'sources': ['w-en-spain-2008']},
   {'year': 2012, 'display': '2012年', 'event': '西班牙无力救助本国金融部门，成为欧元区危机的晚参与者（同上）', 'sources': ['w-en-spain-2008']}],
  [{'step': '房地产泡沫破裂 → 银行不良贷款激增', 'sources': ['w-en-spain-2008']},
   {'step': '银行体系资本不足 → 主权无力独自救助', 'sources': ['w-en-spain-2008']},
   {'step': '2012年寻求外部支持 → 并入欧元区危机进程', 'sources': ['w-en-euro-area-crisis']}],
  [{'holder': '房地产/银行视角', 'view': '地产泡沫与银行坏账是危机核心', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-spain-2008']},
   {'holder': '主权-银行关联视角', 'view': '银行危机与主权风险相互强化（doom loop）', 'basis': '待核实', 'sources': ['w-en-euro-area-crisis']}],
  '与爱尔兰(2008)、希腊(2010)同属欧元区危机案例，但西班牙以房地产泡沫与银行坏账为主、主权压力次之。具体异同待核实。'),
 ('ldi-strategy', '负债驱动投资(LDI)', '理论', 'U6 理论与制度', '理论制度', '全球', '重要',
  '围绕已知负债的规模、时点与风险特征来设计资产组合的资产负债管理方法。',
  '负债驱动投资（LDI）是一种资产负债管理方法：围绕已知义务的规模、时点与风险特征来设计资产组合。它被确定给付型养老金计划（DB）与保险公司用于降低融资波动性，并帮助确保在需要时有可用现金。LDI 常使用衍生品对冲利率与通胀风险，在利率剧变时可能引发保证金压力。具体机制待核实。',
  [{'year': 2022, 'display': '现代实践', 'event': '确定给付型养老金计划与保险公司运用 LDI 降低融资波动（据 Wikipedia Liability-driven investment strategy）', 'sources': ['w-en-ldi-strategy']}],
  [{'step': '养老金/保险有明确负债义务 → 需匹配资产现金流', 'sources': ['w-en-ldi-strategy']},
   {'step': '以长债与衍生品对冲利率/通胀风险 → 降低融资波动', 'sources': ['w-en-ldi-strategy']},
   {'step': '利率剧变时衍生品需追加保证金 → 被迫抛售资产（流动性风险）', 'sources': ['w-en-margin-finance']}],
  [{'holder': '风险管理视角', 'view': 'LDI 可显著降低养老金融资缺口波动', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-ldi-strategy']},
   {'holder': '流动性风险视角', 'view': '杠杆化对冲在利率急升时引发保证金螺旋', 'basis': '待核实', 'sources': ['w-en-margin-finance']}],
  '作为资产负债管理工具，其风险管理收益与流动性风险并存；与2022年英国国债市场动荡相关（具体关联待核实）。具体异同待核实。'),
 ('creditanstalt', '奥地利 Creditanstalt 银行', '银行', 'U3 20世纪上半', '20世纪上半', '欧洲', '补充',
  '1855年在维也纳成立的大型奥地利银行，全称 Österreichische Credit-Anstalt für Handel und Gewerbe。',
  'Creditanstalt（全称原为 k. k. priv. Österreichische Credit-Anstalt für Handel und Gewerbe）是一家大型奥地利银行，于1855年在维也纳成立。它是奥匈帝国时期重要的金融机构。其后续发展与1931年中欧银行危机的关系有待核实补充。具体信息待核实。',
  [{'year': 1855, 'display': '1855年', 'event': 'Creditanstalt 在维也纳成立（据 Wikipedia Creditanstalt）', 'sources': ['w-en-creditanstalt']}],
  [{'step': '1855年于维也纳成立 → 服务贸易与工业融资', 'sources': ['w-en-creditanstalt']},
   {'step': '发展为奥匈帝国重要金融机构', 'sources': ['w-en-creditanstalt']},
   {'step': '后续危机演化（1931年中欧银行危机）待核实', 'sources': ['w-en-great-depression']}],
  [{'holder': '机构史视角', 'view': '大型综合性银行在中欧工业化中承担重要融资职能', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-creditanstalt']}],
  '与Danat银行(1931)同属1931年中欧银行危机的相关机构；具体关联与影响待核实。'),
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
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值、政策规模与影响程度待核实补充。【续作X】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r42_cases.json', encoding='utf-8'))
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
