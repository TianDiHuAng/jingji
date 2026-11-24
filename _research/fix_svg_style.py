# -*- coding: utf-8 -*-
"""续作EN：修正 marker-end 注入——已有 style 属性时合并而非新增。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

old = '''    out = svg.replace('>', '>'+defs, 1)
    # 内联 marker-end，避免依赖全局 CSS 与跨 SVG 引用
    inline = ' style="marker-end:url(#%s)"' % mid
    out = out.replace(q1, q1 + inline).replace(q2, q2 + inline)
    return out'''

new = '''    out = svg.replace('>', '>'+defs, 1)

    # 为每个含 class='ar' / class="ar" 的元素加 marker-end；
    # 若该元素已有 style 属性则合并（避免 duplicate attribute），否则新增。
    def _add_marker(m):
        tag = m.group(0)
        if 'marker-end' in tag:
            return tag
        m_style = re.search(r"style=(['\\\"])(.*?)\\1", tag, re.S)
        if m_style:
            q = m_style.group(1)
            val = m_style.group(2).rstrip(';')
            new_style = '%s%s%s' % (q, val + ';marker-end:url(#%s)' % mid if val else 'marker-end:url(#%s)' % mid, q)
            return tag[:m_style.start()] + 'style=' + new_style + tag[m_style.end():]
        return tag[:-1] + ' style="marker-end:url(#%s)"/>' % mid if tag.endswith('/>') else tag[:-1] + ' style="marker-end:url(#%s)">' % mid

    pat = re.compile(r"<[a-zA-Z][^>]*class=(?:'ar'|\\"ar\\")[^>]*>")
    return pat.sub(_add_marker, out)'''

if old in s:
    s = s.replace(old, new, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('marker-end 注入已改为合并 style')
else:
    print('未匹配')
