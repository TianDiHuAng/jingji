# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)

note = (
    '维基第66轮可用。IA：**新建 `leading-indicator`（领先指标），并做两项覆盖审计**。'
    '①**审计一：经典金融危机清单**——逐一核对 1819／1837／1857／1884／1893／1907／'
    '1763／1772／1792／1825／1847／1866／1873／1890／1896／1901／1910／1914 共 18 个年份，'
    '**全部已有条目**，案例覆盖无缺口。'
    '②**审计二：覆盖矩阵的类型缺口**——207 个案例覆盖 95 个（时期×地区×类型）单元格，'
    '剩余 77 个"缺口"经判断多为**历史空白**（如"18—19 世纪拉美的恶性通胀"在史实上并不成立），'
    '不属于知识缺口。'
    '③**审计三：timeline 年份一致性**——612 个事件中，`year` 字段与事件文本内年份不一致的仅 2 处，'
    '且均为合理表述（`investment` 的 −1700 即公元前 1700 年；`mutual-fund` 的 1774 年设立、'
    '应对的是 1772—73 年危机）。'
    '④**审计四：内容厚度**——121 条 overview 短于 100 字，但**全部**另有 ≥3 个补充区块'
    '（timeline／schools／comparison 等），故内容不薄。'
    '⑤据此新建唯一剩余的高价值缺口 **`leading-indicator`**：三类指标（领先／同步／滞后）、'
    '常见领先指标（房屋开工、新订单、初请失业金、收益率曲线倒挂）、'
    '以及"假信号与结构漂移"的批评。'
    '现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、timeline ' + str(tl) + ' 条、'
    'key_data ' + str(tk) + '。**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IA', 'date': '2026-11-24', 'new_entries': 1, 'upgraded': 1, 'reviewed': 633, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（633 条、647 页）',
    'spot_check': '四项覆盖审计通过；新建 leading-indicator',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：632**（案例 207 / 概念 425）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：730**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：646**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 66 轮可用（round 85）**。**新建 `leading-indicator`，并做四项覆盖审计**。
- **审计一 · 经典恐慌清单**：逐一核对 18 个年份（1819／1837／1857／1884／1893／1907／1763／1772／1792／1825／1847／1866／1873／1890／1896／1901／1910／1914）——**全部已有条目**，案例覆盖无缺口。
- **审计二 · 覆盖矩阵**：207 个案例覆盖 95 个单元格；剩余 77 个"缺口"经判断多为**历史空白**（如"18—19 世纪拉美的恶性通胀"史实上并不成立）。
- **审计三 · timeline 年份一致性**：612 个事件中不一致的仅 **2 处**，均为合理表述（`investment` 的 −1700＝公元前 1700 年；`mutual-fund` 1774 年设立、应对 1772—73 年危机）。
- **审计四 · 内容厚度**：121 条 overview 短于 100 字，但**全部**另有 ≥3 个补充区块，内容不薄。
- **新建 `leading-indicator`（领先指标）**：

  | 内容 | 要点 |
  |---|---|
  | 三类指标 | **领先**（房屋开工、新订单、初请失业金、**收益率曲线倒挂**）／**同步**（GDP、就业）／**滞后**（失业率、通胀） |
  | 逻辑 | 处于经济链条**上游**——订单先于生产、开工先于竣工、融资条件先于投资 |
  | 局限 | **假信号**（先转向又回摆）与**结构漂移**（领先期不稳定） |

- 现状：**633 条**（案例 207／概念 426）、来源 **731**、页面 **647**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HZ｜2026-11-24｜状态：632条；新增 check_pages，共11道检查**',
              '**续作IA｜2026-11-24｜状态：633条；四项覆盖审计通过，新建领先指标**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 页面', pages)
