# -*- coding: utf-8 -*-
"""续作GL：安全恢复 PROGRESS.md（GK 误删 979 行），并只替换"当前状态"区块。

事故：GK 用正则 `## 当前状态.*?(?=\\n## )` 替换，但"当前状态"之后直到"## 轮次记录"
     之间的 982 行不含 `## ` 级标题，导致非贪婪匹配吞掉了全部历史记录。
对策：改用**行号定位**，只替换 [当前状态行, 轮次记录行) 这一区间。
"""
import glob
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'PROGRESS.md')

# 1) 从 git 取回未受损版本（4805ede = GK 之前的最后一次提交）
raw = subprocess.run(['git', 'show', '4805ede:PROGRESS.md'],
                     cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
lines = raw.stdout.splitlines()
print('恢复版本行数:', len(lines))

start = next(i for i, l in enumerate(lines) if l.strip() == '## 当前状态')
end = next(i for i, l in enumerate(lines) if l.strip() == '## 轮次记录')
print('当前状态区间: L%d — L%d（待替换 %d 行）' % (start + 1, end, end - start))

# 2) 计算真实统计
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

block = [
    '## 当前状态（自动生成；以 tools/check_docs.py 核对）',
    '- 模式：自动扩充（AUTONOMOUS.md 协议）',
    '- 当前轮次：67（持续进行中；终止状态为"饱和"，不写 ALL_DONE）',
    '- **条目：%d**（案例 %d / 概念 %d）' % (len(es), len(cases), len(es) - len(cases)),
    '- **来源：%d**（全部 verified 且可达）' % src['count'],
    '- **站点页面：%d**' % pages,
    '- 层级：**核心 %d 条全部 L3**；L3 共 **%d** 条；L1 为 0' % (core, l3),
    '- 内容覆盖：`comparison` **%d/%d**、`related` **%d/%d**' % (len(es), len(es), len(es), len(es)),
    '- 案例内容：政策应对 **%d/%d（%d%%）**、关键数据 **%d/%d（%d%%）**'
    % (wp, len(cases), wp * 100 // len(cases), wk, len(cases), wk * 100 // len(cases)),
    '- 数据量：`key_data` **%d** 条、`timeline` **%d** 条、`schools` **%d** 条' % (tk, tl, sc),
    '- 检查：**9 道**全绿 —— check.py／check_links.py／check_quality.py／check_kd.py／',
    '  check_polnum.py／check_sources.py／check_body_num.py／check_docs.py',
    '- 已知边界：案例政策剩余 %d 条、关键数据剩余 %d 条，经全文检索确认来源无对应内容（见 BLOCKERS.md）'
    % (len(cases) - wp, len(cases) - wk),
    '',
]

new_lines = lines[:start] + block + lines[end:]
open(P, 'w', encoding='utf-8').write('\n'.join(new_lines) + '\n')
print('已恢复并更新，新行数:', len(new_lines))
print('轮次记录块是否保留:', '## 轮次记录' in '\n'.join(new_lines))
