# -*- coding: utf-8 -*-
"""续作II：让 gen_site.py 与 check_pages.py 共用 kdclass 判据。"""
import re

# ---- 1) check_pages.py：改用共享模块 ----
P1 = 'tools/check_pages.py'
with open(P1, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

if 'from kdclass import' not in s:
    # 在 import sys 后插入
    s = s.replace("import sys\n", "import sys\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom kdclass import counts as _kdcounts\n", 1)
    # 替换原有的 conf/stat 计算
    old_calc = re.search(r"    conf = sum\(1 for e in es for k in \(e\.get\('key_data'\) or \[\]\) if _conf\(k\)\)\n"
                         r"    stat = sum\(1 for e in es for k in \(e\.get\('key_data'\) or \[\]\) if _stat\(k\)\)", s)
    if old_calc:
        s = s[:old_calc.start()] + "    _c = _kdcounts(es)\n    conf, stat = _c['confirmed'], _c['statview']" + s[old_calc.end():]
        print('1) check_pages.py 已改用共享判据')
    with open(P1, 'w', encoding='utf-8', newline='') as f:
        f.write(s)

# ---- 2) gen_site.py：在统计处调用共享模块 ----
P2 = 'tools/gen_site.py'
with open(P2, 'r', encoding='utf-8', newline='') as f:
    g = f.read()

if 'from kdclass import' not in g:
    g = g.replace("import os\n", "import os\nimport sys as _sys\n_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom kdclass import counts as _kdcounts\n", 1)
    with open(P2, 'w', encoding='utf-8', newline='') as f:
        f.write(g)
    print('2) gen_site.py 已 import 共享模块')
else:
    print('2) 已存在')
