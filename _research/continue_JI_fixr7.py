# -*- coding: utf-8 -*-
"""续作JI：修正 R7 自测（改用修改现有条目制造重复 id，避免备份不存在的文件）。"""
P = 'tools/selftest.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

old = """DUP = os.path.join(ENT, 'zzz-dup-test.json')


def m_r7():
    d = _r(TGT)
    d['title'] = '一个不重复的测试标题'
    _w(DUP, d)


case('R7 重复id', m_r7, ['tools/check.py'], 'R7', [DUP])"""

new = """TGT2 = os.path.join(ENT, 'capital-adequacy.json')


def m_r7():
    d = _r(TGT2)
    d['id'] = 'bank-resolution'     # 与既有条目撞 id
    d['title'] = '一个不重复的测试标题'
    _w(TGT2, d)


case('R7 重复id', m_r7, ['tools/check.py'], 'R7', [TGT2])"""

if 'TGT2' not in s and old in s:
    s = s.replace(old, new, 1)
    s = s.replace("if os.path.exists(DUP):\n    os.remove(DUP)\n", "")
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已修正 R7 自测')
else:
    print('未匹配（可能已改）')
