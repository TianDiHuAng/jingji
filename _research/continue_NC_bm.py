# -*- coding: utf-8 -*-
"""续作NC：修正 blue-monday-2009。

重大问题（round 132 抽查发现）：
该条目 one_line/overview/timeline 描述的是"2009年3月2日道指跌破7000点、标普676点"，
而其专属来源 w-en-blue-monday-crash-2009 实际描述的是"2009年1月19日英国银行股暴跌（RBS 巨亏）"，
且 7000/676 等数字在所引任何来源中均未出现——属"事件张冠李戴 + 无来源数字"。

修正：改为与来源一致的 1 月 19 日英国银行股事件（key_data 三条本已据该来源），
删除无来源的 3 月美股数字；crisis_type 由"泡沫"改为"银行"。
"""
import json

p = 'data/entries/blue-monday-2009.json'
d = json.load(open(p, encoding='utf-8'))

old_one = d['one_line']
d['one_line'] = ('2009年"蓝色星期一"(1月19日)：RBS 公布英国史上最大企业亏损后，'
                 '英国银行股集体暴跌，RBS 单日跌逾67%。')

d['overview'] = (
    '2009 年"蓝色星期一"(Blue Monday) 指 **2009 年 1 月 19 日（星期一）**'
    '英国银行股的集体暴跌。'
    '**触发点**：**苏格兰皇家银行(RBS) 公布英国史上最大的企业亏损**后，'
    '当天出现**抛售潮**——**RBS 股价单日下跌逾 67%**，'
    '**劳埃德(Lloyds) 跌约 33%、巴克莱(Barclays) 跌约 10%、汇丰(HSBC) 跌约 6%**；'
    '**次日（1 月 20 日）** Lloyds 与 Barclays 再度大跌。'
    '**政策反应**：英国首相布朗(Gordon Brown) 着手**把政府对 RBS 的持股提高至 70%**，'
    '市场随即抛售股份；有传闻称全面国有化迫在眉睫。'
    '来源记载：**RBS 2008 财年亏损约 280 亿英镑**。'
    '**须澄清命名**：「蓝色星期一」在不同语境中可能指不同日期；'
    '本条**依据专属来源，记述的是 2009 年 1 月 19 日的英国银行股事件**。'
    '（另：2009 年 3 月初美股下挫、标普 500 于 3 月见底约 676 点，属**另一段市场行情**，'
    '不在本条所引来源范围内，故不在此并列具体数值。）')

d['timeline'] = [
    {'year': 2009, 'sources': ['w-en-blue-monday-crash-2009'],
     'event': '1月19日 RBS 公布 2008 财年约 280 亿英镑亏损（英国史上最大企业亏损），'
              '股价单日跌逾 67%，英国银行股集体暴跌'},
    {'year': 2009, 'sources': ['w-en-blue-monday-crash-2009'],
     'event': '1月20日 Lloyds、Barclays 继续下跌；英国政府计划将 RBS 持股提高至 70%'},
]

d['crisis_type'] = '银行'

d['comparison'] = (
    '与 `wall-street-1929` 的区别：1929 年崩盘是**全市场估值崩溃 + 银行体系连锁**；'
    '本条则是**单家银行（RBS）巨额亏损公告**引发的**同业股价连锁**，'
    '范围主要限于英国银行板块。'
    '与 `lehman` 的区别：雷曼是**投行流动性枯竭而倒闭**、并引发全球系统性危机；'
    '本条是**已获政府注资的银行**因亏损公告而股价暴跌，'
    '属"**危机深化期的信心冲击**"而非新的系统性断裂。')
if 'lehman' not in d['related']:
    d['related'].append('lehman')
d['related'] = sorted(set(d['related']))

d['pending_notes'] = (d.get('pending_notes', '')
    + ' 【续作NC｜round132】**重大修正**：原 one_line/overview/timeline 描述"2009年3月2日道指跌破7000点、'
      '标普676点"，但专属来源实为"2009年1月19日英国银行股暴跌"，且 7000/676 在所引来源中均未出现——'
      '属事件张冠李戴 + 无来源数字。已改为与来源一致的 1 月 19 日事件，删除无来源的 3 月美股数字；'
      '原 one_line 为「' + old_one + '」。crisis_type 由"泡沫"改为"银行"。'
      '2009年3月美股见底（约676点）为另一事件，如需要应另建条目并补来源。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('blue-monday-2009 已修正')
print('新 one_line:', d['one_line'])
