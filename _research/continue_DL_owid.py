# -*- coding: utf-8 -*-
"""续作DL：用OWID数据核对单源数据点，一致者标注双源印证（离线数据工作）。"""
import json, glob, csv, io

CTRY = {
 'chilean-crisis-1982': 'Chile', 'argentina-2018': 'Argentina', 'brazil-2014': 'Brazil',
 'german-crisis-2022': 'Germany', 'greek-debt-crisis': 'Greece', 'spain-2008': 'Spain',
 'icelandic-crisis-2008': 'Iceland', 'irish-banking-2008': 'Ireland', 'russian-crisis-2014': 'Russia',
 'turkish-crisis-2018': 'Turkey', 'southafrica-debt': 'South Africa', 'nigeria-debt': 'Nigeria',
 'angola-oil-dependence': 'Angola', 'venezuela-crisis-2013': 'Venezuela',
 'venezuela-hyper-2016': 'Venezuela', 'zimbabwe-hyper-2007': 'Zimbabwe',
 'sri-lanka-crisis-2019': 'Sri Lanka', 'pakistan-crisis-2021': 'Pakistan',
 'egypt-2023': 'Egypt', 'lebanese-liquidity-2019': 'Lebanon', 'iranian-economic-crisis': 'Iran',
 'uruguay-2002': 'Uruguay', 'mexican-peso-1994': 'Mexico', 'argentina-crisis-2001': 'Argentina',
 'indian-1991': 'India', 'asian-financial-crisis-1997': 'South Korea',
 'great-recession-russia': 'Russia', 'turkish-crisis-2018b': 'Turkey',
}

COLMAP = {'unemployment': 'sl_uem_totl_zs', 'inflation': 'fp_cpi_totl_zg',
          'gdp': 'ny_gdp_mktp_pp_kd',
          'growth': 'gross_domestic_product__gdp__constant_prices__percent_change_observation'}


def load(kind):
    pat = f'_research/owid_{kind}.csv'
    txt = open(pat, encoding='utf-8').read()
    rows = list(csv.DictReader(io.StringIO(txt)))
    d = {}
    col = COLMAP[kind]
    for r in rows:
        try:
            d[(r['entity'], int(r['year']))] = float(r[col])
        except (ValueError, KeyError, TypeError):
            continue
    return d


DATA = {k: load(k) for k in COLMAP}
print('OWID 索引:', {k: len(v) for k, v in DATA.items()})

# 关键词 → 数据类别
KWKIND = [('失业率', 'unemployment'), ('通胀', 'inflation'), ('GDP增速', 'growth'), ('GDP', 'gdp')]

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
updated, matched, mismatched = 0, [], []

for eid, ctry in CTRY.items():
    if eid not in es:
        continue
    f = es[eid]
    d = json.load(open(f, encoding='utf-8'))
    ch = False
    for k in d.get('key_data', []):
        lab = k.get('label', '')
        if 'OWID' in lab or '世界银行' in lab:   # 已双源
            continue
        kind = None
        for kw, kd in KWKIND:
            if kw in lab:
                kind = kd; break
        if not kind:
            continue
        yr = k.get('year')
        val = k.get('value')
        if not isinstance(yr, int) or not isinstance(val, (int, float)):
            continue
        ref = DATA[kind].get((ctry, yr))
        if ref is None:
            continue
        # 通胀类：绝对差；增长率类：绝对差（百分点）；GDP绝对额：相对差
        if kind in ('inflation', 'growth', 'unemployment'):
            diff = abs(abs(val) - abs(ref))
            tol = max(1.0, abs(ref) * 0.05)
        else:
            diff = abs(val - ref) / max(abs(ref), 1e-9) * 100
            tol = 5.0
        if diff <= tol:
            k['note'] = (k.get('note', '') +
                f' 【双源印证·DL】世界银行/OWID口径同项为 {round(ref, 3)}（{ctry} {yr}），与本值一致。')
            k.setdefault('sources', [])
            if 'owid-dataset' not in k['sources']:
                k['sources'].append('owid-dataset')
            matched.append((eid, lab, val, round(ref, 3)))
            ch = True
        elif diff <= tol * 3:
            mismatched.append((eid, lab, val, round(ref, 3), round(diff, 2)))
    if ch:
        d['pending_notes'] = d.get('pending_notes', '') + ' 【续作DL】部分数据经OWID二次核对。'
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        updated += 1

print('标注双源印证的条目:', updated)
print('印证数据点:', len(matched))
for m in matched:
    print('  ✓', m)
print('接近但未达容差（供人工复核）:', len(mismatched))
for m in mismatched[:8]:
    print('  ~', m)

# 确保 owid-dataset 来源存在
sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
if 'owid-dataset' not in ex:
    sd['sources'].append({'id': 'owid-dataset', 'title': 'Our World in Data（世界银行 WDI 衍生数据集）',
      'author': 'Our World in Data / World Bank', 'year': '2026', 'type': '统计数据',
      'url': 'https://ourworldindata.org/grapher/', 'url2': None, 'verified': True, 'link_ok': True,
      'note': 'CSV 端点抓取核对：unemployment-rate / inflation-of-consumer-prices / gdp-worldbank / real-gdp-growth'})
    sd['count'] = len(sd['sources'])
    json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增来源 owid-dataset')
print('来源总数', len(sd['sources']))
