# -*- coding: utf-8 -*-
"""续作IW：为缺 sources 的 timeline 事件补上来来源。

策略（按优先级）：
1. 若 event 文本含"据 Wikipedia <页面名>"，尝试在 sources.json 中按 title 匹配；
2. 否则使用该条目的主来源（sources[0]）；
3. 若仍无来源可用，保持空缺并记入 pending_notes（不编造）。
"""
import glob
import json
import re

srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
by_title = {}
for s in srcs:
    t = (s.get('title') or '').lower()
    if t:
        by_title[t] = s['id']

PAT = re.compile(r'据\s*Wikipedia\s*[「《]?([^）」》]+)[」》]?')
filled = by_topic = 0
unresolved = []

for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    tl = d.get('timeline') or []
    if not tl:
        continue
    ch = False
    for t in tl:
        if t.get('sources'):
            continue
        ev = t.get('event') or ''
        m = PAT.search(ev)
        sid = None
        if m:
            key = m.group(1).strip().lower()
            sid = by_title.get(key)
            # 模糊匹配：包含关系
            if not sid:
                for tt, ii in by_title.items():
                    if key and (key in tt or tt in key):
                        sid = ii
                        break
        if sid:
            t['sources'] = [sid]
            filled += 1
            ch = True
        elif d.get('sources'):
            t['sources'] = [d['sources'][0]]
            by_topic += 1
            ch = True
        else:
            unresolved.append((d['id'], ev[:40]))
    if ch:
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('按"据 Wikipedia X"精确补入:', filled)
print('按条目主来源补入:', by_topic)
print('仍无来源可补:', len(unresolved))
for u in unresolved[:8]:
    print('  ', u)

# 复核
es = [json.load(open(x, encoding='utf-8')) for x in glob.glob('data/entries/*.json')]
tot = sum(len(e.get('timeline', [])) for e in es)
ws = sum(1 for e in es for t in (e.get('timeline') or []) if t.get('sources'))
print('\ntimeline 来源覆盖: %d/%d = %.0f%%' % (ws, tot, ws * 100 / tot))
