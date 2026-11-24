# -*- coding: utf-8 -*-
"""续作HM：新建 recession-1960-1961 与 recession-1969-1970（READER_QUESTIONS 所列边缘缺口）。"""
import glob
import json
import os

NEW = {
 'recession-1960-1961': {
   'title': '1960—1961年衰退（美国）',
   'tier': '补充',
   'one_line': '美国1960年4月至1961年2月的10个月衰退，GDP下降1.4%，随后是史上第三长的扩张期。',
   'overview': ('美国 1960—1961 年衰退据 NBER 判定持续 **10 个月**（1960年4月—1961年2月），'
                '其间美国 GDP 下降 **1.4 个百分点**。'
                '这次衰退的特殊之处在于**它开启了美国史上第三长的扩张期**（1961年2月—1969年12月）。'
                '政策背景：美联储自 1958 年起收紧货币政策、1961 年转向宽松；'
                '衰退虽在 1961 年 2 月结束，**失业率却继续上升数月**，'
                '直到 1961 年 5 月才达到该周期高点——这是"衰退结束 ≠ 劳动力市场立刻恢复"的经典例证。'),
   'timeline': [
     {'year': 1960, 'event': '4月衰退开始（据 Wikipedia Recession of 1960–1961）'},
     {'year': 1961, 'event': '2月衰退结束，随后进入美国史上第三长扩张期（据 Wikipedia Recession of 1960–1961）'},
     {'year': 1961, 'event': '5月失业率达到该周期高点，晚于衰退结束三个月（据 Wikipedia Recession of 1960–1961）'},
   ],
   'schools': [
     ('货币政策成因说', '美联储自 1958 年起收紧、1961 年才转向宽松，紧缩的时滞与力度被视为衰退的诱因之一'
                        '（据 Wikipedia Recession of 1960–1961）', 'w-en-recession-1960-1961'),
     ('就业滞后现象', '衰退结束后失业率仍上升数月，说明产出转折与就业转折之间存在显著时滞'
                      '（据 Wikipedia Recession of 1960–1961）', 'w-en-recession-1960-1961'),
   ],
   'key_data': [
     ('衰退持续月数', 10, '个月', 1961, '原文：the recession lasted for 10 months'),
     ('GDP 降幅', 1.4, '百分点', 1961, '原文：the GDP of the United States fell 1.4 percentage points'),
   ],
   'comparison': ('与本条目库中其他美国衰退的区别：这次衰退的**幅度较小但开启了最长的扩张之一**，'
                  '因此常被用来说明"衰退深度"与"复苏持续性"并非同一维度。'
                  '与 1969—1970 年衰退的关系：后者紧随这次长扩张之后，成因更偏财政与货币双紧缩。'),
   'related': ['recession-1969-1970', 'business-cycle', 'monetary-policy', 'fiscal-policy', 'recession'],
 },
 'recession-1969-1970': {
   'title': '1969—1970年衰退（美国）',
   'tier': '补充',
   'one_line': '美国1969年12月至1970年11月的11个月温和衰退，GDP仅降0.6%，伴随通胀上升。',
   'overview': ('美国 1969—1970 年衰退据 NBER 判定持续 **11 个月**（1969年12月—1970年11月），'
                '是一次**相对温和**的衰退：GDP 仅下降 **0.6 个百分点**。'
                '其背景是**通胀已在上升**——可能源于充分就业时期的赤字支出扩大。'
                '这次衰退与两项紧缩同时发生：**试图缩减越战造成的财政赤字**（财政紧缩）'
                '与**美联储加息**（货币紧缩）。'
                '通胀与衰退并存的特征使它在当时的宏观政策讨论中具有特殊地位。'),
   'timeline': [
     {'year': 1968, 'event': '经济下滑已在年底开始，早于 NBER 判定的衰退起点（据 Wikipedia Recession of 1969–1970）'},
     {'year': 1969, 'event': '12月衰退开始，与财政紧缩及美联储加息同时（据 Wikipedia Recession of 1969–1970）'},
     {'year': 1970, 'event': '11月衰退结束（据 Wikipedia Recession of 1969–1970）'},
   ],
   'schools': [
     ('财政与货币双紧缩', '越战赤字收紧与美联储加息同时发生，构成衰退的直接背景'
                          '（据 Wikipedia Recession of 1969–1970）', 'w-en-recession-1969-1970'),
     ('通胀先行', '衰退前通胀已在上升，可能与充分就业下的赤字支出有关；'
                  '这使"紧缩治通胀"与"紧缩致衰退"的因果难以简单分离'
                  '（据 Wikipedia Recession of 1969–1970）', 'w-en-recession-1969-1970'),
   ],
   'key_data': [
     ('衰退持续月数', 11, '个月', 1970, '原文：the recession lasted for 11 months'),
     ('GDP 降幅', 0.6, '百分点', 1970, '原文：the gross domestic product of the United States fell 0.6 percen'),
   ],
   'comparison': ('与 1960—1961 年衰退的区别：两者都是短促衰退，但前者（1969—70）**伴随通胀上行**，'
                  '后者发生在低通胀环境。'
                  '与 1973—75 年衰退的关系：后者规模更大且与石油冲击叠加，'
                  '1969—70 常被视为"滞胀"主题的前奏。'),
   'related': ['recession-1960-1961', 'business-cycle', 'monetary-policy', 'fiscal-policy', 'oil-crisis-1973'],
 },
}

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}
titles = {e['title'] for e in es}
for eid in list(NEW):
    if eid in ids or NEW[eid]['title'] in titles:
        print('跳过（已存在）:', eid)
        NEW.pop(eid)

