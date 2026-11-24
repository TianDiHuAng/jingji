# -*- coding: utf-8 -*-
"""续作BL：新增6条区域开发银行与保险监管机构(L2)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：架构示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体成立时间与职能见正文。</text></svg>")
    return ''.join(s)

D = [
 dict(id='iais', title='国际保险监督官协会(IAIS)', cat='制度',
  ol='由200多个辖区保险监管者组成的自愿会员组织，覆盖全球保费约97%。',
  ov='国际保险监督官协会（IAIS）是一个自愿会员组织，成员为来自200多个辖区的保险监管者，这些辖区构成全球保险保费的97%。IAIS 制定保险监管核心原则，并自2008年危机后参与全球系统重要性保险机构（G-SII）的识别与监管。具体职能待核实。',
  tl=[],
  causal=[('保险业跨境经营 → 需监管协调','w-en-iais'),
          ('IAIS 制定核心原则与共同框架','w-en-iais'),
          ('与 BIS、IOSCO 并列构成三大金融标准制定机构','w-en-fsb')],
  schools=[('标准制定视角','以共同原则推动监管趋同','w-en-iais'),
           ('自愿性视角','无强制力，落实依赖成员意愿','w-en-iosco')],
  cmp='与巴塞尔委员会（银行）、IOSCO（证券）并列为三大金融业标准制定机构。具体异同待核实。'),
 dict(id='aiib', title='亚洲基础设施投资银行(AIIB)', cat='制度',
  ol='多边开发银行与国际金融机构，使命为共同改善亚洲经济与社会成果。',
  ov='亚洲基础设施投资银行（AIIB）是一家多边开发银行与国际金融机构，其公开使命是共同改善亚洲的经济与社会成果。它聚焦基础设施投资，被视为现有多边开发体系之外新设的重要机构。具体成立时间与成员待核实。',
  tl=[],
  causal=[('亚洲基础设施融资缺口大 → 新设多边开发银行','w-en-aiib'),
          ('以基础设施投资为主要业务方向','w-en-aiib'),
          ('丰富多边开发金融供给（治理结构存讨论）','w-en-adb')],
  schools=[('补充视角','增加开发融资供给','w-en-aiib'),
           ('治理视角','与既有机构的治理与标准可比性存在讨论','w-en-adb')],
  cmp='与亚开行（ADB，1966年设立）业务领域重叠，但成立背景与治理结构不同。具体异同待核实。'),
 dict(id='adb', title='亚洲开发银行(ADB)', cat='制度',
  ol='旨在促进亚洲社会与经济发展的区域开发银行，总部位于菲律宾马尼拉。',
  ov='亚洲开发银行（ADB）是一家旨在促进亚洲社会与经济发展的区域开发银行。该行总部位于菲律宾马尼拉大都会的曼达卢永市。ADB 为成员国提供贷款、赠款与技术援助，是亚洲主要的多边发展融资来源。具体成立时间与规模待核实。',
  tl=[],
  causal=[('战后亚洲发展融资需求 → 设立区域开发银行','w-en-adb'),
          ('提供贷款与技术援助 → 支持基础设施与减贫','w-en-adb'),
          ('1997亚洲危机中发挥救助与协调作用','w-en-asian-financial-crisis-1997')],
  schools=[('发展融资视角','区域开发银行填补私人资本不足','w-en-adb'),
           ('条件性视角','贷款条件与政策影响力受讨论','w-en-imf')],
  cmp='与世行（全球）相比，ADB 聚焦亚洲；与 AIIB 业务重叠但历史更久。具体异同待核实。'),
 dict(id='ebrd', title='欧洲复兴开发银行(EBRD)', cat='制度',
  ol='1991年成立于巴黎的国际金融机构，多边发展投资银行，以投资为工具推动转型。',
  ov='欧洲复兴开发银行（EBRD）是一家国际金融机构，于1991年在巴黎成立。作为多边发展投资银行，EBRD 以投资为工具来推动（转轨经济体的市场化与私营部门发展）。其成立背景是冷战结束后的中东欧转型。具体职能待核实。',
  tl=[{'year':1991,'display':'1991年','event':'EBRD 在巴黎成立（据 Wikipedia EBRD）','sources':['w-en-ebrd']}],
  causal=[('冷战后中东欧转轨 → 需支持私营部门与市场制度','w-en-ebrd'),
          ('1991年成立 EBRD → 以投资推动转型','w-en-ebrd'),
          ('转轨衰退的经验影响后续危机认知','w-en-transition-economy')],
  schools=[('转型视角','以投资与咨询推动制度转型','w-en-ebrd'),
           ('批判视角','休克疗法式转型的社会代价受争议','w-en-transition-economy')],
  cmp='与世行/ADB 不同，EBRD 带有明确的"转型"使命与政治条件。具体异同待核实。'),
 dict(id='idb', title='美洲开发银行(IDB)', cat='制度',
  ol='总部位于华盛顿特区的国际发展金融机构，是拉美主要发展融资来源之一。',
  ov='美洲开发银行（IDB）是一家国际发展金融机构，总部位于美国华盛顿特区。它是拉丁美洲与加勒比地区主要的发展融资来源之一。IDB 在拉美债务危机后的结构调整与后续发展融资中扮演重要角色。具体成立时间与规模待核实。',
  tl=[],
  causal=[('拉美发展融资需求 → 设立区域开发银行','w-en-idb'),
          ('提供贷款与技术援助','w-en-idb'),
          ('1980年代债务危机中参与调整融资','w-en-latin-american-debt-crisis')],
  schools=[('发展融资视角','区域机构更贴近本地需求','w-en-idb'),
           ('条件性视角','调整贷款的政策条件受讨论','w-en-imf')],
  cmp='与世行相比更聚焦拉美；与 ADB/AfDB 构成区域开发银行体系。具体异同待核实。'),
 dict(id='afdb', title='非洲开发银行(AfDB)', cat='制度',
  ol='多边发展金融机构，自2014年9月起总部设于科特迪瓦阿比让。',
  ov='非洲开发银行集团（AfDB）是一家多边发展金融机构，自2014年9月起总部设于科特迪瓦阿比让。AfDB 向非洲各国政府与私营部门提供融资。它是非洲最主要的多边发展融资渠道之一。具体成立时间与规模待核实。',
  tl=[{'year':2014,'display':'2014年9月','event':'AfDB 总部迁回科特迪瓦阿比让（据 Wikipedia AfDB）','sources':['w-en-afdb']}],
  causal=[('非洲发展融资需求 → 设立区域开发银行','w-en-afdb'),
          ('提供主权与私营部门融资','w-en-afdb'),
          ('债务可持续性与重组议题交织','w-en-debt-crisis-history')],
  schools=[('发展融资视角','补足私人资本与全球机构的不足','w-en-afdb'),
           ('债务视角','融资与债务可持续性需平衡','w-en-debt-sustainability')],
  cmp='与世行/ADB/IDB 并列构成区域开发银行体系；非洲债务问题使其地位关键。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '补充',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：职能与总部等据维基摘要；具体成立时间与规模待核实。【续作BL】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r75_inst2.json', encoding='utf-8'))
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
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': '补充', 'status': 'written',
        'source_count': len(sp['causal']), 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
