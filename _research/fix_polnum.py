# -*- coding: utf-8 -*-
"""改进 check_polnum：把条目自身正文并入查找范围。"""
p = 'tools/check_polnum.py'
s = open(p, encoding='utf-8').read()

old = "        txt = open(p, encoding='utf-8').read().lower()"
new = (
    "        txt = open(p, encoding='utf-8').read().lower()\n"
    "        # 条目自身正文也并入查找范围：部分数字出自 overview/comparison 而非维基全文\n"
    "        own = ' '.join([e.get('overview') or '', e.get('comparison') or '', e.get('one_line') or ''])\n"
    "        txt += ' ' + own.lower()\n"
)

if old in s and 'own = ' not in s:
    s = s.replace(old, new, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('已加入条目正文作为查找范围')
else:
    print('未匹配或已存在')
