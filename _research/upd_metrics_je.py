# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts
c = counts(es)

note = (
    '维基第83轮可用。JE：**穷举第三个同类工具 check_body_num，三个数字检查口径已统一**。'
    '①按 round 101 的教训"一处缺陷往往意味着一批"，本轮排查所有基于"字符串匹配"的检查工具。'
    '确认 `check.py`／`check_links`／`check_quality`／`check_sources`／`check_docs`／`check_pages` '
    '都是**确定性校验**（结构、链接、数字比对），不受此缺陷影响；'
    '真正同源的是 **check_kd／check_polnum／check_body_num** 三个"数字溯源"工具，已被文件头注释明示为同一思路。'
    '②**check_body_num 原状况**：只报告"未匹配"（63 个）并给出保守结论"需人工判断"，'
    '比 check_kd 诚实——但它同样不区分"强匹配"与"弱匹配"，'
    '读者无从判断那 2,500 余个"匹配"里有多少是错位的。'
    '③**已加固**：插入与另两个工具一致的两级判据（数字+单位提示词，或与条目自身已核数据结构一致 → 强；'
    '仅数字出现 → 弱；找不到 → 未匹配）。'
    '修复过程中又发现自己的两处疏漏：替换主循环时因缩进/上下文不匹配而静默失败、'
    '以及旧的 `checked, no_full = 0, 0` 行未同步初始化新计数——均按报错定位后修正。'
    '④**结果**：检查正文数字 2,648 个（其中 1,467 个为 4 位年份等被排除），'
    '实际比对 1,181 个 → **强匹配 796（67%）／弱匹配 322（27%）／未匹配 63（5%）**。'
    '⑤**三个数字溯源工具现在口径完全一致**（强／弱／未匹配三级），'
    '且都在工具内声明"**弱匹配不视为通过**"。'
    '这使"检查全绿"的含义变得明确：它只保证**没有完全找不到的数字**，'
    '不保证每个数字都与来源对应——后者需要人工抽查。'
    '⑥现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JE', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 1181, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 三个数字工具判据统一（强/弱/未匹配）',
    'spot_check': 'check_body_num 加固：强匹配 796/1181，弱匹配 322，未匹配 63',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 83 轮可用（round 102）**。**穷举第三个同类工具 `check_body_num`，三个数字检查口径已统一**。
- 按 round 101 的教训“一处缺陷往往意味着一批”，排查所有基于“字符串匹配”的工具：

  | 类别 | 工具 | 是否受影响 |
  |---|---|---|
  | 确定性校验 | `check.py`／`check_links`／`check_quality`／`check_sources`／`check_docs`／`check_pages` | **否**（结构、链接、数字比对） |
  | **数字溯源** | **`check_kd`／`check_polnum`／`check_body_num`** | **是**（三者文件头均注明同一思路） |

- **`check_body_num` 原状况**：只报告“未匹配”（63 个）并给出保守结论“需人工判断”，比 `check_kd` 诚实——但同样不区分强弱，读者无从判断那 2,500 余个“匹配”里有多少错位。
- **已加固**：插入与另两个工具一致的两级判据。过程中又发现自己的两处疏漏——替换主循环时因上下文不匹配而**静默失败**、旧初始化行未同步新计数，均按报错定位修正。
- **结果**：检查正文数字 2,648 个（其中 1,467 个为 4 位年份等被排除），实际比对 1,181 个：

  | 级别 | 条数 | 占比 |
  |---|---|---|
  | ★ 强匹配 | **796** | 67% |
  | ○ 弱匹配 | 322 | 27% |
  | × 未匹配 | 63 | 5% |

- **三个数字溯源工具口径完全一致**，且均声明“**弱匹配不视为通过**”。这使“检查全绿”的含义明确：它只保证**没有完全找不到的数字**，不保证每个数字都与来源对应——后者需人工抽查。
- 十一道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JD｜2026-11-24｜状态：641条；check_polnum同类缺陷，改两级（强匹配413/558）**',
              '**续作JE｜2026-11-24｜状态：641条；三个数字工具判据统一（强/弱/未匹配）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
