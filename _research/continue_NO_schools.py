# -*- coding: utf-8 -*-
"""续作NO：为 3 条单观点的"重要"概念补第二派（真实争论，据现有来源）。"""
import json

ADD = {
 'effective-demand': (
   '萨伊定律／古典视角',
   '古典经济学认为"供给创造自己的需求"，价格与利率的调整会使储蓄自动转化为投资，'
   '因此**总体上不存在持续的有效需求不足**，政府需求管理既无必要也可能有害——'
   '这正是凯恩斯"有效需求不足"论的对立面（据 Wikipedia Effective demand 及萨伊定律）',
   'w-en-effective-demand'),
 'inequality': (
   '效率／增长权衡视角',
   '一定程度的不平等提供工作与投资激励、有利于资本积累与增长；'
   '库兹涅茨假说进一步认为不平等随经济发展先升后降。'
   '该视角主张关注"机会不平等"而非结果均等（据 Wikipedia Economic inequality 相关讨论）',
   'w-en-inequality'),
 'demand': (
   '需求定律视角',
   '在其他条件不变时，价格上升则需求量下降（需求定律）；'
   '这是需求曲线向下倾斜的根据，也与"需求量变化"（沿曲线）和"需求变化"（曲线移动）的区分相关'
   '（据 Wikipedia Demand）',
   'w-en-demand'),
}
for eid, (holder, view, sid) in ADD.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    if holder in {s.get('holder') for s in d.get('schools') or []}:
        continue
    d.setdefault('schools', []).append({'holder': holder, 'view': view, 'sources': [sid]})
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作NO｜round136】补 schools 第二派观点（据现有来源）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%-20s schools += 1 (共 %d)' % (eid, len(d['schools'])))
