# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)
pct = wk * 100 // len(cases)

note = (
    '维基第36轮可用。FO/FP转向 key_data：从维基全文中用"数字+单位"模式提取候选（22个条目命中），'
    '人工筛选后为14个条目补充17条数据，案例数据覆盖 72%→' + str(pct) + '%（' + str(wk) + '/' + str(len(cases)) + '）、'
    '全站 key_data 357→' + str(tk) + '条。'
    '新增数据：阿姆斯特丹交易所银行营业额50→30百万荷兰盾（1772→1773）、'
    '2013钱荒短期回购利率超25%、丹麦木材市场降99%（1806→1808）、'
    'DeFi抵押品90亿美元与加密资产2.5万亿美元、荷兰200余商船被掠货物值1500万荷兰盾、'
    '第一合众国银行政府认购200万+公众800万美元、安东尼安银币含银量降至2%、'
    '谢尔曼购银法每月购银450万盎司、英镑结算占全球贸易60%以上、'
    '乌拉圭美元化债务超GDP60%且存款流失12%、2011股市两周跌11%、'
    '美国占全球产出份额35%→27%、1884年超1.5亿美元黄金流出、第二合众国银行私人持股80%。'
    '每条均保留英文原文于 note 并标注"单一来源待核实"；value 均为数值以满足 R9。'
    '**筛选原则**：只取与该条目危机直接相关的指标，剔除仅为背景的股份比例等'
    '（如 Creditanstalt 的40%/10%股份认购比例未采用）。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FO-FP', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 14, 'reviewed': 57, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': 'key_data 357→' + str(tk) + '条；案例数据覆盖 72%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FN（人工扫描全部章节后补4条，案例政策69%）',
              '- 当前轮次：续作FO-FP（补17条key_data，案例数据覆盖79%）')
entry = '''- **维基百科第 36 轮可用**。转向 `key_data`：案例数据覆盖 **72% → 79%（162/205）**，全站 `key_data` **357 → 374 条**。
- 方法：从维基全文中用"数字+单位"模式提取候选（22 个条目命中），**人工筛选**后为 14 个条目补充 17 条数据。
- 新增数据举例：

  | 条目 | 数据 |
  |---|---|
  | 1772 英国信用危机 | 阿姆斯特丹交易所银行营业额 **50 → 30 百万荷兰盾**（1772→1773） |
  | 2013 中国钱荒 | 短期回购利率峰值 **超 25%** |
  | 丹麦 1813 | 木材市场降幅 **99%**（1806→1808） |
  | DeFi | 抵押品 **90 亿美元**；加密资产总估值 **2.5 万亿美元** |
  | 第一合众国银行 | 政府认购 **200 万** + 公众 **800 万美元** |
  | 罗马货币 | 安东尼安银币含银量降至 **2%** |
  | 谢尔曼购银法 | 每月须购银 **450 万盎司** |
  | 英镑区 | 以英镑结算占全球贸易 **60% 以上** |
  | 乌拉圭 2002 | 美元化债务 **超 GDP 60%**；存款流失 **12%** |
  | 牙买加协议前 | 美国占全球产出 **35% → 27%** |

- 每条均保留英文原文于 `note` 并标注「单一来源待核实」；`value` 均为数值以满足 R9。
- **筛选原则**：只取与该条目危机**直接相关**的指标，剔除仅为背景的数字（如 Creditanstalt 的 40%/10% 股份认购比例未采用）。
- 三道检查全绿。现状：**625 条**、来源 732、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FN｜2026-11-24｜状态：625条；案例政策69%**',
              '**续作FO-FP｜2026-11-24｜状态：625条；案例数据覆盖79%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | key_data', tk, '| 案例数据覆盖', wk, '/', len(cases), '=', pct, '%')
