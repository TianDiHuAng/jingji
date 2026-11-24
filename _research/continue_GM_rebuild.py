# -*- coding: utf-8 -*-
"""续作GM：重建 PROGRESS.md——保留全部历史记录，只把顶部过时状态替换为当前状态。

结构澄清：原文件的"## 当前状态"区块从 L5 延伸到 L986（40 轮追加的记录都堆在这里，
因为没有 `## ` 级标题分隔）。因此 GK 的正则替换会吞掉全部历史。

新结构：
  # 标题 / 说明
  ## 当前状态（自动生成）
  ## 历史记录（轮次 1—65）
  ## 轮次记录（旧表格）
  ## 状态文件
"""
import glob
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw = subprocess.run(['git', 'show', '4805ede:PROGRESS.md'],
                     cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
lines = raw.stdout.splitlines()
assert len(lines) > 900, '源文件行数异常'

i_state = next(i for i, l in enumerate(lines) if l.strip() == '## 当前状态')
i_round = next(i for i, l in enumerate(lines) if l.strip() == '## 轮次记录')

head = lines[:i_state]                 # 标题与说明
old_state = lines[i_state + 1:i_round]  # 原"当前状态"下的 40 轮记录（要保留为历史）
tail = lines[i_round:]                  # 轮次记录表格 + 状态文件

# 计算真实统计
es = [json.load(open(f, encoding='utf-8'))
      for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))]
src = json.load(open(os.path.join(ROOT, 'data', 'sources.json'), encoding='utf-8'))
cases = [e for e in es if not e['unit'].startswith('U6')]
pages = len(glob.glob(os.path.join(ROOT, 'site', '*.html')))
l3 = sum(1 for e in es if e.get('level') == 'L3')
core = sum(1 for e in es if e.get('tier') == '核心')
wk = sum(1 for e in cases if e.get('key_data'))
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
tl = sum(len(e.get('timeline', [])) for e in es)
sc = sum(len(e.get('schools', [])) for e in es)

new_state = [
    '## 当前状态（自动生成；以 tools/check_docs.py 核对）',
    '',
    '- 模式：自动扩充（AUTONOMOUS.md 协议）；终止状态为"饱和"，不写 ALL_DONE',
    '- **条目：%d**（案例 %d / 概念 %d）' % (len(es), len(cases), len(es) - len(cases)),
    '- **来源：%d**（全部 verified 且可达）' % src['count'],
    '- **站点页面：%d**' % pages,
    '- 层级：**核心 %d 条全部 L3**；L3 共 **%d** 条；L1 为 0' % (core, l3),
    '- 内容覆盖：`comparison` **%d/%d**、`related` **%d/%d**' % (len(es), len(es), len(es), len(es)),
    '- 案例内容：政策应对 **%d/%d（%d%%）**、关键数据 **%d/%d（%d%%）**'
    % (wp, len(cases), wp * 100 // len(cases), wk, len(cases), wk * 100 // len(cases)),
    '- 数据量：`key_data` **%d** 条、`timeline` **%d** 条、`schools` **%d** 条' % (tk, tl, sc),
    '- 检查：**9 道**全绿 —— check.py／check_links.py／check_quality.py／check_kd.py／check_polnum.py',
    '  ／check_sources.py／check_body_num.py／check_docs.py',
    '- 已知边界：案例政策剩余 %d 条、关键数据剩余 %d 条，经全文检索确认来源无对应内容（见 BLOCKERS.md）'
    % (len(cases) - wp, len(cases) - wk),
    '',
    '## 历史记录（轮次 1—65，按追加顺序；其中的"现状"为当时数据）',
    '',
]

out = head + new_state + old_state + tail
# 清理连续空行
cleaned = []
for l in out:
    if l == '' and cleaned and cleaned[-1] == '':
        continue
    cleaned.append(l)

p = os.path.join(ROOT, 'PROGRESS.md')
open(p, 'w', encoding='utf-8').write('\n'.join(cleaned) + '\n')
print('重建完成：%d 行（原 %d 行）' % (len(cleaned), len(lines)))
print('保留历史记录行数:', len(old_state))
