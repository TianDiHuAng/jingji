# -*- coding: utf-8 -*-
"""续作IQ：把"comparison 提到的条目必须在 related 中"固化为检查项（加入 check_pages.py）。"""
P = 'tools/check_pages.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

if '文案与导航一致性' in s:
    print('已存在，跳过')
else:
    # 在 main() 的 problems 输出之前插入检查
    anchor = "    print('期望值:', expect)"
    block = '''    # ── 文案与导航一致性：comparison 提到的条目应出现在 related 中 ──
    _ids = {e['id'] for e in es}
    for e in es:
        comp = e.get('comparison') or ''
        if not comp:
            continue
        mentioned = {i for i in _ids if i != e['id'] and i in comp}
        missing = mentioned - set(e.get('related', []))
        if missing:
            problems.append(('data/' + e['id'] + '.json', '文案与导航一致性',
                             '提到但未在related中', ','.join(sorted(missing)[:3])))

'''
    if anchor in s:
        s = s.replace(anchor, block + anchor, 1)
        with open(P, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('已插入"文案与导航一致性"检查')
    else:
        print('未找到锚点')
