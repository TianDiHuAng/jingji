# -*- coding: utf-8 -*-
"""续作EL：修复同页多SVG导致的重复 id="arrowhead"。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

# 1) fix_svg 增加 need_defs 参数（默认 True），当同页已定义过则不再注入
old_fn = '''def fix_svg(svg):
    """给含 marker-end 但缺 defs 的 SVG 注入箭头 marker 定义（保证双模式可读）。"""
    if not svg or 'id="arrowhead"' in svg or ("class='ar'" not in svg and 'class="ar"' not in svg):
        return svg
    defs = ('<defs><marker id="arrowhead" markerWidth="8" markerHeight="8" '
            'refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" '
            'fill="var(--accent)"/></marker></defs>')
    return svg.replace('<svg ', '<svg ', 1).replace('>', '>'+defs, 1)'''

new_fn = '''_SVG_DEF_DONE = {'v': False}   # 单页内是否已注入 arrowhead 定义

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

if old_fn in s:
    s = s.replace(old_fn, new_fn, 1)
    print('fix_svg 已改为单页只注入一次')
else:
    print('fix_svg 未匹配')

# 2) 在 render_entry 开始处重置标志
old_r = "def render_entry(e):"
new_r = "def render_entry(e):\n    fix_svg('', reset=True)   # 新页：重置 arrowhead 注入标志"
if old_r in s and 'reset=True' not in s.split('def render_entry')[1][:200]:
    s = s.replace(old_r, new_r, 1)
    print('render_entry 已加入重置')

open(p, 'w', encoding='utf-8').write(s)
