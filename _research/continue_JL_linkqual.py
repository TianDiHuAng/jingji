# -*- coding: utf-8 -*-
"""续作JL：把 check_links 与 check_quality 纳入自测。"""
P = 'tools/selftest.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

EXTRA = '''
# ── 扩展：check_links（站内断链）与 check_quality（HTML 质量）──
PAGE = os.path.join(ROOT, 'site', 'bank-resolution.html')
QUAL = os.path.join(ROOT, 'site', 'capital-adequacy.html')


def m_link():
    t = open(PAGE, encoding='utf-8').read()
    t = t.replace('</main>', '<a href="zzz-nonexistent-page.html">断链测试</a></main>', 1)
    open(PAGE, 'w', encoding='utf-8').write(t)


case('check_links 站内断链', m_link, ['tools/check_links.py'], '断链', [PAGE])


def m_qual():
    t = open(QUAL, encoding='utf-8').read()
    # 删除 <h1> 以触发结构检查
    import re as _re
    t2 = _re.sub(r'<h1[^>]*>.*?</h1>', '', t, count=1, flags=_re.S)
    open(QUAL, 'w', encoding='utf-8').write(t2)


case('check_quality 缺h1', m_qual, ['tools/check_quality.py'], 'h1', [QUAL])
'''

anchor = "\nprint('=' * 62)"
if 'check_links 站内断链' not in s and anchor in s:
    s = s.replace(anchor, EXTRA + anchor, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已加入 check_links / check_quality 自测')
else:
    print('已存在或未匹配')
