# -*- coding: utf-8 -*-
"""续作DM：扩大OWID核对范围——从key_data标签自动提取国家名匹配。"""
import json, glob, csv, io, re

CN2EN = {
 '阿根廷': 'Argentina', '巴西': 'Brazil', '智利': 'Chile', '墨西哥': 'Mexico', '委内瑞拉': 'Venezuela',
 '哥伦比亚': 'Colombia', '秘鲁': 'Peru', '乌拉圭': 'Uruguay', '巴拉圭': 'Paraguay', '玻利维亚': 'Bolivia',
 '厄瓜多尔': 'Ecuador', '牙买加': 'Jamaica', '美国': 'United States', '加拿大': 'Canada',
 '俄罗斯': 'Russia', '土耳其': 'Turkey', '希腊': 'Greece', '西班牙': 'Spain', '爱尔兰': 'Ireland',
 '冰岛': 'Iceland', '葡萄牙': 'Portugal', '意大利': 'Italy', '德国': 'Germany', '法国': 'France',
 '英国': 'United Kingdom', '荷兰': 'Netherlands', '比利时': 'Belgium', '瑞士': 'Switzerland',
 '奥地利': 'Austria', '波兰': 'Poland', '匈牙利': 'Hungary', '捷克': 'Czechia', '罗马尼亚': 'Romania',
 '保加利亚': 'Bulgaria', '乌克兰': 'Ukraine', '拉脱维亚': 'Latvia', '立陶宛': 'Lithuania',
 '爱沙尼亚': 'Estonia', '挪威': 'Norway', '瑞典': 'Sweden', '芬兰': 'Finland', '丹麦': 'Denmark',
 '日本': 'Japan', '韩国': 'South Korea', '中国': 'China', '印度': 'India', '印度尼西亚': 'Indonesia',
 '印尼': 'Indonesia', '泰国': 'Thailand', '马来西亚': 'Malaysia', '菲律宾': 'Philippines',
 '越南': 'Vietnam', '新加坡': 'Singapore', '南非': 'South Africa', '尼日利亚': 'Nigeria',
 '安哥拉': 'Angola', '埃及': 'Egypt', '黎巴嫩': 'Lebanon', '伊朗': 'Iran', '伊拉克': 'Iraq',
 '叙利亚': 'Syria', '也门': 'Yemen', '约旦': 'Jordan', '以色列': 'Israel', '沙特': 'Saudi Arabia',
 '科威特': 'Kuwait', '阿联酋': 'United Arab Emirates', '卡塔尔': 'Qatar', '巴基斯坦': 'Pakistan',
 '斯里兰卡': 'Sri Lanka', '孟加拉': 'Bangladesh', '津巴布韦': 'Zimbabwe', '赞比亚': 'Zambia',
 '加纳': 'Ghana', '肯尼亚': 'Kenya', '喀麦隆': 'Cameroon', '莫桑比克': 'Mozambique',
 '坦桑尼亚': 'Tanzania', '埃塞俄比亚': 'Ethiopia', '摩洛哥': 'Morocco', '突尼斯': 'Tunisia',
 '阿尔及利亚': 'Algeria', '苏丹': 'Sudan', '哈萨克斯坦': 'Kazakhstan', '新西兰': 'New Zealand',
 '澳大利亚': 'Australia', '克罗地亚': 'Croatia', '斯洛文尼亚': 'Slovenia', '斯洛伐克': 'Slovakia',
 '塞浦路斯': 'Cyprus', '马耳他': 'Malta', '波多黎各': 'Puerto Rico', '古巴': 'Cuba',
 '厄立特里亚': 'Eritrea', '白俄罗斯': 'Belarus', '格鲁吉亚': 'Georgia', '亚美尼亚': 'Armenia',
 '蒙古': 'Mongolia', '尼泊尔': 'Nepal', '柬埔寨': 'Cambodia', '缅甸': 'Myanmar', '老挝': 'Laos',
 '沙特阿拉伯': 'Saudi Arabia', '阿拉伯联合酋长国': 'United Arab Emirates',
}

COLMAP = {'unemployment': 'sl_uem_totl_zs', 'inflation': 'fp_cpi_totl_zg',
          'gdp': 'ny_gdp_mktp_pp_kd',
          'growth': 'gross_domestic_product__gdp__constant_prices__percent_change_observation'}


def load(kind):
    txt = open(f'_research/owid_{kind}.csv', encoding='utf-8').read()
    rows = list(csv.DictReader(io.StringIO(txt)))
    col = COLMAP[kind]
    d = {}
    for r in rows:
        try:
            d[(r['entity'], int(r['year']))] = float(r[col])
        except (ValueError, KeyError, TypeError):
            continue
    return d


DATA = {k: load(k) for k in COLMAP}

KWKIND = [('失业率', 'unemployment'), ('通胀', 'inflation'), ('GDP增速', 'growth'),
          ('GDP增长', 'growth'), ('经济增速', 'growth'), ('GDP', 'gdp')]

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
matched, mismatched, noyear = [], [], []

for eid, f in es.items():
    d = json.load(open(f, encoding='utf-8'))
    ch = False
    for k in d.get('key_data', []):
        note = k.get('note') or ''
        if '·DL' in note or 'OWID' in (k.get('label') or '') or '世界银行' in (k.get('label') or ''):
            continue
        lab = k.get('label', '')
        ctry = None
        for cn, en in CN2EN.items():
            if cn in lab:
                ctry = en; break
        if not ctry:
            continue
        kind = None
        for kw, kd in KWKIND:
            if kw in lab:
                kind = kd; break
        if not kind:
            continue
        yr = k.get('year'); val = k.get('value')
        if not isinstance(yr, int) or not isinstance(val, (int, float)):
            continue
        ref = DATA[kind].get((ctry, yr))
        if ref is None:
            noyear.append((eid, lab, ctry, yr)); continue
        if kind in ('inflation', 'growth', 'unemployment'):
            diff = abs(val - ref)
            tol = max(0.5, abs(ref) * 0.03)
            sign_ok = (val * ref) >= 0 or abs(val) < 0.15 or abs(ref) < 0.15
        else:
            diff = abs(val - ref) / max(abs(ref), 1e-9) * 100
            tol = 3.0
            sign_ok = True
        if diff <= tol and sign_ok:
            k['note'] = note + f' 【双源印证·DM】世界银行/OWID同项为 {round(ref,3)}（{ctry} {yr}），方向与量级一致。'
            k.setdefault('sources', [])
            if 'owid-dataset' not in k['sources']:
                k['sources'].append('owid-dataset')
            matched.append((eid, lab, val, round(ref, 3))); ch = True
        elif diff <= tol * 3:
            mismatched.append((eid, lab, val, round(ref, 3), round(diff, 2), sign_ok))
    if ch:
        d['pending_notes'] = d.get('pending_notes', '') + ' 【续作DM】新增OWID二次核对项。'
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('新增印证:', len(matched))
for m in matched: print('  ✓', m)
print('接近但未达容差:', len(mismatched))
for m in mismatched[:10]: print('  ~', m)
print('OWID无该年数据:', len(noyear))
for m in noyear[:6]: print('  -', m)
