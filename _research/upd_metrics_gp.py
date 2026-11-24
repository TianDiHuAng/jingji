# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
tl = sum(len(e.get('timeline', [])) for e in es)
sc = sum(len(e.get('schools', [])) for e in es)
thin = [e['id'] for e in es if not (e.get('timeline') or e.get('schools'))]

note = (
    '维基第49轮可用。GN-GP：**为 13 个薄弱条目补充内容**，缺 timeline/schools 的条目由 **16 降至 4**。'
    '①为 8 个补充：equity-premium（1985 年 Mehra-Prescott 提出谜题，历史溢价 **5%—8%** 高得难以置信，'
    '罕见灾难假说）、fractional-reserve（**1668 年瑞典 Riksbank** 为首家央行、挤兑脆弱性）、'
    'inequality（乐施会 2026 报告：亿万富翁 **3,000 人**、财富 **18.3 万亿**创纪录；'
    '过去 30 年国内不平等显著上升）、investment（可追溯至公元前 1700 年汉谟拉比法典）、'
    'eurodollar（1949 年首例）、modigliani-miller（基准含义）、payment-system（系统重要性）、'
    'proprietary-trading（与做市边界）。'
    '②再为 5 个补充：property-rights（1689 洛克自然权利、2013 年产权保护与发展研究）、'
    'specialization（1714 曼德维尔、1776 斯密扣针工厂）、'
    'mutual-fund（**1774 年 van Ketwich** 设信托、2023 年全球资产 **69 万亿美元**）、'
    'nasdaq（2024 年底 **4,075** 家上市公司）、labour-market（1990—2010 搜寻匹配框架）。'
    '③check_docs.py 新增**文档完整性检查**（行数下限／关键章节／轮次记录条数），防止 round 67 的误删重演。'
    '剩余 4 个（expectations／nasdaq／population／subordination）来源内容较少，属来源边界。'
    '当前：timeline ' + str(tl) + ' 条、schools ' + str(sc) + ' 条、key_data ' + str(tk) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GN-GP', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 13, 'reviewed': 16, 'fixed': 0,
    'sources_total': srcn,
    'check_result': 'PASS; 九道检查全绿（check_docs 新增完整性项）',
    'spot_check': '13 个薄弱条目已补；缺 timeline/schools 由 16 降至 4',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 49 轮可用（round 68）**。**为 13 个薄弱条目补充内容**，缺 timeline/schools 的条目由 **16 降至 4**。
- 补充举例：

  | 条目 | 新增 |
  |---|---|
  | **equity-premium** | 1985 年 Mehra-Prescott 提出谜题；历史溢价 **5%—8%** 高得难以置信；罕见灾难假说 |
  | **fractional-reserve** | **1668 年瑞典 Riksbank** 为世界首家央行；挤兑的内在脆弱点 |
  | **inequality** | 乐施会 2026 报告：亿万富翁 **3,000 人**、财富 **18.3 万亿**创纪录 |
  | **mutual-fund** | **1774 年 van Ketwich** 设信托（为应对 1772—73 危机）；2023 年全球资产 **69 万亿美元** |
  | **property-rights** | 1689 洛克自然权利；2013 年产权保护与发展结果研究 |
  | **specialization** | 1714 曼德维尔 → 1776 斯密扣针工厂 |
  | **nasdaq** | 2024 年底 **4,075** 家上市公司 |
  | investment／eurodollar／labour-market 等 | 公元前 1700 年汉谟拉比法典、1949 年首例欧洲美元、搜寻匹配框架 |

- `check_docs.py` 新增**文档完整性检查**（行数下限／关键章节／轮次记录条数），防止 round 67 的误删重演。
- 剩余 4 个（`expectations`／`nasdaq`／`population`／`subordination`）来源内容较少，属来源边界。
- 九道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GL-GM｜2026-11-24｜状态：625条；已修复误删979行历史记录的事故**',
              '**续作GN-GP｜2026-11-24｜状态：625条；13个薄弱条目已补，缺timeline/schools降至4**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | timeline', tl, '| schools', sc, '| key_data', tk, '| 薄弱', len(thin))
