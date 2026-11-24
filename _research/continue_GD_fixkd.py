# -*- coding: utf-8 -*-
"""续作GD：修正 GC 升级时 key_data 的格式（元组→dict）。"""
import json
import glob

FIX = {
 'growth': [
   ('技术进步对美国长期人均收入增长的贡献（索洛估计）', 80, '%', 1957,
    '原文：technological progress has accounted for 80 percent of the long-term rise in U.S. per capita income'),
   ('资本投资增加对同一增长的贡献', 20, '%', 1957,
    '原文：with increased investment in capital explaining only the remaining 20 percent'),
   ('2013年消费支出中用于1869年不存在的商品与服务的比例', 60, '%', 2013,
    '原文：about 60% of consumer spending in 2013 went on goods and services that did not exist in 1869'),
   ('20世纪许多商品实际价格的降幅（以上）', 90, '%', 2000,
    '原文：Over the 20th century, the real price of many goods fell by over 90%'),
 ],
 'recession': [
   ('衰退的深度门槛：实际国民总收入降幅', 1.5, '%', 0,
    '原文：A 1.5% decline in real gross national income'),
   ('衰退的深度门槛：非农就业降幅', 15, '%', 0,
    '原文：a 15% decline in non-agricultural employment'),
   ('衰退的扩散门槛：非农就业下降的行业占比（以上）', 75, '%', 0,
    '原文：A decline in non-agricultural employment in more than 75% of industries'),
   ('被界定为"萧条"的GDP降幅门槛', 10, '%', 0,
    '原文：A severe (GDP down by 10%) or prolonged (three or four years) recession is referred to as an economic depression'),
 ],
 'utility': [
   ('效用概念的现代用法数（至少）', 2, '种含义', 2000,
    '原文：the term has been used with at least two meanings'),
 ],
 'market-failure': [],
}

for eid, rows in FIX.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    sid = next((s for s in d['sources'] if s.startswith('w-en')), d['sources'][0])
    d['key_data'] = [{
        'label': label, 'value': value, 'unit': unit, 'year': year,
        'comparable_price': False,
        'note': note + '；单一来源待核实。', 'sources': [sid],
    } for label, value, unit, year, note in rows]
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%s: key_data 修正为 %d 条 dict' % (eid, len(d['key_data'])))

# 全站扫描：确保所有 key_data 元素都是 dict
bad = []
for f in glob.glob('data/entries/*.json'):
    e = json.load(open(f, encoding='utf-8'))
    for i, k in enumerate(e.get('key_data', [])):
        if not isinstance(k, dict):
            bad.append((e['id'], i, type(k).__name__))
print('\n格式异常条目:', bad if bad else '无')
