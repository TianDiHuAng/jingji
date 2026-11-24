# -*- coding: utf-8 -*-
"""续作KB：加入 R21——overview 中文占比不得低于 55%（防止英文摘要充正文）。"""
P = 'tools/check.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

old = "    # R14 分层顺序"
new = """    # R21 overview 须以中文为主（英文占比不得 >45%）
    import re as _re21
    for _e in entries:
        _ov = _e.get('overview') or ''
        _zh = len(_re21.findall(r'[\\u4e00-\\u9fff]', _ov))
        _en = len(_re21.findall(r'[A-Za-z]', _ov))
        if _zh + _en > 40:
            _r21 = _en / (_zh + _en)
            if _r21 > 0.45:
                err('R21', _e.get('id', '?'),
                    'overview 英文占比 %.0f%%（须 ≤45%%）' % (_r21 * 100))
    # R14 分层顺序"""

if 'R21' not in s and old in s:
    s = s.replace(old, new, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已加入 R21')
else:
    print('已存在或未匹配')
