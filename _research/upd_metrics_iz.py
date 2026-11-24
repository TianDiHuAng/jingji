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
from kdclass import counts
c = counts(es)

note = (
    '维基第80轮可用。IY-IZ：**发现并修复 72 处"来源 id 指向不存在"的引用，并扩展 R4 覆盖嵌套字段**。'
    '①上一轮把 timeline 的来源覆盖率从 85% 补到 100%，本轮**进一步验证这些 id 是否真实存在**——'
    '发现 **72 处无效引用**（timeline 67／schools 5）。'
    '②**根因**：上一轮批量补来源时，部分 id 是按"条目名/id **猜测**构造"的'
    '（如 `w-en-british-credit-crisis-of-1772`，实际是 `w-en-british-credit-1772`；'
    '又如 `w-en-<eid>` 形式 22 处）——**猜出来的 id 看着像真的**。'
    '③**修复**：模糊匹配（含包含关系）修好 **38 处**，改用条目主来源 **34 处**，'
    '**未能解决 0 处**；修复后**剩余无效引用 0**。'
    '④**扩展 R4 检查**：原 R4 只校验条目的 `sources`，现新增 **R4b** 覆盖'
    '`timeline`／`schools`／`policy_response`／`key_data` 的 `sources`——'
    '嵌套字段里的来源 id 也必须在 `sources.json` 中定义。'
    '⑤**这轮的教训比修好的数字更重要**：'
    '上一轮我为"覆盖率 100%"感到满意，但**覆盖率不等于有效性**——'
    '96 个补齐的来源里有 72 个是猜的 id。'
    '这与 round 73 的"覆盖率靠套话凑"是同一类错误的另一种形态：'
    '**指标达标 ≠ 内容可靠**。'
    '⑥现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、'
    'timeline ' + str(tl) + '、key_data ' + str(tk) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿（check.py 现为 R1–R19 + R4b）**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IY-IZ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 72, 'reviewed': 642, 'fixed': 72,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（新增 R4b 嵌套来源校验）',
    'spot_check': '修复 72 处无效来源引用；R4 扩展到嵌套字段',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 80 轮可用（round 99）**。**发现并修复 72 处"来源 id 指向不存在"的引用，扩展 R4 覆盖嵌套字段**。
- 上一轮把 `timeline` 来源覆盖率从 85% 补到 100%，本轮**进一步验证这些 id 是否真实存在**——发现 **72 处无效引用**（timeline 67／schools 5）。
- **根因**：上一轮批量补来源时，部分 id 是按"条目名/id **猜测**构造"的：

  | 猜的 id | 实际 id |
  |---|---|
  | `w-en-british-credit-crisis-of-1772` | `w-en-british-credit-1772` |
  | `w-en-<eid>`（22 处） | 实际来源 id 拼写不同 |

  **猜出来的 id 看着像真的**——它们符合命名规律，但在 `sources.json` 里不存在。

- **修复**：模糊匹配（含包含关系）修好 **38 处**，改用条目主来源 **34 处**，**未能解决 0 处**；剩余无效引用 **0**。
- **扩展 R4 → R4b**：原 R4 只校验条目的 `sources`，现覆盖 `timeline`／`schools`／`policy_response`／`key_data` 的 `sources`。
- **本轮最重要的教训**：
  > 上一轮我为"覆盖率 100%"感到满意，但**覆盖率不等于有效性**——96 个补齐的来源里有 72 个是猜的 id。
  
  这与 round 73 的"覆盖率靠套话凑"是同一类错误的另一种形态：**指标达标 ≠ 内容可靠**。
- 现状：**641 条**、来源 **741**、页面 **655**。**十一道检查全绿（`check.py` 现含 R1–R19 + R4b）**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IW-IX｜2026-11-24｜状态：641条；timeline来源覆盖85%→100%，加R19**',
              '**续作IY-IZ｜2026-11-24｜状态：641条；修复72处无效来源引用，R4扩展到嵌套字段**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
