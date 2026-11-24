# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
comp = sum(1 for e in es if e.get('comparison'))

note = (
    '维基第54轮可用。GX-GZ：**清理空洞内容**，两件事。'
    '①**删除 2 条占位型 `key_data`**：`south-sea-bubble-1720` 与 `tulip-mania-1637` 的 `value=1` '
    '是"归一化示意口径"而非史料原值——既无信息量，又会让读者误以为该条目有量化数据。'
    '依"宁可页面不显示某区块，也不显示毫无信息量的话"原则移除，两条目不再设"关键数据"区块。'
    '②**删除 57 条模板化 `comparison`**：内容形如"与同为「X」类共享相似传导机制，'
    '差异在于时期／地区／制度环境；具体异同待核实"——对**所有同类条目都成立**，故不含信息量。'
    '（此前 CO 轮已清理过 300 条，这批是后来为把覆盖率凑到 100% 时批量生成的。）'
    '再删 2 条变体（`amsterdam-crisis-1763`／`finnish-banking-1990`）。'
    '③**`comparison` 覆盖率从 100% 降至 90%（' + str(comp) + '/' + str(len(es)) + '）——这是诚实的下降**：'
    '原来的 100% 是靠套话凑成的。清理后保留的 566 条中位长度 168 字符，'
    '虽仍有 110 条短于 60 字符，但多数含实质信息（如"与世行相比 ADB 聚焦亚洲"）。'
    '④九道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GX-GZ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 625, 'fixed': 61,
    'sources_total': len(srcs),
    'check_result': 'PASS; 九道检查全绿',
    'spot_check': '删除 2 条占位 key_data + 59 条无信息量 comparison；覆盖率 100%→90%（诚实下降）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 54 轮可用（round 73）**。**清理空洞内容**——两件事，都是"减法"。
- **① 删除 2 条占位型 `key_data`**

  | 条目 | 问题 |
  |---|---|
  | `south-sea-bubble-1720` | `value=1`，unit 写明"归一化示意口径，**非史料原值**" |
  | `tulip-mania-1637` | 同上 |

  这类值既无信息量，又会让读者误以为该条目有量化数据。依「宁可页面不显示某区块，也不显示毫无信息量的话」原则移除；两条目不再设"关键数据"区块。

- **② 删除 57 条模板化 `comparison`**
  - 内容形如：「与同为「X」类共享相似传导机制，差异在于时期／地区／制度环境；具体异同待核实」
  - 这段话对**所有同类条目都成立**，因此不含任何信息量
  - 此前 CO 轮已清理过 300 条，这批是后来为把覆盖率凑到 100% 时**批量生成**的
  - 再删 2 条变体（`amsterdam-crisis-1763`／`finnish-banking-1990`）

- **③ `comparison` 覆盖率从 100% 降至 90%（566/625）——这是诚实的下降**
  - 原来的 100% 是靠套话凑成的
  - 保留的 566 条中位长度 168 字符；仍有 110 条短于 60 字符，但多数含实质信息（如"与世行相比 ADB 聚焦亚洲"）
- 九道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GV-GW｜2026-11-24｜状态：625条；跨语言对照判定修正(6→32)，首页统计扩展为9项**',
              '**续作GX-GZ｜2026-11-24｜状态：625条；删除59条无信息量内容，comparison 100%→90%（诚实下降）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', comp)
