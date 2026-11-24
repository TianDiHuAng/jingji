# -*- coding: utf-8 -*-
"""续作EO：修正 _add_marker 对自闭合标签的处理。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

old = '''    pat = re.compile(r"<[a-zA-Z][^>]*class=(?:'ar'|\\"ar\\")[^>]*>")
    return pat.sub(_add_marker, out)'''

new = '''    pat = re.compile(r"<[a-zA-Z][^>]*class=(?:'ar'|\\"ar\\")[^>]*>")
    return pat.sub(_add_marker, out)'''

# 直接替换 _add_marker 函数体
old_fn = '''    def _add_marker(m):
        tag = m.group(0)
        if 'marker-end' in tag:
            return tag
        m_style = re.search(r"style=(['\\\"])(.*?)\\1", tag, re.S)
        if m_style:
            q = m_style.group(1)
            val = m_style.group(2).rstrip(';')
            new_style = '%s%s%s' % (q, val + ';marker-end:url(#%s)' % mid if val else 'marker-end:url(#%s)' % mid, q)
            return tag[:m_style.start()] + 'style=' + new_style + tag[m_style.end():]
        return tag[:-1] + ' style="marker-end:url(#%s)"/>' % mid if tag.endswith('/>') else tag[:-1] + ' style="marker-end:url(#%s)">' % mid'''

new_fn = '''    def _add_marker(m):
        tag = m.group(0)
        if 'marker-end' in tag:
            return tag
        add = 'marker-end:url(#%s)' % mid
        m_style = re.search(r"style=(['\\\"])(.*?)\\1", tag, re.S)
        if m_style:                      # 已有 style：把 marker-end 并进去
            q = m_style.group(1)
            val = m_style.group(2).strip().rstrip(';')
            merged = (val + ';' + add) if val else add
            return tag[:m_style.start()] + 'style=' + q + merged + q + tag[m_style.end():]
        if tag.endswith('/>'):           # 自闭合：在 /> 之前插入
            return tag[:-2].rstrip() + ' style="%s"/>' % add
        return tag[:-1].rstrip() + ' style="%s">' % add'''

if old_fn in s:
    s = s.replace(old_fn, new_fn, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('_add_marker 已修正')
else:
    print('未匹配 _add_marker')
