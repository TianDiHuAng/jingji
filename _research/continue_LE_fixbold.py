# -*- coding: utf-8 -*-
"""续作LE：修复三引号引入的换行导致 ** 未被渲染。

根因：用三引号字符串写入的 overview 含真实换行（\\n），
而 mdesc() 的粗体正则 `\\*\\*(.+?)\\*\\*` 默认不跨行匹配，
因此跨行的 **...** 无法渲染，残留 ** 于页面上。

修复两处：
1) 数据层：把 overview（及同类长文本字段）中的换行规范化为空——
   中文段落本不需要硬换行；
2) 渲染层：给 mdesc 的正则加 re.S，跨行也能渲染（防御性）。
"""
import glob
import json
import re

# ── 1) 数据层规范化 ──
FIELDS = ('overview', 'comparison', 'one_line')
fixed = 0
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    ch = False
    for fld in FIELDS:
        v = d.get(fld)
        if isinstance(v, str) and '\n' in v:
            d[fld] = re.sub(r'\s*\n\s*', '', v)
            ch = True
    for t in d.get('timeline') or []:
        ev = t.get('event')
        if isinstance(ev, str) and '\n' in ev:
            t['event'] = re.sub(r'\s*\n\s*', '', ev)
            ch = True
    for s in d.get('schools') or []:
        vw = s.get('view')
        if isinstance(vw, str) and '\n' in vw:
            s['view'] = re.sub(r'\s*\n\s*', '', vw)
            ch = True
    for p in d.get('policy_response') or []:
        for k in ('view', 'measure'):
            v = p.get(k)
            if isinstance(v, str) and '\n' in v:
                p[k] = re.sub(r'\s*\n\s*', '', v)
                ch = True
    if ch:
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        fixed += 1
print('数据层规范化条目数:', fixed)

# ── 2) 渲染层加 re.S 作为防御 ──
P = 'tools/gen_site.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')
n = 0
# 找到 mdesc 内的粗体替换
if "re.sub(r'\\*\\*(.+?)\\*\\*'" in s:
    s = s.replace("re.sub(r'\\*\\*(.+?)\\*\\*'", "re.sub(r'\\*\\*(.+?)\\*\\*', flags_hack if False else 0, ", 0) if False else s
# 直接改用带 re.S 的替换（逐个替换出现处）
before = s
s = s.replace("re.sub(r'\\*\\*(.+?)\\*\\*', r'<strong>\\1</strong>', t)",
              "re.sub(r'\\*\\*(.+?)\\*\\*', r'<strong>\\1</strong>', t, flags=re.S)")
if s != before:
    n += 1
out = s.replace('\n', '\r\n') if crlf else s
open(P, 'wb').write(out.encode('utf-8'))
print('渲染层 mdesc 加 re.S 处数:', n)
