# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts
c = counts(es)

note = (
    '维基第84轮可用。JF：**建立检查器自测，并由此发现 R4b 从未真正生效**。'
    '①动机：round 102 的教训是"以为改了但没生效"。对检查器同样成立——'
    '**新增规则若从未被触发过，就不能确认它有效**。'
    '故构造 5 个必然违规的样本，逐个注入、跑检查、断言报错出现、再复原。'
    '②**首轮自测 4/5 通过，R4b 未被捕获**——排查发现严重 bug：'
    'R4b 的代码写在主循环之外，却沿用了循环变量 `e`，'
    '因此**只检查了最后一个条目**（`e` 的残留值），其余 640 个条目完全没被检查。'
    '修复为 `for _e in entries:` 包裹后，**5/5 全部捕获**。'
    '③**影响评估**：这意味着 round 99 我"修复 72 处无效来源引用并加 R4b"时，'
    'R4b 只对 1 个条目生效。所幸那 72 处是靠脚本修的（不是靠 R4b 发现），'
    '修后的复核也是独立做的，故数据本身无误；**错的只是"今后会被自动拦住"这个承诺**。'
    '④**已固化为 `tools/selftest.py`**，成为常规工具：'
    '今后每次改动检查器，都应先跑它确认规则仍能捕获已知错误。'
    '⑤自测覆盖：R17（来源type非法）、R18（link_ok为空）、'
    'R19（timeline缺sources）、R4b（嵌套来源不存在）、check_pages（文案与导航一致性）。'
    '⑥这是**第 8 次工具缺陷**，且是第一次**由自测主动发现**而非抽查偶然发现**。'
    '现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿 + 自测 5/5**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JF', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 641, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + tools/selftest.py 5/5',
    'spot_check': '自测发现 R4b 因变量作用域 bug 只检查了 1 个条目；已修复',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 84 轮可用（round 103）**。**建立检查器自测，并由此发现 R4b 从未真正生效**。
- **动机**：round 102 的教训是“以为改了但没生效”。对检查器同样成立——**新增规则若从未被触发过，就不能确认它有效**。故构造 **5 个必然违规的样本**，逐个注入、跑检查、断言报错出现、再复原。
- **首轮自测 4/5，R4b 未被捕获**——排查发现严重 bug：

  > R4b 的代码写在主循环之外，却沿用了循环变量 `e`，因此**只检查了最后一个条目**（`e` 的残留值），其余 640 个条目完全没被检查。

  修复为 `for _e in entries:` 包裹后，**5/5 全部捕获**：

  | 自测项 | 结果 |
  |---|---|
  | R17 来源 type 非法 | 通过 |
  | R18 link_ok 为空 | 通过 |
  | R19 timeline 缺 sources | 通过 |
  | **R4b 嵌套来源不存在** | 通过（修复后） |
  | check_pages 文案与导航一致性 | 通过 |

- **影响评估**：round 99 我“修复 72 处无效引用并加 R4b”时，R4b 只对 1 个条目生效。所幸那 72 处是靠脚本修的（不是靠 R4b 发现），修后复核也独立做过，**数据本身无误**；错的只是“今后会被自动拦住”这个承诺。
- **已固化为 `tools/selftest.py`**：今后每次改动检查器，先跑它确认规则仍能捕获已知错误。
- **第 8 次工具缺陷，且是第一次由自测主动发现**（而非抽查偶然发现）。
- 现状：**641 条**、来源 **741**、页面 **655**。**十一道检查全绿 + 自测 5/5**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JE｜2026-11-24｜状态：641条；三个数字工具判据统一（强/弱/未匹配）**',
              '**续作JF｜2026-11-24｜状态：641条；建立检查器自测，发现R4b只检查1个条目**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
