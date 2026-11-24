# -*- coding: utf-8 -*-
"""续作FJ：补写5条案例政策应对。"""
import json
import os
import glob

POL = {
 'weimar-hyper-1921': (
   '**货币改革（地租马克）**：1923年8月经济学家 Karl Helfferich 提议发行"黑麦马克"(Roggenmark)，'
   '以与黑麦市场价格挂钩的抵押债券为支撑，但因黑麦以纸马克计价波动过大而**被否决**。'
   '农业部长 **Hans Luther** 提议以黄金替代黑麦，由此发行 **"地租马克"(Rentenmark)**——'
   '以与黄金市场价格挂钩的债券为支撑，黄金债券按 **2,790 金马克/公斤黄金** 计值（与战前金马克相同）。'
   '地租马克**不可兑换黄金**，只与黄金债券挂钩。'
   '该方案于 **1923年10月13—15日** 的货币改革法令中获得通过；'
   'Luther 出任财政部长时设立了新的 **Rentenbank**。'
   '（正文另记载恶性通胀末期出现以香烟等商品为基础的替代交换媒介。）',
   '据 Wikipedia「Hyperinflation in the Weimar Republic」Stabilization 章节；'
   '政策主体：德国政府/Rentenbank；动作：发行地租马克（以黄金计价债券为锚）、设立新发行银行'),

 'turkish-crisis-2018': (
   '**"行动计划"**：2018 年财长 Albayrak 公布新的三年经济计划以遏制危机，'
   '目标是"控制通胀、刺激增长、削减经常账户赤字"；'
   '措施包括**削减政府支出 100 亿美元**、暂停尚未招标的项目。'
   '**央行独立性问题**：土耳其通胀显著高于其他新兴市场（2017年10月为 **11.9%**，为2008年7月以来最高）；'
   '2018年里拉贬值加速——3月底 4.0、5月中 4.5、8月初 5.0、8月中达 6.0 与 7.0 里拉兑 1 美元。'
   '正文记载了总统对央行政策的干预，经济学家对此有讨论。',
   '据 Wikipedia「Turkish currency and debt crisis, 2018」相关章节；'
   '政策主体：土耳其政府/央行；动作：削减支出100亿美元、暂停未招标项目；总统干预央行'),

 'wall-street-1929': (
   '**调查与立法**：**1932 年**美国参议院设立 **Pecora 委员会**调查崩盘成因；'
   '**次年（1933）国会通过《格拉斯-斯蒂格尔法》**，强制分离吸收存款与发放贷款的商业银行'
   '与承销、发行、分销股票债券的投资银行。'
   '此后全球股市相继……（正文另记载各国市场的后续反应）。',
   '据 Wikipedia「Wall Street crash of 1929」Aftermath 章节；'
   '政策主体：美国参议院/国会；动作：设立调查委员会、通过格拉斯-斯蒂格尔法'),

 'panic-1930': (
   '**制度学习（事后）**：在随之而来的"大收缩"之后，**美联储开始学习应对区域性银行恐慌**，'
   '并**逐步承担起最后贷款人的角色**；'
   '大萧条的结果也使"实施扩张性货币政策的重要性"变得显而易见。',
   '据 Wikipedia「Panic of 1930」Aftermath 章节；'
   '说明：正文记载的是危机后的制度演进（美联储职能转变），而非1930年当年的具体措施'),

 'panic-1907': (
   '**制度背景与后果**：欧美银行体系的一个显著差异是**美国没有中央银行**——'
   '欧洲国家能在现金储备不足时扩张货币供给。'
   '认为美国经济在缺乏央行时很脆弱的看法并不新：1907年初银行家 Jacob Schiff 就曾在纽约商会演讲中警告。'
   '这次恐慌与随后的调查推动了对中央银行制度的需求，'
   '最终促成 **1913 年《联邦储备法》** 的通过。',
   '据 Wikipedia「Panic of 1907」Aftermath 与 Central bank 章节；'
   '说明：正文主要记载制度性后果（催生美联储）；当年私营救助细节见本条目其他章节'),
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FJ】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('\n补写 %d | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
