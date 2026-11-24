# -*- coding: utf-8 -*-
"""续作BB：新增3条罗马货币史条目（填补矩阵「早期—17世纪×恶性通胀」空白）。"""
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
 dict(id='edict-maximum-prices', title='罗马价格敕令(301)', cat='恶性通胀',
  unit='U1 早期—17世纪', period='早期—17世纪', region='欧洲', tier='重要', level='L2',
  ol='301年戴克里先颁布的价格敕令，谴责贪婪并为所有重要商品与服务设定最高价格与工资。',
  ov='价格敕令由戴克里先于301年颁布。该文件谴责贪婪，并为所有重要物品与服务设定最高价格与工资。它是在罗马帝国货币持续贬损、物价飞涨背景下试图以行政手段抑制通胀的著名尝试，但因普遍规避与供给萎缩而难以奏效。具体条款与后果待核实。',
  tl=[
    {'year':301,'display':'301年','event':'戴克里先颁布《价格敕令》，为重要商品与服务设定最高价格与工资（据 Wikipedia Edict on Maximum Prices）','sources':['w-en-edict-maximum-prices']},
  ],
  causal=[('罗马货币长期贬损（成色下降）→ 物价上涨','w-en-debasement'),
          ('301年价格敕令 → 以行政限价抑制通胀','w-en-edict-maximum-prices'),
          ('限价致商品退出市场/规避 → 政策难以为继','w-en-price-controls')],
  schools=[('行政限价视角','限价可短期抑制名义价格，但扭曲供给','w-en-edict-maximum-prices'),
           ('货币视角','通胀根源在货币贬损，须先稳定币值','w-en-debasement')],
  cmp='与后世价格管制（如1971年美国价格管制、战时管制）机制相似：均试图以行政手段压制货币性通胀。具体异同待核实。'),
 dict(id='roman-currency', title='罗马货币体系', cat='货币',
  unit='U1 早期—17世纪', period='早期—17世纪', region='欧洲', tier='补充', level='L2',
  ol='罗马史大部分时期的金币、银币、铜币与黄铜币体系，以数世纪间的通胀性贬损为特征。',
  ov='罗马货币在罗马史的大部分时期由金币、银币、青铜币、山铜（黄铜）与铜币构成。从公元前三世纪共和国时期引入，历经帝国时期，罗马货币在形式、面额与成分上发生许多变化。其一个特征是数世纪间的通胀性贬损与硬币更替。具体演变待核实。',
  tl=[
    {'year':-300,'display':'公元前3世纪','event':'罗马共和国时期引入铸币体系（据 Wikipedia Roman currency）','sources':['w-en-roman-currency']},
    {'year':301,'display':'301年','event':'戴克里先颁布价格敕令以应对物价飞涨（同上及相关条目）','sources':['w-en-edict-maximum-prices']},
  ],
  causal=[('帝国开支与铸币需求 → 降低硬币贵金属含量','w-en-debasement'),
          ('货币成色下降 → 物价上涨与信心流失','w-en-roman-currency'),
          ('通胀性贬损与硬币更替 → 长期货币不稳定','w-en-hyperinflation')],
  schools=[('金属主义视角','成色下降直接削弱货币价值','w-en-debasement'),
           ('财政视角','贬值是弥补财政缺口的手段','w-en-seigniorage')],
  cmp='与近代金本位下的贬值（如1930年代）机制相通：均以减少金属含量或改变平价实现事实贬值。具体异同待核实。'),
 dict(id='debasement', title='货币成色贬损', cat='货币',
  unit='U6 理论与制度', period='理论制度', region='全球', tier='重要', level='L2',
  ol='降低硬币内在价值、却仍按面值流通的做法（尤指商品货币如金银币）。',
  ov='货币成色贬损是降低硬币内在价值的做法，尤其在与商品货币（如金币或银币）相关时使用，同时继续按面值使其流通。若硬币中金、银、铜或镍的含量被减少，该硬币就被称为已贬损。成色贬损是前现代通胀的主要机制，也是一种隐性征税（铸币税）。具体论述待核实。',
  tl=[],
  causal=[('财政压力 → 减少硬币贵金属含量','w-en-debasement'),
          ('名义面值不变但内在价值下降 → 物价上涨','w-en-debasement'),
          ('形成隐性征税（铸币税）与通胀','w-en-seigniorage')],
  schools=[('货币视角','成色贬损直接推高物价','w-en-debasement'),
           ('财政视角','贬损是政府的隐性收入来源','w-en-seigniorage')],
  cmp='与法币超发机制相通，均以扩大名义货币量实现再分配；区别在于成色贬损受金属供给约束。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': sp['level'], 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [{'holder': '政策当局', 'view': '应对措施见时间线；效果待核实', 'basis': '需多来源印证',
                             'sources': [sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基摘要；具体年代与数据待核实。【续作BB】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r73_rome.json', encoding='utf-8'))
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
        'id': sp['id'], 'level': sp['level'], 'tier': sp['tier'], 'status': 'written',
        'source_count': len(sp['causal']), 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
