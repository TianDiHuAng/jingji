# -*- coding: utf-8 -*-
"""检查器自测——注入已知错误，确认每条规则确实能捕获。

动机（round 102 教训）：我多次遇到"以为改了但没生效"的静默失败。
对检查器同样如此：**新增规则如果从未被触发过，就不能确认它有效**。
本脚本对每个新增规则构造一个必然违规的样本，跑检查、断言报错出现、再复原。

覆盖：R4b、R17、R18、R19、check_pages 的文案与导航一致性、check_kd 的分级。
"""
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENT = os.path.join(ROOT, 'data', 'entries')
SRC = os.path.join(ROOT, 'data', 'sources.json')


def run(cmd):
    r = subprocess.run([sys.executable, '-X', 'utf8'] + cmd, cwd=ROOT,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '') + (r.stderr or '')


def backup(paths):
    for p in paths:
        shutil.copy(p, p + '.bak_jf')


def restore(paths):
    for p in paths:
        if os.path.exists(p + '.bak_jf'):
            shutil.move(p + '.bak_jf', p)


results = []


def case(name, mutate, check_cmd, expect_kw, paths):
    backup(paths)
    try:
        mutate()
        out = run(check_cmd)
        ok = expect_kw in out
        results.append((name, ok, expect_kw, out.strip().splitlines()[:1]))
    finally:
        restore(paths)


