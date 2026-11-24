# -*- coding: utf-8 -*-
"""续作IK：用 FSB 官方页补 sifi 条目的认定机制。"""
import json

SID = 'org-fsb-gsib'
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
if SID not in {s['id'] for s in sj['sources']}:
    sj['sources'].append({
        'id': SID,
        'title': 'Global Systemically Important Financial Institutions (G-SIFIs) — FSB',
        'author': 'Financial Stability Board (FSB)',
        'year': '2026',
        'type': '权威机构',
        'url': 'https://www.fsb.org/work-of-the-fsb/market-and-institutional-resilience/global-systemically-important-financial-institutions-g-sifis/',
        'url2': None,
        'verified': True,
        'link_ok': True,
        'note': 'FSB 关于全球系统重要性金融机构的官方说明页；含 G-SIB 识别起始年份与年度更新安排',
    })
    sj['count'] = len(sj['sources'])
    json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('注册来源:', SID)

p = 'data/entries/sifi.json'
d = json.load(open(p, encoding='utf-8'))

if SID not in d['sources']:
    d['sources'].append(SID)

d['overview'] = (
    '系统重要性金融机构（SIFI）指其失败可能触发金融危机的银行、保险公司或其他金融机构。'
    '这类机构俗称"太大而不能倒"；因其倒闭外溢巨大，监管对其施加更高的资本与处置要求。'
    '**认定机制（以全球系统重要性银行为例，据 FSB 官方说明）**：'
    'FSB 与巴塞尔银行监管委员会(BCBS)及各国当局协商，'
    '**自 2011 年起**识别全球系统重要性银行(G-SIBs)；'
    '名单被划分为若干 **"分档"(buckets)**，每一档对应不同水平的**附加损失吸收能力**要求；'
    '名单**每年 11 月更新**一次，同时公布对 G-SIB 适用政策措施的落实情况。'
    '国内层面另有各自认定的 D-SIB（国内系统重要性银行）体系；具体分档阈值与打分方法待核实。')

d['timeline'] = [
    {'year': 2011, 'event': 'FSB 与 BCBS 及各国当局协商，开始识别全球系统重要性银行(G-SIBs)'
                            '（据 FSB G-SIFIs 官方说明）'},
    {'year': 2011, 'event': 'G-SIB 名单按"分档"(buckets)划分，各档对应不同附加损失吸收能力要求'
                            '（据 FSB G-SIFIs 官方说明）'},
]

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作IK】补 FSB 官方认定机制（2011 年起识别、分档对应附加损失吸收要求、'
                        '每年 11 月更新）；分档阈值与打分方法待核对原文。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('sifi 已补充：来源 %d、timeline %d' % (len(d['sources']), len(d['timeline'])))
print('overview 长度:', len(d['overview']))
