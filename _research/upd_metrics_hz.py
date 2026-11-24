# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))

note = (
    '维基第65轮可用。HZ：**新增第 11 个检查工具 `tools/check_pages.py`**——把 round 83 的教训固化成机制。'
    '①工具功能：直接解析**已生成的 HTML**，从中提取首页与验证页上的统计数字，'
    '与按真实数据独立计算出的期望值交叉核对，可发现"改了 A 忘了 B"这类跨页不一致。'
    '核对项包括：条目总数／可用来源／关键数据条数／**独立机构双源印证**／**统计口径对照**，'
    '以及验证页各板块标题中的条数（独立机构印证／统计口径对照／跨语言对照）。'
    '②当前全部一致（632／730／420／2／15）。'
    '③同时把 **CRLF 行尾**这一反复踩两次的坑写入 `DECISIONS.md`：'
    '给出正确做法（`newline=""` 保留行尾 + 行号定位 + 括号配平确定语句边界 + 写回时显式加 `\\r\\n`）。'
    '④**这轮的重点不是新增内容，而是让"经验变成机制"**：'
    'round 82 板块插不进、round 83 语句替换不了，同一原因造成两次失败而无记录；'
    '同理，round 73 手工清理 57 条模板话未固化为检查，导致后来重长。'
    '现状：条目 ' + str(len(es)) + '、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、'
    'key_data ' + str(tk) + '、comparison ' + str(comp) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HZ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 646, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（新增 check_pages）',
    'spot_check': '新增页面一致性检查；CRLF 教训写入 DECISIONS',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 检查：**10 道**全绿 —— check.py／check_links.py／check_quality.py／check_kd.py／check_polnum.py',
              '- 检查：**11 道**全绿 —— check.py／check_links.py／check_quality.py／check_kd.py／check_polnum.py')
s = s.replace('  ／check_sources.py／check_body_num.py／check_docs.py／check_filler.py',
              '  ／check_sources.py／check_body_num.py／check_docs.py／check_filler.py／check_pages.py')
add = '''- **维基百科第 65 轮可用（round 84）**。**新增第 11 个检查工具 `tools/check_pages.py`**——把 round 83 的教训固化成机制。
- **工具功能**：直接解析**已生成的 HTML**，提取首页与验证页上的统计数字，与按真实数据独立计算的期望值交叉核对，专治"**改了 A 忘了 B**"。
  - 核对项：条目总数／可用来源／关键数据条数／**独立机构双源印证**／**统计口径对照**，以及验证页各板块标题条数
  - 当前全部一致（632／730／420／2／15）
- **同时把 CRLF 行尾写入 `DECISIONS.md`**（这个坑踩了两次）：

  | 轮次 | 症状 |
  |---|---|
  | 82 | 插入板块失败 |
  | 83 | 替换语句失败 |

  正确做法：`newline=''` 保留行尾 → 行号定位 → 括号配平确定语句边界 → 写回时显式加 `\\r\\n`。

- **这轮的重点不是新增内容，而是让"经验变成机制"**：
  - round 82/83 同一原因失败两次而无记录
  - round 73 手工清理 57 条模板话未固化为检查 → 后来重长
- **十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HX-HY｜2026-11-24｜状态：632条；首页与验证页口径已统一（2/15）**',
              '**续作HZ｜2026-11-24｜状态：632条；新增 check_pages，共11道检查**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
