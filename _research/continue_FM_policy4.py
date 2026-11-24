# -*- coding: utf-8 -*-
"""续作FM：补写4条案例政策应对。"""
import json
import os
import glob

POL = {
 'danish-bankruptcy-1813': (
   '**宣布破产并设立新国家银行**：**1813年1月5日**丹麦-挪威宣布破产，'
   '并设立新的国家银行 **Rigsbank** 以带领经济走出困境。'
   'Rigsbank 的两大目标是：**稳定经济**、建立**统一的全州货币体系**；'
   '它是第一个负责通过**重构货币**来稳定经济的政府机构。'
   '**1818 年**成立**私营**的 **Nationalbank**，向公民与企业提供信贷以助经济复苏，'
   '目标是恢复**白银**为丹麦经济的核心货币、并恢复对中央银行体系的信心。',
   '据 Wikipedia「Danish state bankruptcy of 1813」Bankruptcy declared 与相关章节；'
   '政策主体：丹麦-挪威政府/Rigsbank/Nationalbank；动作：设新国家银行、重构货币、恢复银本位'),

 'zimbabwe-hyper-2007': (
   '**货币重定值(Redenomination)**：1980 年独立时津巴布韦元成为通用货币；'
   '随着支付小额款项需要更大面额，津巴布韦储备银行计划印制并发行高达 '
   'Z$10、20、50、100 **万亿** 的面额。'
   '**最终方案——采用外币为官方货币**：津巴布韦实际采纳的解决办法是'
   '**将某些外币定为官方货币**。为便利商业，采用**哪一种**货币并不如'
   '"政府统一到**单一货币**"重要；候选为美元、欧元与南非兰特，'
   '其中**美元**最具可信度、在津巴布韦境内也最为广泛流通。',
   '据 Wikipedia「Hyperinflation in Zimbabwe」Redenomination 与 Solutions 章节；'
   '政策主体：津巴布韦储备银行/政府；动作：货币重定值、采用外币为法定货币（美元化）'),

 'enron': (
   '**财务重述与监管调查**：**2001年10月16日**安然宣布须重述 1997—2000 年财务报表以纠正会计违规。'
   '重述使该期间**利润减少 6.13 亿美元**（约占所报利润的 **23%**）、'
   '使 2000 年末**负债增加 6.28 亿美元**（约占所报负债的 6%、权益的 5.5%），并降低了权益。'
   '此后美国证交会(SEC) 展开调查；该案最终促成**萨班斯-奥克斯利法**(2002) 的通过。',
   '据 Wikipedia「Enron scandal」Restructuring losses and SEC investigation 与相关章节；'
   '政策主体：SEC/美国国会；动作：财务重述、监管调查、立法改革'),

 'washington-mutual': (
   '**接管后的处置**：2008 年华盛顿互惠银行被置入**接管(receivership)**后，'
   '其分支机构被 FDIC 出售给摩根大通(Chase)；'
   '2009 年内，所有被购买的原 WaMu 分行被**重新冠名为 Chase 或关闭**，'
   '所有 WaMu 发出的财务文件改为带有 Chase 标识，'
   'WaMu 与 Providian 发行的信用卡与借记卡也改为 Chase 标识。',
   '据 Wikipedia「Washington Mutual」Post receivership bank operations 章节；'
   '政策主体：FDIC/摩根大通；动作：接管并出售、品牌与业务整合'),
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FM】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('\n补写 %d | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
