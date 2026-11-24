# -*- coding: utf-8 -*-
"""续作JO：把 R20 纳入自测。"""
P = 'tools/selftest.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

EXTRA = '''
# ── 扩展：R20（U1 不得标全球）──
U1T = os.path.join(ENT, 'roman-currency.json')


def m_r20():
    d = _r(U1T)
    d['region'] = '全球'
    _w(U1T, d)


case('R20 U1标全球', m_r20, ['tools/check.py'], 'R20', [U1T])
'''

anchor = "\nprint('=' * 62)"
if 'R20 U1标全球' not in s and anchor in s:
    s = s.replace(anchor, EXTRA + anchor, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已加入 R20 自测')
else:
    print('已存在或未匹配')
