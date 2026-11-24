# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)
from kdclass import counts
c = counts(es)

note = (
    '维基第70轮可用。IJ：**用 FSB 一手文献建成首个"维基无专属页"的概念条目**。'
    '①探测 BIS／FSB 页面：BIS 统计术语表（19,470 字符）为**索引页**（列术语名、无详尽定义），'
    'BIS 猜测的几个政策文档 URL 均 404；**FSB《金融机构有效处置制度的关键属性》页面可用**（4,974 字符）。'
    '②据 FSB 一手文献**新建 `bank-resolution`（银行处置）**——此概念在 round 86/87 因'
    '"维基仅有通用页 Bank regulation and supervision"而被判为缺口。'
    'FSB 页面给出的可核实事实：**2011 年 10 月**发布**十二项**关键属性；'
    '定位为覆盖"所有类型、可能在失败时具系统重要性"金融机构的**总括标准(umbrella standard)**；'
    '**2014 年**版本增补附件但十二项正文未改。'
    '条目另含：处置与救助／破产清算／存款保险的三组辨析，'
    '核心工具（bail-in／过桥机构／资产分离／临时接管）与跨境协调难点，'
    '以及两派观点（FSB 的"可信处置"视角 vs 对可行性的质疑——后者已标注为本库归纳、出处待核实）。'
    '③**方法意义**：这验证了 round 88 打开的路径——当某概念无维基专属页时，'
    '可退而使用**国际机构的一手标准文献**作为专属来源，而不必放弃建条目。'
    '④现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、timeline ' + str(tl) + '、key_data ' + str(tk) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IJ', 'date': '2026-11-24', 'new_entries': 1, 'upgraded': 1, 'reviewed': 5, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（636 条、650 页）',
    'spot_check': '首个以国际机构一手文献为专属来源的条目（bank-resolution）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：635**（案例 207 / 概念 428）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：734**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：649**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 70 轮可用（round 89）**。**用 FSB 一手文献建成首个"维基无专属页"的概念条目**。
- **探测结果**：

  | 来源 | 结果 |
  |---|---|
  | BIS 统计术语表 | 可用（19,470 字符），但为**索引页**——列术语名、无详尽定义 |
  | BIS 政策文档（猜的 URL） | 均 **404** |
  | **FSB《处置制度关键属性》** | **可用**（4,974 字符） |

- **新建 `bank-resolution`（银行处置）**——此概念在 round 86/87 因"维基仅有通用页"被判为缺口。FSB 页面给出的可核实事实：

  | 事实 | 内容 |
  |---|---|
  | 发布时间 | **2011 年 10 月** |
  | 内容 | **十二项**关键属性 |
  | 定位 | 覆盖"所有类型、可能在失败时具系统重要性"机构的**总括标准(umbrella standard)** |
  | 修订 | **2014 年**版本增补附件，十二项正文未改 |

- 条目另含：处置 vs 救助 / 破产清算 / 存款保险的三组辨析；核心工具（**bail-in**／**过桥机构**／资产分离／临时接管）与**跨境协调**难点；两派观点（FSB"可信处置"视角 vs 对可行性的质疑——后者标注为本库归纳、出处待核实）。
- **方法意义**：验证了 round 88 打开的路径——当某概念无维基专属页时，可退而使用**国际机构的一手标准文献**作为专属来源，而不必放弃建条目。
- 现状：**636 条**（案例 207／概念 429）、来源 **735**、页面 **650**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IE-II｜2026-11-24｜状态：635条；首次用IMF一手文献，抽取共享判据模块**',
              '**续作IJ｜2026-11-24｜状态：636条；用FSB一手文献建成bank-resolution**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 页面', pages)
