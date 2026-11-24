# -*- coding: utf-8 -*-
"""续作FA：基于维基全文为案例补写 policy_response（人工核验后撰写）。"""
import json
import os

POL = {
 'amsterdam-crisis-1763': (
   '阿姆斯特丹银行（荷兰央行）**提供额外流动性**以缓解危机；'
   '学者认为这是这场恐慌影响相对温和的主要原因之一。'
   '危机后 1763 年 8—9 月仍有 38 家阿姆斯特丹商号破产，但多为小企业，'
   '在与债权人达成和解后数月内得以复业；到 10 月市场已显现回归常态的迹象（活动水平低于此前）。',
   '据 Wikipedia「Amsterdam banking crisis of 1763」Policy response 章节；'
   '政策主体：阿姆斯特丹银行（央行）；动作：提供额外流动性'),

 'chilean-crisis-1982': (
   '**1981年11月起政府救助银行**：大型的 Banco de Talca 与 Banco Español Chile、'
   '小型的 Banco de Linares 与 Banco de Fomento de Valparaíso 获救助，'
   '四家金融公司（Compañía General、Cash、Capitales、del Sur）亦被救助；'
   '其中 Banco de Talca 与 Banco Español Chile 被**国有化**（撤换管理层、剥夺股东所有权，后再度私有化）。'
   '**1983年1月13日政府实施大规模银行干预**，救助五家银行并解散另外三家。'
   '危机后经济政策转向，纳入部分食品的价格带与浮动汇率。',
   '据 Wikipedia 相关条目 Bank interventions 与 Aftermath 章节；'
   '政策主体：智利政府；动作：救助、国有化、解散、汇率制度改革'),

 'china-2015-turbulence': (
   '**2015年政府应对**：国有金融机构组成的"国家队"投入 **1.6 万亿元人民币**买入数千家公司股票；'
   '监管机构限制券商净卖出、暂停新股发行(IPO)、限制卖空；'
   '政府以央行资金为后盾向券商提供买入股票的资金；'
   '中国证监会还对持股超过 5% 的股东实施**六个月内禁止减持**。',
   '据 Wikipedia 相关条目 2015 Government response 章节；'
   '政策主体：中国政府/证监会；动作：入市买入、限制卖空与减持、暂停IPO'),

 'china-realestate-2020': (
   '**2021年9月22日**，珠海市与深圳南山区政府将恒大相关物业的销售收入纳入**政府监管账户**，'
   '以保护购房者并推动项目建设；随着数百个项目停工，多省跟进。'
   '**2021年10月**有报道称中央政府计划推行**全国性房产税**以抑制投机，但据报党内存在广泛阻力。'
   '**2023年1月**，人民银行与银保监会允许房价连续三个月下跌的城市**下调或取消首套房贷款利率下限**；'
   '到 2023 年 2 月中已有 30 多个城市将房贷利率降至十余年最低，地方政府并提供购房补贴与放宽限购。'
   '**2024年3月**，住房和城乡建设部部长倪虹在发布会上表示，资不抵债的房地产开发企业应当破产。',
   '据 Wikipedia 相关条目 Chinese government responses 与 Response 章节；'
   '政策主体：地方政府/中央部委/央行；动作：资金监管、房贷利率调整、破产表态'),

 'brazil-2014': (
   '**反危机措施**（多数不受欢迎，在罗塞夫被弹劾、特梅尔接任后推行或提出）：'
   '第 95 号**宪法修正案**（"新财政制度"）为未来 **20 年**的政府支出设定上限；'
   '《外包法》允许企业将外包员工用于主营业务（此前仅限安保、清洁等辅助业务）；'
   '**2017年劳动改革**。**2017年一季度**GDP 环比回升 **1%**，为连续八个季度下滑后的首次回升；'
   '财政部长称国家已走出"本世纪最大衰退"，但经济学家认为这仅标志"技术性衰退"结束，'
   '因失业率仍高，断言危机结束为时过早。',
   '据 Wikipedia 相关条目 Anti-crisis measures 与 Recovery 章节；'
   '政策主体：巴西联邦政府/国会；动作：宪法支出上限、劳动改革、外包法'),

 'barings-1995': (
   '**市场化处置（非政府救助）**：荷兰银行 ING 于 1995 年以**象征性的 1 英镑**收购巴林银行，'
   '并**承担其全部负债**，组建子公司 ING Barings。'
   '2001 年 ING 将美国业务以 2.75 亿美元售予 ABN Amro，'
   '其余并入欧洲银行部门；最终仅余资产管理业务（Baring Asset Management），'
   '2005 年被拆分出售给 MassMutual。'
   '该案成为"以象征价格整体承债收购"这一处置方式的参照。',
   '据 Wikipedia「Barings Bank」Aftermath 章节；'
   '处置主体：ING（私营）；动作：1英镑收购并承担全部负债'),
}

n = 0
for eid, (view, basis) in POL.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('policy_response'):
        print('已有', eid); continue
    d['policy_response'] = [{
        'holder': '政策当局' if eid != 'barings-1995' else '处置方（私营）',
        'view': view,
        'basis': basis + '；效果评价待核实',
        'sources': d['sources'][:2],
    }]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FA】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

import glob
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('补写 %d 条 | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
