# -*- coding: utf-8 -*-
"""续作AW：新增7条经济史/危机总论概念(L2)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：概念示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)

D = [
 dict(id='financial-crisis', title='金融危机（总论）', cat='其他',
  ol='各类金融资产突然大幅丧失名义价值的情形；若波及整体经济则成为经济危机。',
  ov='金融危机是各类情形中的一种：某些金融资产突然丧失大部分名义价值。若经济活动的更广泛下降影响到整个经济，则称为经济危机。金融危机可按类型分为银行危机、货币危机、债务危机与资产泡沫破裂等，是多条具体案例的共同上位概念。具体分类待核实。',
  causal=[('资产价格或机构偿付能力恶化 → 名义价值大幅丧失','w-en-financial-crisis'),
          ('恐慌性抛售与信心崩塌 → 冲击扩散','w-en-bank-run'),
          ('波及实体经济活动 → 演变为经济危机','w-en-financial-crisis')],
  schools=[('类型学视角','按银行/货币/债务/泡沫等类型划分危机','w-en-financial-crisis'),
           ('传染视角','危机通过贸易金融渠道跨境扩散','w-en-contagion')],
  srcs=['w-en-financial-crisis','w-en-contagion']),
 dict(id='stock-market-crash', title='股市崩盘', cat='泡沫',
  ol='股市中大部分股票价格突然剧烈下跌、造成大量纸面财富损失的现象。',
  ov='股市崩盘是股票市场中大部分板块股价突然剧烈下跌的现象，造成显著的纸面财富损失。崩盘由恐慌性抛售与潜在经济因素共同驱动。历史上著名的崩盘包括1929、1987与2008年等，其机制与后果差异很大。具体论述待核实。',
  causal=[('估值过高或外部冲击 → 抛售开始','w-en-stock-market-crash'),
          ('恐慌性抛售与保证金追缴 → 价格急跌','w-en-margin-finance'),
          ('财富效应与信心受损 → 影响实体需求','w-en-financial-crisis')],
  schools=[('恐慌视角','崩盘由恐慌性抛售驱动','w-en-stock-market-crash'),
           ('基本面视角','崩盘反映经济基本面恶化','w-en-efficient-market')],
  srcs=['w-en-stock-market-crash','w-en-margin-finance']),
 dict(id='commercial-revolution', title='商业革命', cat='其他',
  ol='欧洲史上以贸易为基础的经济发展时期，始于11世纪、延续至18世纪中叶工业革命。',
  ov='在欧洲史上，商业革命见证了以贸易为基础的欧洲经济的发展：它始于公元11世纪，一直延续到18世纪中叶工业革命到来。商业革命伴随贸易网络扩张、金融工具与商业组织创新，为工业革命奠定基础。具体内容待核实。',
  causal=[('远程贸易扩张 → 贸易网络与商业组织发展','w-en-commercial-revolution'),
          ('金融工具与信用技术创新（汇票、合伙、保险）','w-en-bill-of-exchange'),
          ('资本积累与市场扩展 → 为工业革命奠基','w-en-industrial-revolution')],
  schools=[('贸易驱动视角','贸易扩张带动制度与金融创新','w-en-commercial-revolution'),
           ('制度视角','商业制度演进是长期增长基础','w-en-institutional-economics')],
  srcs=['w-en-commercial-revolution','w-en-industrial-revolution']),
 dict(id='price-revolution', title='价格革命', cat='其他',
  ol='16世纪下半叶欧洲一系列经济事件，与高通胀率特别相关（亦称西班牙价格革命）。',
  ov='价格革命（有时称西班牙价格革命）是发生在16世纪下半叶的一系列经济事件，与当时的高通胀率特别相关。通常与美洲贵金属大量流入、货币供给激增相联系，是早期货币数量论与通胀经验的重要历史案例。具体数据待核实。',
  causal=[('美洲贵金属大量流入 → 货币供给激增','w-en-price-revolution'),
          ('物价总水平长期大幅上涨 → 实际工资与分配变化','w-en-price-revolution'),
          ('为货币数量论提供早期经验证据','w-en-quantity-theory-money')],
  schools=[('货币数量视角','贵金属流入推动物价上涨','w-en-quantity-theory-money'),
           ('人口/实际因素视角','人口增长与需求变化亦起作用','w-en-price-revolution')],
  srcs=['w-en-price-revolution','w-en-quantity-theory-money']),
 dict(id='history-of-money', title='货币史', cat='货币',
  ol='商品与服务交换体系随时间的发展历程。',
  ov='货币史是商品与服务交换体系随时间发展的历程。货币是间接、一般性地实现这些职能的手段，而不同于以物易物的直接交换。货币史涵盖商品货币、铸币、纸币、法币到数字货币的演变。具体阶段待核实。',
  causal=[('以物易物的局限 → 出现一般等价物','w-en-history-of-money'),
          ('商品货币 → 铸币 → 纸币与法币的演进','w-en-commodity-money'),
          ('信用与银行体系发展 → 信用货币','w-en-credit-money')],
  schools=[('商品起源视角','货币源于交换媒介的商品属性','w-en-commodity-money'),
           ('信用起源视角','货币源于债权债务记账关系','w-en-credit-money')],
  srcs=['w-en-history-of-money','w-en-commodity-money']),
 dict(id='history-of-banking', title='银行史', cat='制度',
  ol='银行制度的起源与演变，最早的原型银行可追溯至约公元前2000年的亚述、印度与苏美尔。',
  ov='银行史始于最早的原型银行——即各地的商人，他们向农民与在城市间运送货物的商人提供谷物贷款；时间约为公元前2000年的亚述、印度与苏美尔。此后经历神庙银行、私人银行、汇票与分支网络、中央银行与近代商业银行体系。具体阶段待核实。',
  causal=[('商人提供谷物贷款 → 出现原型银行','w-en-history-of-banking'),
          ('汇票与分支网络 → 跨境银行与信用扩张','w-en-bill-of-exchange'),
          ('中央银行与监管体系形成 → 现代银行制度','w-en-central-bank')],
  schools=[('演进视角','银行由贸易融资需求逐步演化','w-en-history-of-banking'),
           ('制度视角','银行制度与产权、法律环境共同演进','w-en-institutional-economics')],
  srcs=['w-en-history-of-banking','w-en-bill-of-exchange']),
 dict(id='economic-history', title='经济史', cat='理论',
  ol='运用经济学方法工具、或特别关注经济现象的历史研究。',
  ov='经济史是运用经济学的方​​法工具、或特别关注经济现象的历史研究。其研究结合历史方法、统计方法与（经济学）应用。经济史为检验经济理论、理解制度变迁与长期增长提供经验基础。具体方法待核实。',
  causal=[('历史资料与经济理论结合 → 解释长期经济变迁','w-en-economic-history'),
          ('统计与计量方法 → 量化历史证据','w-en-economic-history'),
          ('为政策与理论提供长期视角','w-en-institutional-economics')],
  schools=[('历史学派视角','强调历史特殊性与制度演化','w-en-economic-history'),
           ('计量史学视角','以统计与模型检验历史假说','w-en-great-divergence')],
  srcs=['w-en-economic-history','w-en-institutional-economics']),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [],
        'comparison': '经济史/危机总论概念，与具体案例互补；具体细节待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体年代与数据待核实。【续作AW】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r68_concepts.json', encoding='utf-8'))
NEED = {
 'w-en-commercial-revolution': 'commercial-revolution',
 'w-en-price-revolution': 'price-revolution',
 'w-en-history-of-money': 'history-of-money',
 'w-en-history-of-banking': 'history-of-banking',
 'w-en-economic-history': 'economic-history',
 'w-en-stock-market-crash': 'stock-market-crash',
}
for sid, eid in NEED.items():
    if sid in ex:
        continue
    v = meta.get(eid)
    if not v:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + v['slug'], 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia REST API核对(本会话抓取摘要)'
    })
    ex.add(sid)
    print('新增来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': len(sp['srcs']), 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
