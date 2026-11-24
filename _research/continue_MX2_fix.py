# -*- coding: utf-8 -*-
"""续作MX2：修复"简介称来源未载、正文/时间线却当事实陈述"的不一致，并清理 disclaimer 中的未核实数字。

发现（round 131 抽查）：
- dotcom-bubble-2000：overview 称来源未载 2619%／1000%／900%，但 timeline 仍写"高通股价上涨2619%，多只大盘股涨超1000%"——自相矛盾。
- finnish-banking-1990：disclaimer 复述"近零升至近20%"。
- panic-1901：disclaimer 复述"170 美元与 1000 美元"。
原则：不编造数字；未核实的数字不应在正文/时间线以事实陈述，也不应在 disclaimer 里复述。
"""
import json

# 1) dotcom-bubble-2000：时间线去掉未核实数值；overview disclaimer 去掉复述
p = 'data/entries/dotcom-bubble-2000.json'
d = json.load(open(p, encoding='utf-8'))
for t in d.get('timeline') or []:
    if '2619' in (t.get('event') or ''):
        t['event'] = '1999 高通(Qualcomm)等个股涨幅惊人（具体涨幅数值待核实，现行来源未载）'
d['overview'] = d['overview'].replace(
    '1999年高通(Qualcomm)等个股涨幅惊人（具体涨幅数值待核实：现行来源页面未载 2619%、超1000%、超900% 三项，需补充出处）',
    '1999年高通(Qualcomm)等个股涨幅惊人（具体涨幅数值待核实，现行来源页面未载，需补充出处）')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('dotcom-bubble-2000 已修（timeline + overview）')

# 2) finnish-banking-1990：disclaimer 去复述
p = 'data/entries/finnish-banking-1990.json'
d = json.load(open(p, encoding='utf-8'))
d['overview'] = d['overview'].replace(
    '（具体峰值待核实：现行来源页面未载"近零升至近20%"这一表述，需补充出处）',
    '（具体失业率峰值待核实，现行来源页面未载，需补充出处）').replace(
    '（具体峰值待核实：现行来源页面未载“近零升至近20%”这一表述，需补充出处）',
    '（具体失业率峰值待核实，现行来源页面未载，需补充出处）')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('finnish-banking-1990 已修')

# 3) panic-1901：disclaimer 去复述
p = 'data/entries/panic-1901.json'
d = json.load(open(p, encoding='utf-8'))
d['overview'] = d['overview'].replace(
    '（具体价格数值待核实：现行来源页面未载 170 美元与 1000 美元两项，需补充出处）',
    '（具体价格数值待核实，现行来源页面未载，需补充出处）')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('panic-1901 已修')
