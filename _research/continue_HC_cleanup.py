# -*- coding: utf-8 -*-
"""续作HC：让 gen_site.py 在生成前清理过时的 .html（条目被删除/改 id 后的残留）。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

# 在写出任何页面之前插入清理逻辑：找到"页面输出目录"的变量名
import re
m = re.search(r'^(OUT|SITE|DEST)\s*=\s*', s, re.M)
print('输出目录变量:', m.group(1) if m else '未找到，使用 site/')

anchor = None
for cand in ('def page(', 'if __name__'):
    i = s.find(cand)
    if i > 0:
        anchor = i
        break

cleanup = '''
# ── 生成前清理：删除不再对应任何条目/特殊页的旧 .html ───────────────
def _cleanup_stale_pages(outdir, entry_ids, special):
    """避免条目被删除或改 id 后，旧页面成为孤儿文件累积在站点里。"""
    if not os.path.isdir(outdir):
        return []
    removed = []
    for fn in os.listdir(outdir):
        if not fn.endswith('.html'):
            continue
        stem = fn[:-5]
        if stem in entry_ids or stem in special:
            continue
        try:
            os.remove(os.path.join(outdir, fn))
            removed.append(fn)
        except OSError:
            pass
    return removed


'''

if '_cleanup_stale_pages' not in s:
    # 插到第一个 def 之前
    first_def = s.find('\ndef ')
    if first_def < 0:
        first_def = s.find('def ')
    s = s[:first_def] + cleanup + s[first_def:]
    open(p, 'w', encoding='utf-8').write(s)
    print('已插入 _cleanup_stale_pages 函数')
else:
    print('清理函数已存在')
