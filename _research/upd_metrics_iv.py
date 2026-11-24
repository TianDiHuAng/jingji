# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
from kdclass import counts
c = counts(es)

note = (
    '维基第78轮可用。IU-IV：**穷举全部枚举字段的取值一致性，并补齐一处缺失标记**。'
    '①**枚举字段普查**（9 个字段）：'
    '`level` 2 种（L2 607／L3 34）、`tier` 3 种、`unit` 6 种、`period` 6 种（镜像 unit）、'
    '`region` 8 种、`crisis_type` 8 种、`needs_verification` 全部 True、'
    '`verified` 全部 True、`type` 4 种——**取值均干净，无异名**。'
    '②**唯一异常：`link_ok` 有 34 个 None**（早期批量注册时未填，全为 `w-en-*`）。'
    '批量实测这 34 个 URL 可达性：**34 个全部可达**，已回填为 True。'
    '现 741 个来源的 `link_ok` **全部为 True**。'
    '③**加入 R18 检查**：`link_ok` 不得为空（须为 true/false），防止今后新增来源时漏填。'
    '④这轮延续了 round 96 的方法：**先统一取值，再加检查**；'
    '区别在于本轮是**穷举全部枚举字段**而非只查发现的那个——'
    '结果证明除 `link_ok` 外，其余 8 个字段的取值都已自发一致。'
    '⑤现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '（全部 verified 且 link_ok）、'
    '页面 ' + str(pages) + '、key_data ' + str(tk) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿（check.py 现为 R1–R18）**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IU-IV', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 34, 'reviewed': 741, 'fixed': 34,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（check.py 新增 R18）',
    'spot_check': '34 个 link_ok 空缺已实测回填（全部可达）；枚举字段普查通过',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 78 轮可用（round 97）**。**穷举全部枚举字段的取值一致性，补齐一处缺失标记**。
- **枚举字段普查（9 个）**：

  | 字段 | 取值种数 | 结论 |
  |---|---|---|
  | `level` | 2（L2 607／L3 34） | ✓ |
  | `tier` | 3（核心 34／重要 502／补充 105） | ✓ |
  | `unit` / `period` | 6 / 6（互为镜像） | ✓ |
  | `region` | 8（全球 457…大洋洲 5） | ✓ |
  | `crisis_type` | 8 | ✓ |
  | `needs_verification` / `verified` | 全 True | ✓ |
  | `type` | 4 | ✓ |
  | **`link_ok`** | **None 34 + True 707** | **异常** |

- **唯一异常已修**：34 个 `link_ok` 为 None（早期批量注册时未填，全为 `w-en-*`）。批量实测这 34 个 URL——**全部可达**，已回填 True。现 741 个来源的 `link_ok` **全部为 True**。
- **加入 R18 检查**：`link_ok` 不得为空，防止今后新增来源时漏填。
- 这轮延续 round 96 的方法（**先统一取值、再加检查**），但改为**穷举全部枚举字段**——结果证明除 `link_ok` 外其余 8 个字段取值已自发一致。
- 现状：**641 条**、来源 **741**、页面 **655**。**十一道检查全绿（`check.py` 现为 R1–R18）**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IT｜2026-11-24｜状态：641条；统一来源类型词汇表并加入R17检查**',
              '**续作IU-IV｜2026-11-24｜状态：641条；枚举字段普查通过，补34个link_ok并加R18**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