# 注册来源
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
have = {s['id'] for s in sj['sources']}
META = {
 'w-en-recession-1960-1961': ('Recession of 1960–1961', 'https://en.wikipedia.org/wiki/Recession_of_1960%E2%80%931961'),
 'w-en-recession-1969-1970': ('Recession of 1969–1970', 'https://en.wikipedia.org/wiki/Recession_of_1969%E2%80%931970'),
}
for sid, (t, u) in META.items():
    if sid not in have:
        sj['sources'].append({'id': sid, 'title': t, 'author': 'Wikipedia contributors', 'year': '2026',
                              'type': '权威百科', 'url': u, 'url2': None, 'verified': True,
                              'link_ok': True, 'note': 'Wikipedia API 核对（本会话抓取全文）'})
        print('注册来源:', sid)
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

n = 0
for eid, v in NEW.items():
    sid = 'w-en-' + eid
    d = {
        'id': eid, 'title': v['title'], 'level': 'L2', 'tier': v['tier'],
        'unit': 'U4 20世纪下半', 'period': '20世纪下半', 'region': '北美',
        'crisis_type': '其他',
        'one_line': v['one_line'], 'overview': v['overview'],
        'timeline': v['timeline'], 'causal_chain': [],
        'schools': [{'holder': h, 'view': vw, 'sources': [src]} for h, vw, src in v['schools']],
        'key_data': [{'label': lb, 'value': val, 'unit': u, 'year': y, 'comparable_price': False,
                      'note': nt + '；单一来源待核实。', 'sources': [sid]}
                     for lb, val, u, y, nt in v['key_data']],
        'comparison': v['comparison'],
        'related': [r for r in v['related'] if r in ids],
        'sources': [sid], 'needs_verification': True,
        'pending_notes': '【续作HM】据维基专属页全文新建；来源为单一维基页面，数值待第二来源印证。',
    }
    json.dump(d, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('新建:', eid)

cov = json.load(open('coverage.json', encoding='utf-8'))
covids = {e['id'] for e in cov['entries']}
for eid, v in NEW.items():
    if eid not in covids:
        cov['entries'].append({'id': eid, 'level': 'L2', 'tier': v['tier'], 'status': 'written',
                               'source_count': 1, 'needs_verification': 1, 'last_updated': '2026-11-24',
                               'unit': 'U4 20世纪下半', 'period': '20世纪下半', 'region': '北美',
                               'crisis_type': '其他'})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新建 %d 条 | coverage total: %d' % (n, cov['total']))
