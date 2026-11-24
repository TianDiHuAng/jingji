# -*- coding: utf-8 -*-
"""续作IL：用 FSB 官方页补 shadow-banking 的监管政策沿革（timeline）。"""
import json

SID = 'org-fsb-nbfi'
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
if SID not in {s['id'] for s in sj['sources']}:
    sj['sources'].append({
        'id': SID,
        'title': 'Non-Bank Financial Intermediation — FSB',
        'author': 'Financial Stability Board (FSB)',
        'year': '2026',
        'type': '权威机构',
        'url': 'https://www.fsb.org/work-of-the-fsb/market-and-institutional-resilience/post-2008-financial-crisis-reforms/non-bank-financial-intermediation/',
        'url2': None,
        'verified': True,
        'link_ok': True,
        'note': 'FSB 非银行金融中介(NBFI)官方说明页；含 2013 年五项政策建议与 2020 年 3 月市场压力记述',
    })
    sj['count'] = len(sj['sources'])
    json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('注册来源:', SID)

p = 'data/entries/shadow-banking.json'
d = json.load(open(p, encoding='utf-8'))
if SID not in d['sources']:
    d['sources'].append(SID)

# 概述补监管政策五个领域
if '五个领域' not in d['overview']:
    d['overview'] = d['overview'].rstrip() + (
        '**监管政策的五个领域（据 FSB 官方说明）**：2013 年 FSB 与标准制定机构(SSBs)'
        '制定加强 NBFI 监督与监管的政策建议，获 G20 认可，聚焦——'
        '①缓减**银行与 NBFI 部门之间的溢出**；②降低**货币市场基金(MMF)对"挤兑"的脆弱性**；'
        '③改善透明度、校准**证券化**相关的激励；'
        '④抑制**回购与证券借贷等证券融资交易**的顺周期性与金融稳定风险；'
        '⑤评估并缓减其他非银行实体与活动的**系统性风险**。')

# timeline
if not d.get('timeline'):
    d['timeline'] = [
        {'year': 2013, 'event': 'FSB 与标准制定机构制定加强 NBFI 监督与监管的政策建议，'
                                '获 G20 认可，聚焦五个领域（据 FSB NBFI 官方说明）'},
        {'year': 2020, 'event': 'COVID-19 疫情使全球金融体系承压：3 月关键融资市场出现剧烈压力，'
                                '公共当局需采取广泛措施恢复市场功能——这凸显加强 NBFI 韧性的必要'
                                '（据 FSB NBFI 官方说明）'},
    ]

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作IL】补 FSB 官方监管政策沿革（2013 五项建议／2020 年 3 月市场压力）。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('shadow-banking 已补充：来源 %d、timeline %d' % (len(d['sources']), len(d['timeline'])))
