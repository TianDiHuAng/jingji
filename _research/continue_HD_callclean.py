# -*- coding: utf-8 -*-
"""续作HD：在 gen_site.py 实际写出页面前调用清理函数。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

# 1) 插入清理函数（放在 page() 定义之前）
if '_cleanup_stale_pages' not in s:
    helper = '''
# ── 生成前清理：删除不再对应任何条目/特殊页的旧 .html ───────────────
def _cleanup_stale_pages(outdir, entry_ids, special):
    """避免条目被删除或改 id 后，旧页面作为孤儿文件累积在站点里。"""
    if not os.path.isdir(outdir):
        return []
    removed = []
    for fn in os.listdir(outdir):
        if not fn.endswith('.html'):
            continue
        if fn[:-5] in entry_ids or fn[:-5] in special:
            continue
        try:
            os.remove(os.path.join(outdir, fn))
            removed.append(fn)
        except OSError:
            pass
    return removed


'''
    i = s.find('def page(')
    s = s[:i] + helper.lstrip('\n') + s[i:]
    print('已插入清理函数')

# 2) 在第一次写 site 目录之前调用（找到 index.html 的写出点）
marker = "open(os.path.join(SITE,'index.html'),'w',encoding='utf-8')"
call = ("""_SPECIAL = {'index','cases','concepts','index-all','timeline','sources','verification','matrix'}
_SPECIAL |= {'unit-' + u.split()[0].lower() for u in units}
_removed = _cleanup_stale_pages(SITE, set(entries.keys()), _SPECIAL)
if _removed:
    print('清理过时页面: %d 个（%s）' % (len(_removed), ', '.join(_removed[:5])))

""")
if call.strip() not in s:
    s = s.replace(marker, call + marker, 1)
    print('已插入清理调用')
else:
    print('调用已存在')

open(p, 'w', encoding='utf-8').write(s)
