# -*- coding: utf-8 -*-
"""续作JJ：把 R10 的 SVG 校验扩展到 deep_svg 字段。

发现（round 104）：check.py 第 195 行只校验 e['svg']（588 条），
而 L3 机制图存在 e['deep_svg']（34 条）从未被校验。
好消息：34 条 deep_svg 的 XML 均可解析；但元素白名单未检查。
"""
P = 'tools/check.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

old = "    check_svg(e.get('svg',''), where)"
new = """    check_svg(e.get('svg',''), where)
    # R10b deep_svg（L3 机制图）同样须校验
    _dsvg = e.get('deep_svg')
    if _dsvg:
        check_svg(_dsvg, where + ' [deep_svg]')"""

if 'R10b' not in s and old in s:
    s = s.replace(old, new, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已把 R10 扩展到 deep_svg')
else:
    print('已存在或未匹配')
