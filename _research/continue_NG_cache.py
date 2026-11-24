# -*- coding: utf-8 -*-
"""续作NG：为 5 条"wiki_full 缓存为通用来源而非专属页"的案例补注，并记入 BACKLOG。

说明：这 5 条条目本身引用了正确的专属来源、内容经人工阅读核对准确；
只是本地 `_research/wiki_full/<id>.txt` 存的是其**通用来源**（Currency crisis / Economic bubble / Bank run 等）的文本，
专属来源的全文未缓存，导致本地无法逐数核对。网络恢复后应补抓专属来源全文。
"""
import json

IDS = ['dutch-stock-crashes', 'panic-1896', 'panic-1910',
       'us-video-game-crash-1983', 'yemen-currency-divergence']
NOTE = (' 【续作NG｜round133】核实：本地 wiki_full 缓存为**通用来源**（如 Currency crisis／Economic bubble／Bank run）'
        '而非本条的专属来源页；条目**已正确引用专属来源**，内容经人工阅读核对准确，'
        '但专属来源全文未缓存，本地数/年核对受限。**网络恢复后应补抓专属来源全文**。')
for eid in IDS:
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    if '续作NG' not in (d.get('pending_notes') or ''):
        d['pending_notes'] = (d.get('pending_notes', '') + NOTE)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, 'pending_notes 已补注')

# BACKLOG 记录
bl = 'BACKLOG.md'
b = open(bl, encoding='utf-8').read()
add = """
## 待办：补抓专属来源全文（5 条案例，round 133 记录）

以下条目的本地 `_research/wiki_full/<id>.txt` 存的是其**通用来源**的文本（Currency crisis／Economic bubble／Bank run 等），
**专属来源页的全文未缓存**，导致本地无法逐数/逐年核对。条目本身引用正确、内容经人工阅读准确。

**网络恢复后需为下列条目补抓其专属来源全文（按 sources 中非通用的那一项）：**
"""
for eid in IDS:
    d = json.load(open('data/entries/%s.json' % eid, encoding='utf-8'))
    add += '- `%s`（%s）：sources=%s\n' % (eid, d['title'], d['sources'])
add += """
**补抓方法**：用 Wikipedia API 按专属来源的 title 抓 extract，覆盖写入 `_research/wiki_full/<id>.txt`，
然后跑 `check_kd.py` / `check_body_num.py` 复核。
"""
if '补抓专属来源全文（5 条案例' not in b:
    b = b.rstrip() + '\n' + add
    open(bl, 'w', encoding='utf-8').write(b)
    print('BACKLOG 已记录 5 条缓存缺口')
