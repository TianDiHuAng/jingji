# -*- coding: utf-8 -*-
"""续作JG：把自测扩展到核心规则 R1／R7／R8／R9／R10／R12。"""
P = 'tools/selftest.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

EXTRA = '''

# ── 扩展：核心数据规则 ──
def _w(path, d):
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def _r(path):
    return json.load(open(path, encoding='utf-8'))


# 6) R1 必填字段缺失
def m_r1():
    d = _r(TGT)
    d.pop('one_line', None)
    _w(TGT, d)


case('R1 必填字段缺失', m_r1, ['tools/check.py'], 'R1', [TGT])


# 7) R7 重复 id
DUP = os.path.join(ENT, 'zzz-dup-test.json')


def m_r7():
    d = _r(TGT)
    d['id'] = 'bank-resolution'
    d['title'] = '一个不重复的测试标题'
    _w(DUP, d)


case('R7 重复id', m_r7, ['tools/check.py'], 'R7', [DUP])


# 8) R8 timeline 年份非升序
def m_r8():
    d = _r(TGT)
    d['timeline'] = [{'year': 2020, 'event': 'x', 'sources': ['w-en-bank-bailout']},
                     {'year': 1900, 'event': 'y', 'sources': ['w-en-bank-bailout']}]
    _w(TGT, d)


case('R8 timeline年份乱序', m_r8, ['tools/check.py'], 'R8', [TGT])


# 9) R9 key_data value 非数值
def m_r9():
    d = _r(TGT)
    d['key_data'] = [{'label': '测试指标', 'value': '十二', 'unit': '项', 'year': 2011,
                      'comparable_price': False, 'note': '测试', 'sources': ['org-fsb-key-attributes']}]
    _w(TGT, d)


case('R9 key_data值非数值', m_r9, ['tools/check.py'], 'R9', [TGT])


# 10) R10 SVG 元素非法
def m_r10():
    d = _r(TGT)
    d['deep_svg'] = ('<svg viewBox="0 0 10 10"><foreignObject></foreignObject></svg>')
    _w(TGT, d)


case('R10 SVG非法元素', m_r10, ['tools/check.py'], 'R10', [TGT])


# 11) R12 coverage 引用了不存在的条目
COV = os.path.join(ROOT, 'coverage.json')


def m_r12():
    d = _r(COV)
    d['entries'].append({'id': 'zzz-not-exist', 'level': 'L1', 'tier': '补充',
                         'status': 'planned', 'source_count': 0, 'needs_verification': 0,
                         'last_updated': '2026-01-01', 'unit': 'U6 理论与制度',
                         'period': '理论制度', 'region': '全球', 'crisis_type': '制度'})
    _w(COV, d)


case('R12 coverage含不存在条目', m_r12, ['tools/check.py'], 'R12', [COV])
'''

# 插在最终输出之前
anchor = "\nprint('=' * 62)\nprint('检查器自测结果')"
if 'R12 coverage' not in s and anchor in s:
    s = s.replace(anchor, EXTRA + anchor, 1)
    # 同时把新文件加入清理
    s = s.replace("print('=' * 62)\nprint('检查器自测结果')",
                  "if os.path.exists(DUP):\n    os.remove(DUP)\nprint('=' * 62)\nprint('检查器自测结果')", 1)
    with open(P, 'w', encoding='utf-8', newline='') as f:
        f.write(s)
    print('已扩展自测至 R1/R7/R8/R9/R10/R12')
else:
    print('已存在或未匹配')
