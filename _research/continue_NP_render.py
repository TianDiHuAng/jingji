# -*- coding: utf-8 -*-
"""round 137：扫描生成 HTML 的渲染异常。"""
import glob, re
BAD = ['>None<', '>nan<', 'None ', '&lt;', '{}', "list' object", "dict' object",
       '>True<', '>False<', '**']
cnt = {b: [] for b in BAD}
for f in glob.glob('site/*.html'):
    t = open(f, encoding='utf-8').read()
    for b in BAD:
        if b in t:
            cnt[b].append(f.split('/')[-1].split('\\')[-1])
for b in BAD:
    if cnt[b]:
        print('%-16s 出现于 %d 页: %s' % (repr(b), len(cnt[b]), cnt[b][:5]))
    else:
        print('%-16s 无' % repr(b))