# ── 1) R17：来源 type 非法 ──
def m_r17():
    d = json.load(open(SRC, encoding='utf-8'))
    d['sources'][0]['type'] = '非法类型XYZ'
    json.dump(d, open(SRC, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R17 来源type非法', m_r17, ['tools/check.py'], 'R17', [SRC])


# ── 2) R18：link_ok 置空 ──
def m_r18():
    d = json.load(open(SRC, encoding='utf-8'))
    d['sources'][0]['link_ok'] = None
    json.dump(d, open(SRC, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R18 link_ok为空', m_r18, ['tools/check.py'], 'R18', [SRC])


# ── 3) R19：timeline 缺 sources ──
TGT = os.path.join(ENT, 'bank-resolution.json')


def m_r19():
    d = json.load(open(TGT, encoding='utf-8'))
    d['timeline'][0].pop('sources', None)
    json.dump(d, open(TGT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R19 timeline缺sources', m_r19, ['tools/check.py'], 'R19', [TGT])


# ── 4) R4b：嵌套字段引用不存在的来源 ──
def m_r4b():
    d = json.load(open(TGT, encoding='utf-8'))
    d['schools'][0]['sources'] = ['w-en-nonexistent-xyz']
    json.dump(d, open(TGT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R4b 嵌套来源不存在', m_r4b, ['tools/check.py'], 'R4', [TGT])


# ── 5) check_pages：comparison 提到但 related 缺失 ──
def m_nav():
    d = json.load(open(TGT, encoding='utf-8'))
    d['related'] = []
    json.dump(d, open(TGT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('文案与导航一致性', m_nav, ['tools/check_pages.py'], '文案与导航一致性', [TGT])

INDEXALL = os.path.join(ROOT, 'site', 'index-all.html')


def m_complete():
    t = open(INDEXALL, encoding='utf-8').read()
    # 移除一个条目链接，应触发"未列全条目"
    import re as _re
    t2 = _re.sub(r'<a href="bank-run\.html">[^<]*</a>', '', t, count=1)
    open(INDEXALL, 'w', encoding='utf-8').write(t2)


case('站点完整性(未列全)', m_complete, ['tools/check_pages.py'], '未列全', [INDEXALL])

_DUP_A = os.path.join(ENT, 'capital-adequacy.json')
_DUP_B = os.path.join(ENT, 'liquidity-coverage-ratio.json')


def m_dupov():
    a = json.load(open(_DUP_A, encoding='utf-8'))
    b = json.load(open(_DUP_B, encoding='utf-8'))
    b['overview'] = a['overview']          # 制造整段重复
    json.dump(b, open(_DUP_B, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('check_filler 整段重复', m_dupov, ['tools/check_filler.py'], '高度相似', [_DUP_B])

MATRIX = os.path.join(ROOT, 'site', 'matrix.html')


def m_matrix():
    t = open(MATRIX, encoding='utf-8').read()
    t2 = t.replace('<td>641</td>', '<td>999</td>')
    open(MATRIX, 'w', encoding='utf-8').write(t2)


case('矩阵合计校验', m_matrix, ['tools/check_pages.py'], '矩阵合计', [MATRIX])

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

TGT2 = os.path.join(ENT, 'capital-adequacy.json')


def m_r7():
    d = _r(TGT2)
    d['id'] = 'bank-resolution'     # 与既有条目撞 id
    d['title'] = '一个不重复的测试标题'
    _w(TGT2, d)


case('R7 重复id', m_r7, ['tools/check.py'], 'R7', [TGT2])


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


def m_r12b():
    d = _r(COV)
    # 把首条的 level 改成与条目文件不一致
    e0 = d['entries'][0]['id']
    d['entries'][0]['level'] = 'L1' if d['entries'][0].get('level') != 'L1' else 'L3'
    _w(COV, d)


case('R12b coverage字段不一致', m_r12b, ['tools/check.py'], 'R12b', [COV])


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


def m_qual_bold():
    t = open(QUAL, encoding='utf-8').read()
    # 注入孤立 **（未配对），应被 check_quality 捕获
    t2 = t.replace('</main>', '<p>孤立粗体**测试</p></main>', 1)
    open(QUAL, 'w', encoding='utf-8').write(t2)


case('check_quality 孤立**', m_qual_bold, ['tools/check_quality.py'], '未渲染', [QUAL])

# ── 扩展：R20（U1 不得标全球）──
U1T = os.path.join(ENT, 'roman-currency.json')


def m_r20():
    d = _r(U1T)
    d['region'] = '全球'
    _w(U1T, d)


case('R20 U1标全球', m_r20, ['tools/check.py'], 'R20', [U1T])

CORE_ENT = os.path.join(ENT, 'tulip-mania-1637.json')


def m_r23():
    d = json.load(open(CORE_ENT, encoding='utf-8'))
    d['level'] = 'L2' if d.get('level') != 'L2' else 'L3'
    json.dump(d, open(CORE_ENT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R23 核心未达L3', m_r23, ['tools/check.py'], 'R23', [CORE_ENT])

CB_ENT = os.path.join(ENT, 'currency-board.json')


def m_r24():
    d = json.load(open(CB_ENT, encoding='utf-8'))
    d['related'] = [r for r in d.get('related', []) if r != 'cook-islands-currency']
    json.dump(d, open(CB_ENT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R24 related孤岛', m_r24, ['tools/check.py'], 'R24', [CB_ENT])

RW_ENT = os.path.join(ENT, 'railway-mania.json')


def m_r25():
    d = json.load(open(RW_ENT, encoding='utf-8'))
    d['unit'] = 'U3 20世纪上半'   # 1845/47 全落在 U3 外 → 触发 R25
    json.dump(d, open(RW_ENT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R25 单元时间线不符', m_r25, ['tools/check.py'], 'R25', [RW_ENT])


def m_r26():
    d = json.load(open(RW_ENT, encoding='utf-8'))
    d.setdefault('timeline', []).append({'year': 2099, 'event': '未来事件测试'})
    json.dump(d, open(RW_ENT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R26 未来年份事件', m_r26, ['tools/check.py'], 'R26', [RW_ENT])

BH_ENT = os.path.join(ENT, 'bank-holiday.json')


def m_r27():
    d = json.load(open(BH_ENT, encoding='utf-8'))
    d['causal_chain'] = []
    json.dump(d, open(BH_ENT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R27 案例缺因果链', m_r27, ['tools/check.py'], 'R27', [BH_ENT])

SRCJSON = os.path.join(ROOT, 'data', 'sources.json')


def m_r28():
    d = json.load(open(SRCJSON, encoding='utf-8'))
    # 复制一个已有来源、改 id 但保留同 url → 触发 R28
    import copy
    s = copy.deepcopy(d['sources'][0])
    s['id'] = 'zz-dup-url-test'
    d['sources'].append(s)
    d['count'] = len(d['sources'])
    json.dump(d, open(SRCJSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R28 来源URL重复', m_r28, ['tools/check.py'], 'R28', [SRCJSON])


def m_r29():
    d = json.load(open(RW_ENT, encoding='utf-8'))
    d['period'] = '20世纪上半'   # 与 unit U2 不对应 → 触发 R29
    json.dump(d, open(RW_ENT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R29 period与unit不符', m_r29, ['tools/check.py'], 'R29', [RW_ENT])


def m_r30():
    d = json.load(open(RW_ENT, encoding='utf-8'))
    d['region'] = '殴洲'   # 拼写错的非法枚举 → 触发 R30
    json.dump(d, open(RW_ENT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('R30 枚举值非法', m_r30, ['tools/check.py'], 'R30', [RW_ENT])

REPORT_MD = os.path.join(ROOT, 'REPORT.md')


def m_report_num():
    t = open(REPORT_MD, encoding='utf-8').read()
    t2 = t.replace('总条目 641', '总条目 999', 1)
    open(REPORT_MD, 'w', encoding='utf-8').write(t2)


case('check_docs REPORT数字', m_report_num, ['tools/check_docs.py'], '不一致', [REPORT_MD])

BACKLOG_MD = os.path.join(ROOT, 'BACKLOG.md')


def m_backlog_dup():
    t = open(BACKLOG_MD, encoding='utf-8').read()
    # 把已建成条目塞进"概念缺口"表
    t2 = t.replace('| `sacrifice-ratio` |', '| `bank-resolution` | 测试注入 |\n| `sacrifice-ratio` |', 1)
    open(BACKLOG_MD, 'w', encoding='utf-8').write(t2)


case('BACKLOG 缺口含已建条目', m_backlog_dup, ['tools/check_docs.py'], '把已建成条目列为缺口', [BACKLOG_MD])

SCOPE_MD = os.path.join(ROOT, 'scope.md')


def m_scope_miss():
    lines = open(SCOPE_MD, encoding='utf-8').read().split('\n')
    out = [l for l in lines if not l.startswith('| tulip-mania-1637 |')]
    open(SCOPE_MD, 'w', encoding='utf-8').write('\n'.join(out))


case('scope 未覆盖条目', m_scope_miss, ['tools/check_docs.py'], '未覆盖条目', [SCOPE_MD])

SAT_JSON = os.path.join(ROOT, 'SATURATION.json')


def m_sat():
    d = json.load(open(SAT_JSON, encoding='utf-8'))
    d['saturated'] = True
    json.dump(d, open(SAT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


case('SATURATION 误报饱和', m_sat, ['tools/check_docs.py'], '误报饱和', [SAT_JSON])

print('=' * 62)
print('检查器自测结果')
print('=' * 62)
npass = 0
for name, ok, kw, line in results:
    print('  %-28s %s' % (name, '通过' if ok else '**未捕获**'))
    if not ok:
        print('      期望关键字: %s | 首行输出: %s' % (kw, line))
    npass += 1 if ok else 0
print('-' * 62)
print('捕获成功 %d/%d' % (npass, len(results)))
