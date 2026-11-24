# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)
from kdclass import counts
c = counts(es)
# 机构来源统计
orgs = [s['id'] for s in srcs if s['id'].startswith('org-')]

note = (
    '维基第71轮可用。IK-IL：**继续用国际机构官方页补内容，两处实质补充**。'
    '①**`sifi`（系统重要性金融机构）**：原概述写"具体认定标准待核实"，'
    '据 FSB 官方页补上认定机制——FSB 与 BCBS 及各国当局协商、'
    '**自 2011 年起**识别全球系统重要性银行(G-SIBs)；名单划分**"分档"(buckets)**，'
    '各档对应不同水平的**附加损失吸收能力**要求；名单**每年 11 月更新**。'
    '新增来源 `org-fsb-gsib` 与 timeline 2 条。'
    '②**`shadow-banking`（影子银行体系）**原缺 timeline，'
    '据 FSB 官方页补监管政策沿革——**2013 年** FSB 与标准制定机构制定政策建议、获 G20 认可，'
    '聚焦**五个领域**（银行与 NBFI 的溢出／货币市场基金挤兑脆弱性／证券化透明度与激励／'
    '回购与证券借贷的顺周期性／其他非银实体的系统性风险）；'
    '**2020 年 3 月** COVID-19 使关键融资市场出现剧烈压力，凸显加强 NBFI 韧性的必要。'
    '③**一处否定性发现**：BIS 的"杠杆率"相关页面（23,604 字符）实为**各法域实施评估时间表**'
    '（RCAP LEV），而非杠杆率的定义或规则说明——**实施页 ≠ 定义页**，故未用作 `leverage-ratio` 的来源。'
    '英国央行 ring-fencing 页 404、EBA 杠杆率页 404。'
    '④现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '（其中 org-* 机构来源 ' + str(len(orgs)) + ' 个）、'
    '页面 ' + str(pages) + '、timeline ' + str(tl) + '、key_data ' + str(tk) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IK-IL', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 4, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿',
    'spot_check': 'sifi 补 FSB 认定机制；shadow-banking 补监管沿革',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **来源：735**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
add = '''- **维基百科第 71 轮可用（round 90）**。**继续用国际机构官方页补内容，两处实质补充**。
- **① `sifi`（系统重要性金融机构）**：原概述写"具体认定标准待核实"，据 FSB 官方页补上机制：

  | 项 | 内容 |
  |---|---|
  | 识别起始 | FSB 与 BCBS 及各国当局协商，**自 2011 年起**识别 G-SIBs |
  | 分档 | 名单划分 **"buckets"（分档）**，各档对应不同水平的**附加损失吸收能力**要求 |
  | 更新频率 | 名单**每年 11 月更新** |

- **② `shadow-banking`（影子银行体系）**原缺 timeline，据 FSB 官方页补监管沿革：
  - **2013 年** FSB 与标准制定机构制定政策建议、获 G20 认可，聚焦**五个领域**：银行与 NBFI 的溢出／**货币市场基金挤兑脆弱性**／证券化透明度与激励／**回购与证券借贷的顺周期性**／其他非银实体的系统性风险
  - **2020 年 3 月**：COVID-19 使关键融资市场出现剧烈压力，凸显加强 NBFI 韧性的必要
- **③ 一处否定性发现**：BIS 的"杠杆率"相关页面（23,604 字符）实为**各法域实施评估时间表**（RCAP LEV），而非定义或规则说明——**实施页 ≠ 定义页**，故未用作 `leverage-ratio` 的来源。英国央行 ring-fencing 页、EBA 杠杆率页均 404。
- 现状：**636 条**、来源 **737**（其中 `org-*` 机构来源 **18** 个）、页面 **650**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IJ｜2026-11-24｜状态：636条；用FSB一手文献建成bank-resolution**',
              '**续作IK-IL｜2026-11-24｜状态：636条；sifi补认定机制，shadow-banking补监管沿革**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 来源', len(srcs), '| org来源', len(orgs))
