# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
srcn = len(srcs)
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
used = set()
for e in es:
    used.update(e.get('sources', []))
unused = [s['id'] for s in srcs if s['id'] not in used]

note = (
    '维基第51轮可用。**本轮发现并修复了第 4 次「工具缺陷导致的错误结论」**。'
    '①检查站内连通性与来源引用：孤儿页面 0 个；但发现 **65 个来源未被任何条目引用**，'
    '其中 **11 个与现有条目明确对应**（来源库里有、条目却没引）。'
    '②最典型的是 `blue-monday-2009`：round 61 我判定"维基无专属条目"并记入 BACKLOG，'
    '**实际专属条目 `Blue_Monday_Crash_2009` 一直存在，且来源库里早已注册** `w-en-blue-monday-crash-2009`。'
    '根因是**维基 URL 大小写敏感**（我测的是 `crash` 小写，正确是 `Crash` 大写）；'
    '更根本的失误是：**判断"来源不存在"之前没有先检索自己的 sources.json**。'
    '③已为 11 个条目补上来源（blue-monday／steel-crisis-1973／copper-panic-1789／'
    'british-credit-1772／israel-bank-1983／us-state-defaults-1840s／great-depression／'
    'crisis-33ce／crisis-1914／venezuela-energy-2010／great-recession-russia）。'
    '④blue-monday 新抓的全文**印证了原有的 -67% 数据**，并补充 RBS 2008 年亏损 **280 亿英镑**、'
    '政府持股 **70%** 两条数据。'
    '⑤教训记入 BLOCKERS（第 4 次），BACKLOG 中该条已标记解决。'
    '剩余未引用来源 ' + str(len(unused)) + ' 个（多为中文维基旧源与书籍，条目改用英文维基后闲置）。'
    '当前：' + str(len(es)) + ' 条、来源 ' + str(srcn) + '、key_data ' + str(tk) + ' 条、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GR', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 12, 'reviewed': 65, 'fixed': 11,
    'sources_total': srcn,
    'check_result': 'PASS; 九道检查全绿',
    'spot_check': '11 处"有源未引"已修复；第4次工具缺陷已记录',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 51 轮可用（round 70）**。**发现并修复第 4 次「工具缺陷导致的错误结论」**。
- 检查结果：孤儿页面 **0** 个；但 **65 个来源未被任何条目引用**，其中 **11 个与现有条目明确对应**（来源库里有、条目没引）。
- **最典型的案例：`blue-monday-2009`**

  | | |
  |---|---|
  | round 61 的判断 | "维基**无专属条目**"，记入 BACKLOG |
  | 实际情况 | 专属条目 `Blue_Monday_Crash_2009` **一直存在**，且来源库**早已注册** `w-en-blue-monday-crash-2009` |
  | 根因 | **维基 URL 大小写敏感**——我测的是 `crash`（小写），正确的是 `Crash`（大写） |
  | 更根本的失误 | **判断"来源不存在"之前，没有先检索自己的 `sources.json`** |

- 已为 11 个条目补上来源：blue-monday／steel-crisis-1973／copper-panic-1789／british-credit-1772／israel-bank-1983／us-state-defaults-1840s／great-depression／crisis-33ce／crisis-1914／venezuela-energy-2010／great-recession-russia。
- `blue-monday` 新抓全文**印证了原有的 −67% 数据**，并补充：RBS 2008 年亏损 **280 亿英镑**、政府持股 **70%**。
- 教训记入 `BLOCKERS.md`（第 4 次工具缺陷）；BACKLOG 中该条已标记**已解决**。
- 剩余未引用来源 **54** 个（多为中文维基旧源与书籍，条目改用英文维基后闲置）。
- 九道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GQ｜2026-11-24｜状态：625条；双向关联对529→1615**',
              '**续作GR｜2026-11-24｜状态：625条；修复11处"有源未引"，第4次工具缺陷已记录**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 未引用来源', len(unused))
