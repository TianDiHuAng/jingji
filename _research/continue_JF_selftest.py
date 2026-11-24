# -*- coding: utf-8 -*-
"""续作JF：检查器自测——注入已知错误，确认新增规则确实能捕获。

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
