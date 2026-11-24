# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
tl = sum(len(e.get('timeline', [])) for e in es)
sc = sum(len(e.get('schools', [])) for e in es)
pr = sum(len(e.get('policy_response', [])) for e in es)
from kdclass import counts
c = counts(es)

note = (
    '维基第79轮可用。IW-IX：**把"逐条带来源"从三类内容字段做起，并加入 R19**。'
    '①**审计发现**：`timeline` 642 个事件中 **96 个缺 sources**（集中在近期新建的条目——'
    '我在 event 文本里写了"（据 Wikipedia X）"却未填 sources 字段），涉及 43 个条目；'
    '而 `schools`（1,249 条）与 `policy_response`（151 条）的 sources **已 100% 齐备**。'
    '②**批量补全**：按"据 Wikipedia X"精确匹配补入 **86 个**，按条目主来源补入 **10 个**，'
    '无一条需要留空。**timeline 来源覆盖 642/642 = 100%**。'
    '③**加入 R19 检查**：`timeline`／`schools`／`policy_response` 的**每一条**都必须带 sources，'
    '否则报错。至此三类结构化内容字段的"有据可查"由机器强制保障。'
    '④**方法上的递进**：round 97 穷举的是**枚举字段的取值**（形式一致性），'
    '本轮穷举的是**结构化内容的来源**（内容可追溯性）。'
    '两者合起来覆盖了"每个字段取值合法 + 每条陈述有据"两个层面。'
    '⑤现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    'timeline ' + str(tl) + '／schools ' + str(sc) + '／policy_response ' + str(pr) + ' 条，**全部带来源**；'
    'key_data ' + str(tk) + ' 条。**十一道检查全绿（check.py 现为 R1–R19）**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IW-IX', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 43, 'reviewed': 642, 'fixed': 96,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（check.py 新增 R19）',
    'spot_check': 'timeline 来源覆盖 85%→100%；三类内容字段全部带来源',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 79 轮可用（round 98）**。**把"逐条带来源"落实到三类内容字段，并加入 R19**。
- **审计发现**：

  | 字段 | 条数 | 来源覆盖 |
  |---|---|---|
  | `timeline` | 642 | **546（85%）** ← 96 个缺 |
  | `schools` | 1,249 | 1,249（100%）✓ |
  | `policy_response` | 151 | 151（100%）✓ |

  缺的 96 个集中在**近期新建条目**——我在 event 文本里写了"（据 Wikipedia X）"却**未填 `sources` 字段**。

- **批量补全**：按"据 Wikipedia X"精确匹配补入 **86 个**，按条目主来源补入 **10 个**，无一条留空。**timeline 来源覆盖 642/642 = 100%**。
- **加入 R19 检查**：`timeline`／`schools`／`policy_response` 的**每一条**都必须带 `sources`，否则报错。三类结构化内容字段的"有据可查"由机器强制保障。
- **方法递进**：round 97 穷举的是**枚举字段取值**（形式一致性）；本轮穷举的是**结构化内容的来源**（内容可追溯性）。两者合起来覆盖"取值合法 + 陈述有据"。
- 现状：**641 条**、来源 **741**、页面 **655**。**十一道检查全绿（`check.py` 现为 R1–R19）**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IU-IV｜2026-11-24｜状态：641条；枚举字段普查通过，补34个link_ok并加R18**',
              '**续作IW-IX｜2026-11-24｜状态：641条；timeline来源覆盖85%→100%，加R19**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | timeline %d | schools %d | policy %d' % (tl, sc, pr))
