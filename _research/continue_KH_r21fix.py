# -*- coding: utf-8 -*-
"""续作KH：改进 R21 判据——先剥离专名与括号内容，再计算英文占比。

问题：4 个条目（danatbank-1931／merrill-lynch／creditanstalt／silicon-valley-bank）
是**中文内容 + 必要的机构全称**，英文占比被专名拉高到 48—63%，
但它们并非"英文摘要充正文"。

改进：计算前先移除
  ①中文/英文括号内的内容；
  ②连续 2 词以上、首字母大写的英文专名序列（机构名、人名）。
再以剩余文本计算英文占比。
"""
P = 'tools/check.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

old = """    # R21 overview 须以中文为主（英文占比不得 >45%）
    import re as _re21
    for _e in entries:
        _ov = _e.get('overview') or ''
        _zh = len(_re21.findall(r'[\\u4e00-\\u9fff]', _ov))
        _en = len(_re21.findall(r'[A-Za-z]', _ov))
        if _zh + _en > 40:
            _r21 = _en / (_zh + _en)
            if _r21 > 0.45:
                err('R21', _e.get('id', '?'),
                    'overview 英文占比 %.0f%%（须 ≤45%%）' % (_r21 * 100))"""

new = """    # R21 overview 须以中文为主（剥离专名与括号内容后，英文占比不得 >45%）
    import re as _re21
    for _e in entries:
        _ov = _e.get('overview') or ''
        _t = _re21.sub(r'[（(][^）)]{0,120}[）)]', '', _ov)          # 去括号内容
        _t = _re21.sub(r'(?:[A-Z][A-Za-z&.\\-]*\\s+){1,}[A-Z][A-Za-z&.\\-]*', '', _t)  # 去英文专名序列
        _t = _re21.sub(r'\\b[A-Z]{2,}\\b', '', _t)                     # 去缩写（SVB/TARP 等）
        _zh = len(_re21.findall(r'[\\u4e00-\\u9fff]', _t))
        _en = len(_re21.findall(r'[A-Za-z]', _t))
        if _zh + _en > 40:
            _r21 = _en / (_zh + _en)
            if _r21 > 0.45:
                err('R21', _e.get('id', '?'),
                    'overview 英文占比 %.0f%%（剥离专名后仍超 45%%）' % (_r21 * 100))"""

if '剥离专名后' not in s and old in s:
    s = s.replace(old, new, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('R21 判据已改进')
else:
    print('未匹配（可能已改）')
