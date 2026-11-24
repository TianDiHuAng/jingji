# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))
kd = sum(len(e.get('key_data') or []) for e in es)

note = """维基第149轮可用。PH：交叉引用完整性核查（干净）+ 发现并记录备份风险。
①**交叉引用核查**：comparison 字段引用未知 id = **0**、过短(<20字) = **0**；**全域（overview/comparison/policy/schools/causal/timeline）backtick id 引用未知 = 0**——所有内联 id 均指向真实条目或来源。
②**备份风险（新发现）**：用可达的 GitHub API 查远程 `TianDiHuAng/jingji`（public）——`pushed_at = 2026-11-22`（约 round 25），此后本地 **约 415 提交（round 26–169）未推送**；本会话**无 GitHub token**，无法自动推送。已记入 BACKLOG「备份风险」，建议有凭证时 `git push origin main`。
③十一道检查全绿、自测 34/34。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PH', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 641, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 34/34',
    'spot_check': 'cross-ref 全净（0 未知id）；发现远程仓库停在 2026-11-22、约 415 提交未备份，记 BACKLOG',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 149 轮可用（round 169）**。**交叉引用完整性核查（干净）+ 发现并记录备份风险**。
- **交叉引用核查**：comparison 字段引用未知 id = **0**、过短 = **0**；**全域（overview/comparison/policy/schools/causal/timeline）backtick id 引用未知 = 0**——所有内联 id 均指向真实条目或来源。
- **备份风险（新发现）**：用可达的 GitHub API 查远程 `TianDiHuAng/jingji`（public）——`pushed_at = 2026-11-22`（约 round 25），此后本地 **约 415 提交（round 26–169）未推送**；本会话**无 GitHub token**，无法自动推送。已记入 BACKLOG「备份风险」，建议有凭证时 `git push origin main`。
- 十一道检查全绿、自测 34/34。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
