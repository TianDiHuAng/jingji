# -*- coding: utf-8 -*-
"""阶段4批量生成条目：先全部L1骨架，核心条目附带完整L2结构。
内容纪律：数字一律不编造，用"待核实"；事实引用真实来源 id（来源库已核对）。"""
import json, re, os, glob

# 从 scope.md 解析标题映射（coverage.json 不含 title）
titles = {}
for line in open('scope.md',encoding='utf-8'):
    m = re.match(r'\|\s*([a-z0-9-]+)\s*\|\s*([^|]+?)\s*\|', line)
    if m and m.group(1) not in ('---',):
        titles[m.group(1)] = m.group(2).strip()

scope = json.load(open('coverage.json',encoding='utf-8'))
srcdata = json.load(open('data/sources.json',encoding='utf-8'))
sources = {s['id']:s for s in srcdata['sources'] if s['verified']}
src_list = list(sources.values())

def find_sources(eid, title, name):
    """按条目 id/标题匹配来源：英文维基 slug + 中文维基 + 通用主题来源"""
    out = []
    # 1) 同名英文维基来源（slug 匹配 id）
    s1 = 'w-en-'+re.sub(r'[^a-z0-9]+','-',eid.lower()).strip('-')[:48]
    if s1 in sources: out.append(s1)
    # 2) 从来源库标题里找关键词匹配
    key = re.sub(r'[\(\)（）\d\s—–\-]+','', name)
    key2 = re.sub(r'[\d\s—–\-]+','', name)
    for s in src_list:
        st = re.sub(r'[\s\W_]+','', s['title'].lower())
        kt = re.sub(r'[\s\W_]+','', key.lower())
        if kt and len(kt)>=4 and kt[:8] in st:
            if s['id'] not in out: out.append(s['id'])
        if len(out)>=3: break
    # 3) 通用兜底来源（按危机类型）
    if len(out)<2:
        fallback = {
         '银行':'w-en-bank-run','货币':'w-en-currency-crisis','债务':'w-en-debt-crisis',
         '泡沫':'w-en-speculative-bubble','恶性通胀':'w-en-hyperinflation',
         '其他':'w-en-economic-history','制度':'w-en-central-bank','理论':'w-en-financial-crisis'
        }
        f = fallback.get(e['crisis_type'] if (e:=next((x for x in scope['entries'] if x['id']==eid),{})) else '其他','w-en-financial-crisis')
        if f in sources and f not in out: out.append(f)
    if len(out)<2 and 'w-en-financial-crisis' in sources and 'w-en-financial-crisis' not in out:
        out.append('w-en-financial-crisis')
    return out[:4]

def l1_entry(e, srcs, name):
    time_desc = e['period']
    return {
      'id': e['id'],
      'title': name,
      'level': 'L1',
      'tier': e['tier'],
      'unit': e['unit'],
      'period': e['period'],
      'region': e['region'],
      'crisis_type': e['crisis_type'],
      'one_line': f"{name}：发生于{time_desc}、地区为{e['region']}的{e['crisis_type']}类案例（条目骨架，详细内容待补充）。",
      'overview': f"本条目属于《经济史与金融危机案例库》，分类维度为 时期={e['period']}、地区={e['region']}、危机类型={e['crisis_type']}。完整的时间线、背景、传导机制、数据与争议内容待核实后补充。",
      'timeline': [],
      'causal_chain': [],
      'key_data': [],
      'schools': [],
      'policy_response': [],
      'comparison': '',
      'svg': '',
      'sources': srcs,
      'related': [],
      'needs_verification': True,
      'pending_notes': 'L1骨架：时间线、背景条件、传导机制、关键数据、各方解释、政策应对、SVG图示均待核实补充。'
    }

os.makedirs('data/entries', exist_ok=True)
existing = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob('data/entries/*.json')}
created=0; skipped=0
for e in scope['entries']:
    if e['id'] in existing: skipped+=1; continue  # 保留已写的L2样板
    name = titles.get(e['id'], e['id'])
    srcs = find_sources(e['id'], name, name)
    entry = l1_entry(e, srcs, name)
    with open(f"data/entries/{e['id']}.json",'w',encoding='utf-8') as f:
        json.dump(entry, f, ensure_ascii=False, indent=2)
    created+=1
print('新建L1骨架',created,'跳过已存在',skipped,'总计',len(scope['entries']))
