# -*- coding: utf-8 -*-
"""续作JK：把 check_filler 纳入自测——注入 5 种模板句，确认能捕获。"""
P = 'tools/selftest.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

EXTRA = '''
# ── 扩展：check_filler 套话检测 ──
FL = os.path.join(ENT, 'capital-adequacy.json')

_FILLER_CASES = [
    ('与同为「银行」类危机共享相似传导机制', '模板句/套话'),
    ('与同类案例共享这一特征', '模板句/套话'),
    ('本案例对其他案例均适用', '模板句/套话'),
]


def _mk_filler(text):
    def _m():
        d = _r(FL)
        d['comparison'] = text + '。' + ('补充说明' * 20)
        _w(FL, d)
    return _m


for _i, (_txt, _name) in enumerate(_FILLER_CASES, 1):
    case('check_filler 套话%d' % _i, _mk_filler(_txt), ['tools/check_filler.py'], '模板', [FL])

# 占位数值
def m_ph():
    d = _r(FL)
    d['key_data'] = [{'label': '测试指标', 'value': 0, 'unit': '待补', 'year': 2020,
                      'comparable_price': False, 'note': '待补', 'sources': [d['sources'][0]]}]
    _w(FL, d)


case('check_filler 占位值', m_ph, ['tools/check_filler.py'], '占位', [FL])
'''

anchor = "\nprint('=' * 62)"
if 'check_filler 套话' not in s and anchor in s:
    s = s.replace(anchor, EXTRA + anchor, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已加入 check_filler 自测（CRLF=%s）' % crlf)
else:
    print('已存在或未匹配')
