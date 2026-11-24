# -*- coding: utf-8 -*-
"""定位 HTML 中残留的 ** 位置（哪个页面、哪段文本）。"""
import glob
import re

for f in glob.glob('site/*.html'):
    t = open(f, encoding='utf-8').read()
    if '**' in t:
        for m in re.finditer(r'.{80}\*\*.{80}', t, re.S):
            seg = m.group(0).replace('\n', ' ')
            print('%s: ...%s...' % (f.split('/')[-1], seg))
            print()
