# -*- coding: utf-8 -*-
"""续作AJ：新增3条1930s危机案例(1931欧洲银行危机/1933紧急银行法/1935银行法)。"""
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
 dict(id='european-banking-1931', title='1931年欧洲银行危机', cat='银行',
  unit='U3 20世纪上半', period='20世纪上半', region='欧洲', tier='重要',
  ol='1931年欧洲金融不稳定高峰：奥地利与德国多家大银行倒闭，引发德英相继退出金本位。',
  ov='1931年欧洲银行危机是一次重大的金融不稳定事件，其高峰是奥地利与德国多家大银行倒闭，包括1931年5月11日的 Creditanstalt、1931年7月11日的 Landesbank der Rheinprovinz 与1931年7月13日的 Danat-Bank。该危机触发德国于1931年7月15日退出金本位，英国随后于1931年9月19日退出，并造成广泛的（影响）。具体规模待核实。',
  tl=[
    {'year':1931,'display':'1931年5月11日','event':'奥地利 Creditanstalt 倒闭（据 Wikipedia European banking crisis of 1931）','sources':['w-en-european-banking-1931']},
    {'year':1931,'display':'1931年7月11日','event':'德国 Landesbank der Rheinprovinz 倒闭（同上）','sources':['w-en-european-banking-1931']},
    {'year':1931,'display':'1931年7月13日','event':'德国 Danat-Bank 倒闭（同上）','sources':['w-en-european-banking-1931']},
    {'year':1931,'display':'1931年7月15日','event':'德国退出金本位（同上）','sources':['w-en-european-banking-1931']},
    {'year':1931,'display':'1931年9月19日','event':'英国退出金本位（同上）','sources':['w-en-european-banking-1931']}],
  causal=[('中欧大银行接连倒闭（Creditanstalt、Landesbank、Danat-Bank）→ 存款人与外国债权人恐慌','w-en-european-banking-1931'),
          ('资本外流与黄金储备流失 → 维持金本位不可持续','w-en-european-banking-1931'),
          ('德国(7-15)、英国(9-19)相继退出金本位 → 金本位体系瓦解','w-en-gold-standard')],
  schools=[('金本位约束视角','金本位下央行无法自由提供流动性，危机被迫以退出告终','w-en-gold-standard'),
           ('银行恐慌视角','大银行倒闭通过对手方与存款人恐慌迅速传染','w-en-bank-run')],
  cmp='与1907、2008年危机相比，1931年危机的关键特征是金本位约束下的政策瘫痪；其后果是金本位体系瓦解。具体异同待核实。'),
 dict(id='emergency-banking-act-1933', title='1933年紧急银行法', cat='制度',
  unit='U3 20世纪上半', period='20世纪上半', region='美洲', tier='重要',
  ol='1933年3月美国国会通过的法案，旨在稳定银行体系（配合"银行假日"）。',
  ov='《紧急银行救助法》（E.B.R.A.）是美国国会于1933年3月通过的一项法案，旨在稳定银行体系。该法案与罗斯福宣布的全国"银行假日"配套，通过对银行进行审查与择优复业来恢复公众信心。它是1933年银行业改革的第一步。具体条款待核实。',
  tl=[
    {'year':1933,'display':'1933年3月','event':'美国国会通过《紧急银行救助法》，旨在稳定银行体系（据 Wikipedia Emergency Banking Act of 1933）','sources':['w-en-emergency-banking-act-1933']},
    {'year':1933,'display':'1933年3月后','event':'与"银行假日"配套，审查后择优复业（同上；细节待核实）','sources':['w-en-emergency-banking-act-1933']}],
  causal=[('大萧条中银行大规模倒闭与挤兑 → 体系信心崩溃','w-en-emergency-banking-act-1933'),
          ('宣布银行假日并立法审查银行 → 隔离不稳健机构','w-en-emergency-banking-act-1933'),
          ('择优复业、恢复信心 → 为后续改革铺路','w-en-glass-steagall')],
  schools=[('危机处置视角','假日+审查是快速止血的必要手段','w-en-emergency-banking-act-1933'),
           ('制度视角','为1933年银行法（分业经营）与存款保险奠基','w-en-deposit-insurance')],
  cmp='与2008年TARP、2023年SVB处置同为危机中的紧急干预，但1933年以"停业审查"为主而非注资。具体异同待核实。'),
 dict(id='banking-act-1935', title='1935年银行法', cat='制度',
  unit='U3 20世纪上半', period='20世纪上半', region='美洲', tier='补充',
  ol='1935年8月19日通过、8月23日签署的美国联邦法律，改变美联储体系的结构与权力分配。',
  ov='《1935年银行法》由美国国会于1935年8月19日通过，富兰克林·D·罗斯福总统于8月23日签署成为法律。这是一部改变美联储体系结构与权力分配（的立法），其变革始于1933年银行法。该法包含三个标题。具体内容待核实。',
  tl=[
    {'year':1935,'display':'1935年8月19日','event':'美国国会通过《1935年银行法》（据 Wikipedia Banking Act of 1935）','sources':['w-en-banking-act-1935']},
    {'year':1935,'display':'1935年8月23日','event':'罗斯福总统签署成为法律，改变美联储结构与权力分配（同上）','sources':['w-en-banking-act-1935']}],
  causal=[('1933年银行法启动改革 → 需进一步完善央行架构','w-en-banking-act-1935'),
          ('1935年立法调整美联储结构与权力分配','w-en-banking-act-1935'),
          ('强化中央集权与政策工具 → 影响后续货币政策运作','w-en-federal-reserve')],
  schools=[('制度设计视角','权力集中于理事会提升政策协调','w-en-banking-act-1935'),
           ('制衡视角','储备银行与地区利益的影响力调整（有争论）','w-en-central-bank-independence')],
  cmp='与1913年《联邦储备法》创设美联储、1933年银行法分业经营构成美国央行制度演进三步。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [{'holder': '政策当局', 'view': '应对措施见时间线；效果待核实', 'basis': '需多来源印证',
                             'sources': [sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['tl'][0]['event'][:12], '传导', '后果']),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值与影响程度待核实补充。【续作AJ】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r55_cases.json', encoding='utf-8'))
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
        'id': sp['id'], 'level': 'L2', 'tier': sp['tier'], 'status': 'written',
        'source_count': len(sp['causal']), 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
