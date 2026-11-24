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

note = """维基第123轮可用。OB-OC：核查 REPORT.md，**发现它停留在 round 25（135 条/212 来源，且误标 SATURATED），陈旧 117 轮**，已重写并加固 check_docs。
①**发现**：`REPORT.md` 首行仍为"轮次25…SATURATED…135 条/212 来源"。更严重的是，我近多轮更新脚本里的 `REPORT.md` 标题替换因旧标题不匹配而**静默失效**（一直没生效）。
②**根因（check_docs 的盲区）**：`check_docs` 只比对"状态/现状"行中的数字，而旧 REPORT 的状态行**不含数字**（只有 SATURATED），故 `scan()` 返回空 → **静默通过**，陈旧 117 轮无人发现。
③**修复**：将 `REPORT.md` **完整重写**为当前准确状态（641 条/742 来源/655 页、十一道检查、自测、遗留与下一步），并在其中加一行**机器可核对的状态摘要**（"当前：总条目 641、来源 742 条、站点 655 页…"）。同时把"## 一、当前规模"标题改名，避免其被 scan 当作无数字的"状态行"。
④**加固 check_docs**：新增守卫——若 REPORT.md **不含任何可核对的状态数字行**则判为完整性失败（堵住"状态行无数字→静默通过"的洞）；并把 REPORT 的状态数字纳入比对。注入测试（641→999）确认能捕获。
⑤**纳入自测**：`selftest.py` 新增"check_docs REPORT数字"用例，自测 23 → **24 项**，全通过；同步更新 HEALTH_CHECK。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 24/24。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OB-OC', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 2, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 24/24',
    'spot_check': 'REPORT.md 陈旧 117 轮已重写；check_docs 加"缺可核对状态行"守卫；自测 23→24',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 123 轮可用（round 143）**。**核查 REPORT.md，发现它停留在 round 25（135 条／212 来源、误标 SATURATED），陈旧 117 轮**，已重写并加固 check_docs。
- **发现**：`REPORT.md` 首行仍为「轮次25…SATURATED…135 条/212 来源」。更严重的是，我近多轮更新脚本里的 REPORT.md 标题替换因**旧标题不匹配而静默失效**（一直没生效）。
- **根因（check_docs 盲区）**：`check_docs` 只比对「状态/现状」行中的数字，而旧 REPORT 的状态行**不含数字**（只有 SATURATED），故 `scan()` 返回空 → **静默通过**，陈旧 117 轮无人发现。
- **修复**：将 `REPORT.md` **完整重写**为当前准确状态，并加一行**机器可核对的状态摘要**（「当前：总条目 641、来源 742 条、站点 655 页…」）；把「## 一、当前规模」标题改名，避免被 scan 当作无数字状态行。
- **加固 check_docs**：新增守卫——若 REPORT.md **不含任何可核对状态数字行**则判完整性失败（堵住「状态行无数字→静默通过」的洞）。注入测试（641→999）确认能捕获。
- **纳入自测**：`selftest.py` 新增「check_docs REPORT数字」用例，自测 23 → **24 项**；同步更新 HEALTH_CHECK。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 24/24。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
