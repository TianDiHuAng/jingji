# -*- coding: utf-8 -*-
"""续作EM：每个SVG使用唯一marker id并内联引用，消除跨SVG依赖。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

old = '''_SVG_DEF_DONE = {'v': False}   # 单页内是否已注入 arrowhead 定义

def fix_svg(svg, reset=False):
    """给含 marker-end 但缺 defs 的 SVG 注入箭头 marker 定义。

    同一页面只注入一次（HTML 中 id 必须唯一）；后续 SVG 复用已定义的 marker。
    reset=True 表示新页开始，重置标志。
    """
    if reset:
        _SVG_DEF_DONE['v'] = False
        return svg
    if not svg:
        return svg
    if 'id="arrowhead"' in svg:
        _SVG_DEF_DONE['v'] = True
        return svg
    needs = ("class='ar'" in svg) or ('class="ar"' in svg)
    if not needs or _SVG_DEF_DONE['v']:
        return svg          # 已有定义可复用，或无需箭头
    defs = ('<defs><marker id="arrowhead" markerWidth="8" markerHeight="8" '
            'refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" '
            'fill="var(--accent)"/></marker></defs>')
    _SVG_DEF_DONE['v'] = True
    return svg.replace('>', '>'+defs, 1)'''

new = '''_SVG_SEQ = {'n': 0}   # 单页内 SVG 计数，用于生成唯一 marker id

def fix_svg(svg, reset=False):
    """为含箭头的 SVG 注入**唯一 id** 的 arrow marker，并把 marker-end 内联。

    每个 SVG 独立定义自己的 marker（不跨 SVG 引用），确保兼容性；
    同页多个 SVG 时 id 各不相同（HTML 要求 id 唯一）。
    reset=True 表示新页开始，重置计数。
    """
    if reset:
        _SVG_SEQ['n'] = 0
        return svg
    if not svg:
        return svg
    q1, q2 = "class='ar'", 'class="ar"'
    if q1 not in svg and q2 not in svg:
        return svg                      # 无箭头元素，无需处理
    if 'id="arrowhead' in svg:
        return svg                      # 已处理过
    _SVG_SEQ['n'] += 1
    mid = 'arrowhead%d' % _SVG_SEQ['n']
    defs = ('<defs><marker id="%s" markerWidth="8" markerHeight="8" '
            'refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" '
            'fill="var(--accent)"/></marker></defs>' % mid)
    out = svg.replace('>', '>'+defs, 1)
    # 内联 marker-end，避免依赖全局 CSS 与跨 SVG 引用
    inline = ' style="marker-end:url(#%s)"' % mid
    out = out.replace(q1, q1 + inline).replace(q2, q2 + inline)
    return out'''

if old in s:
    s = s.replace(old, new, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('fix_svg 已改为唯一 id + 内联引用')
else:
    print('未匹配')
