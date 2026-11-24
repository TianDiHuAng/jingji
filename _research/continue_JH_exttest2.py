# -*- coding: utf-8 -*-
"""续作JH：扩展自测（CRLF 感知）。

注：tools/selftest.py 是 CRLF 文件；直接用 '\\n' 作锚点会匹配失败（round 82/83 的老问题）。
本脚本读入时把 CRLF 归一化为 LF，操作后按原文件的行尾风格写回。
"""
import re

P = 'tools/selftest.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')
print('原文件 CRLF =', crlf)

EXTRA = '''
# ── 扩展：核心数据规则 ──
def _w(path, d):
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def _r(path):
    return json.load(open(path, encoding='utf-8'))


def m_r1():
    d = _r(TGT)
    d.pop('one_line', None)
    _w(TGT, d)


case('R1 必填字段缺失', m_r1, ['tools/check.py'], 'R1', [TGT])

DUP = os.path.join(ENT, 'zzz-dup-test.json')


def m_r7():
    d = _r(TGT)
    d['title'] = '一个不重复的测试标题'
    _w(DUP, d)


case('R7 重复id', m_r7, ['tools/check.py'], 'R7', [DUP])


def m_r8():
    d = _r(TGT)
    d['timeline'] = [{'year': 2020, 'event': 'x', 'sources': [d['sources'][0]]},
                     {'year': 1900, 'event': 'y', 'sources': [d['sources'][0]]}]
    _w(TGT, d)


case('R8 timeline年份乱序', m_r8, ['tools/check.py'], 'R8', [TGT])


def m_r9():
    d = _r(TGT)
    d['key_data'] = [{'label': '测试指标', 'value': '十二', 'unit': '项', 'year': 2011,
                      'comparable_price': False, 'note': '测试', 'sources': [d['sources'][0]]}]
    _w(TGT, d)


case('R9 key_data值非数值', m_r9, ['tools/check.py'], 'R9', [TGT])


def m_r10():
    d = _r(TGT)
    d['deep_svg'] = '<svg viewBox="0 0 10 10"><foreignObject></foreignObject></svg>'
    _w(TGT, d)


case('R10 SVG非法元素', m_r10, ['tools/check.py'], 'R10', [TGT])

COV = os.path.join(ROOT, 'coverage.json')


def m_r12():
    d = _r(COV)
    d['entries'].append({'id': 'zzz-not-exist', 'level': 'L1', 'tier': '补充',
                         'status': 'planned', 'source_count': 0, 'needs_verification': 0,
                         'last_updated': '2026-01-01', 'unit': 'U6 理论与制度',
                         'period': '理论制度', 'region': '全球', 'crisis_type': '制度'})
    _w(COV, d)


case('R12 coverage含不存在条目', m_r12, ['tools/check.py'], 'R12', [COV])

if os.path.exists(DUP):
    os.remove(DUP)
'''

anchor = "\nprint('=' * 62)"
if 'R12 coverage' not in s and anchor in s:
    s = s.replace(anchor, EXTRA + anchor, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已扩展自测（R1/R7/R8/R9/R10/R12），行尾保持 CRLF =', crlf)
else:
    print('已存在或未匹配锚点')
