# -*- coding: utf-8 -*-
"""续作NQ：修正 3 条 overview 中不平衡的 ** 标记（局部嵌套导致渲染残留）。"""
import json

FIX = {
 'capital-flight': (
   '**因此危机管理的核心之一是**"如何让持有者相信不必跑"**。',
   '**因此危机管理的核心之一是**：如何让持有者相信不必跑。'),
 'financial-accelerator': (
   '**关键的政策含义**：**修复净值**（而非仅仅降低利率）才是打破这一循环的关键。',
   '**关键的政策含义是：修复净值（而非仅仅降低利率）才是打破这一循环的关键。**'),
 'short-selling': (
   '**一个关键的制度安排是"**裸卖空"与"有担保卖空"的区别**：',
   '**一个关键的制度安排**是"裸卖空"与"有担保卖空"的区别：'),
}
for eid, (a, b) in FIX.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    if a in d['overview']:
        d['overview'] = d['overview'].replace(a, b)
        d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作NQ｜round137】修正 overview 中不平衡的 ** 标记。')
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(eid, '已修；** 计数=', d['overview'].count('**'))
    else:
        print(eid, '未匹配原文（可能已改），当前 ** 计数=', d['overview'].count('**'))
