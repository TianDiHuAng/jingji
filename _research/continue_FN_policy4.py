# -*- coding: utf-8 -*-
"""续作FN：补写4条案例政策应对。"""
import json
import os
import glob

POL = {
 'merrill-lynch': (
   '**以出售完成的处置（非政府救助）**：巨额损失归因于其**未对冲**的按揭资产组合'
   '（以 CDO 形式持有）价值下跌；交易对手对美林**偿付能力与货币市场再融资能力**'
   '失去信心，最终导致其被出售。部分银行甚至考虑：若雷曼倒闭，就**停止与美林交易**。'
   '为应对债券需求骤降，金融机构以**贱卖价格**出售按揭证券与 CDO 以偿付到期债务。'
   '（2008年9月的收购由美国银行完成。）',
   '据 Wikipedia「Merrill Lynch」Sale to Bank of America 章节；'
   '处置方式：被美国银行收购（市场化并购，非政府注资）；背景为CDO损失与交易对手信心崩塌'),

 'hungarian-hyper-1945': (
   '**货币更替终结恶性通胀**：pengő 于 **1927年1月1日**取代 korona 成为匈牙利货币，'
   '又于 **1946年7月31日**被 **forint** 取代。'
   'pengő 的引入本身是战后稳定计划的一部分，但它仅存续 20 年，'
   '即被史上最极端的恶性通胀变得一文不值。'
   '**末期的发行记录**：1946年7月11日匈牙利国家银行发行最后一批 pengő 纸币'
   '（1 亿 B-pengő，即 10²⁰）；银行还印制了 10 亿 B-pengő（10²¹）面额但**从未进入流通**；'
   '7月25日发行最后的 adópengő 纸币（1 亿 adópengő），'
   '到 7月31日相当于 2×10²⁹ pengő。',
   '据 Wikipedia「Hungarian pengő」End of the pengő 与相关章节；'
   '政策主体：匈牙利国家银行/政府；动作：以 forint 取代 pengő（货币更替）'),

 'ukrainian-crisis-2008': (
   '**央行行政管制与外部融资**：**2008年10月**乌克兰国家银行对**提前取款实施暂停令(moratorium)**。'
   '到 2008年12月11日，银行组合中不良贷款占比升至 **10.3%** 且继续上升；'
   '银行几乎停止放贷、客户争相提取存款。'
   '2008年11月工业产出同比**骤降 28.6%**（10月已降 19.8%）。'
   '**国际层面**：**2009年4月** IMF 预测乌克兰经济 2009 年萎缩 **8.0%**、2010 年增长 1.0%，'
   '并与乌方就救助计划展开磋商（IMF 驻乌代表团团长 Ceyla Pazarbasioglu 参与）。',
   '据 Wikipedia「Ukrainian crisis of 2008」2008 与 2009 章节；'
   '政策主体：乌克兰国家银行/IMF；动作：对提前取款实施暂停令、IMF 救助磋商'),

 'tripartite-1936': (
   '**三方协议（1936年9月）**：该协议是**非正式、临时性**的。'
   '签署国同意**避免竞争性贬值**、将货币价值维持在现有水平——'
   '前提是这种努力不会严重妨碍**国内繁荣**。'
   '**法国**作为协议的一部分对本国货币**贬值**；'
   '其余金集团国家——**比利时、瑞士、荷兰**——也签署了该协议。',
   '据 Wikipedia「Tripartite Agreement of 1936」Agreement 章节；'
   '政策主体：法、英、美及金集团国家；动作：承诺避免竞争性贬值、法国贬值换取协议'),
}

n = 0
for eid, (view, basis) in POL.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('policy_response'):
        print('已有', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
                             'basis': basis + '；效果评价待核实',
                             'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FN】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('\n补写 %d | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
