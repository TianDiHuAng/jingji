# -*- coding: utf-8 -*-
"""续作JN：加入 R20（U1 单元不得标"全球"），并纳入自测。"""
P = 'tools/check.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

old = "    # R14 分层顺序"
new = """    # R20 U1（早期—17世纪）不适用"全球"标签
    for _e in entries:
        if str(_e.get('unit', '')).startswith('U1') and _e.get('region') == '全球':
            err('R20', _e.get('id', '?'), 'U1 时期尚无全球金融体系，不应标 region=全球')
    # R14 分层顺序"""

if 'R20' not in s and old in s:
    s = s.replace(old, new, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已加入 R20')
else:
    print('已存在或未匹配')
