# -*- coding: utf-8 -*-
"""续作GF：全面修复 Markdown 粗体未渲染（把长文本字段的 esc 改为 mdesc）。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

REPL = [
    # 概述
    ('sec(\'概述\', f\'<p>{esc(e.get("overview",""))}</p>\'',
     'sec(\'概述\', f\'<p>{mdesc(e.get("overview",""))}</p>\''),
    # 时间线事件
    ('>{esc(t.get("event",""))} ',
     '>{mdesc(t.get("event",""))} '),
    # 各方解释的 view
    ('{esc(s.get("view"))} ',
     '{mdesc(s.get("view"))} '),
    # 待核实说明
    ('<div class="note">{esc(e["pending_notes"])}</div>',
     '<div class="note">{mdesc(e["pending_notes"])}</div>'),
    # key_data 的 label（部分含粗体）与 note
    ('<td>{esc(k.get("label"))}</td>',
     '<td>{mdesc(k.get("label"))}</td>'),
]

cnt = 0
for old, new in REPL:
    if old in s and new not in s:
        s = s.replace(old, new)
        cnt += 1
        print('替换:', old[:52])

# key_data 的 note 在表格下方以文本形式渲染时也要处理
s = s.replace("{esc(d.get('note',''))}", "{mdesc(d.get('note',''))}")
s = s.replace('{esc(k.get("note",""))}', '{mdesc(k.get("note",""))}')

open(p, 'w', encoding='utf-8').write(s)
print('\n共替换 %d 处规则' % cnt)
