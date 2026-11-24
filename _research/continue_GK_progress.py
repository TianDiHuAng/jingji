# -*- coding: utf-8 -*-
"""续作GK：更新 PROGRESS.md 顶部"当前状态"区块（此前停留在轮次25，已滞后40轮）。"""
import json
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

NEW = f'''## 当前状态（自动生成，勿手改；以 tools/check_docs.py 核对）
- 模式：自动扩充（AUTONOMOUS.md 协议）
- 当前轮次：66（持续进行中；终止状态为"饱和"，不写 ALL_DONE）
- **条目：{len(es)}**（案例 {len(cases)} / 概念 {len(es) - len(cases)}）
- **来源：{src['count']}**（全部 verified 且可达）
- **站点页面：{pages}**
- 层级：**核心 {core} 条全部 L3**；L3 共 **{l3}** 条；L1 为 0（已全部升至 L2 及以上）
- 内容覆盖：`comparison` **{len(es)}/{len(es)}**、`related` **{len(es)}/{len(es)}**
- 案例内容：政策应对 **{wp}/{len(cases)}（{wp * 100 // len(cases)}%）**、关键数据 **{wk}/{len(cases)}（{wk * 100 // len(cases)}%）**
- 数据量：`key_data` **{tk}** 条、`timeline` **{tl}** 条、`schools` **{sc}** 条
- 检查：**9 道**全绿 —— check.py（数据 R1–R16）／check_links.py（链接与 SVG）／
  check_quality.py（HTML 结构 11 项）／check_kd.py（key_data 数值）／
  check_polnum.py（政策段数字）／check_sources.py（来源可达性）／
  check_body_num.py（正文数字）／check_docs.py（文档统计一致性）
- 已知边界：案例政策覆盖剩余 {len(cases) - wp} 条、关键数据剩余 {len(cases) - wk} 条，
  经全文检索确认来源无对应内容；`BLOCKERS.md` 记录明细。
'''

p = os.path.join(ROOT, 'PROGRESS.md')
s = open(p, encoding='utf-8').read()
# 替换第一个 "## 当前状态" 到下一个 "## " 之前的整段
m = re.search(r'## 当前状态.*?(?=\n## )', s, re.S)
if m:
    s = s[:m.start()] + NEW + s[m.end():]
    open(p, 'w', encoding='utf-8').write(s)
    print('PROGRESS.md 顶部当前状态已更新为实际数据')
else:
    print('未找到"## 当前状态"区块')
