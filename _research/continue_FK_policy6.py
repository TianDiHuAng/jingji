# -*- coding: utf-8 -*-
"""续作FK：补写6条案例政策应对。"""
import json
import os
import glob

POL = {
 'savings-loan-1986': (
   '**处置成本与保险基金枯竭**：1985—86 年的倒闭对 FSLIC 极为昂贵——'
   '1985 年处置成本 **74 亿美元**、1986 年 **91 亿美元**，'
   '使 FSLIC 准备金在 1987 年前夕降至**不足 20 亿美元**；'
   '与此同时储贷业规模大为扩张，使这点准备金被摊得极薄。'
   'FSLIC 的即时反应是提高存款保险费率以增加收入。'
   '**资不抵债的规模**：1988 年底按 FHLBB 监管准则正式资不抵债的机构为 **250 家**，'
   '剔除无形资产后**翻倍至 508 家**；此时 FSLIC 自身也已资不抵债。'
   '**立法处置**：1989年2月6日新总统布什提出处置储贷机构倒闭的方案，'
   '最终形成 **FIRREA** 法与新设的**重组信托公司(RTC)**。',
   '据 Wikipedia「Savings and loan crisis」FSLIC recapitalization 与 FIRREA and the RTC 章节；'
   '政策主体：FSLIC/总统/国会；动作：提高保险费率、FIRREA立法、设立RTC'),

 'signature-bank': (
   '**资产处置**：**2023年3月19日**，FDIC 宣布 Signature Bridge Bank 的部分存款与贷款'
   '将由纽约社区银行(NYCB) 承接，其 **40 家分行**并入 Flagstar Bank 子公司（3月20日生效）。'
   '该交易**不包括约 600 亿美元贷款**，这部分留在接管程序中——'
   '其中包括 **110 亿美元**的租金管制公寓贷款。',
   '据 Wikipedia「Signature Bank」Disposition of assets 章节；'
   '政策主体：FDIC；动作：部分资产出售给NYCB、其余留在接管程序'),

 'china-liquidity-2013': (
   '**有意不注入流动性**：面对市场反应，人民银行**拒绝**注入额外资金来弥补流动性缺口，'
   '这被解读为从"快速增长"转向"有质量的增长"的**重大政策变化**。'
   '分析人士认为，突然收紧放贷利率是**对过度放贷银行的警告**，'
   '意在约束其放贷行为。',
   '据 Wikipedia「Chinese Banking Liquidity Crisis of 2013」PBOC Reaction 章节；'
   '政策主体：中国人民银行；动作：拒绝注入流动性（有意收紧以示警）'),

 'soviet-hyper-1917': (
   '**转向新经济政策(NEP)**：面对经济崩溃与广泛的农民反抗，'
   '**1921年春**苏联政府改变方针，通过采用**新经济政策**回归国家与农民之间的市场关系：'
   '以规范化的**"实物税"**取代强制征购；NEP 的组成部分还包括恢复**功能性的货币**。',
   '据 Wikipedia 相关条目 Coming of the NEP period 章节；'
   '政策主体：苏联政府；动作：以实物税替代强制征购、恢复货币与市场关系'),

 'panic-1857': (
   '**总统层面的应对**：到 1859 年恐慌趋于平息、经济开始稳定。'
   '布坎南总统宣布纸币体系似乎是恐慌的**根源**，'
   '决定**撤回 20 美元以下银行券的使用**；'
   '他"建议州银行脱离[发行]银行"，并要求它们效法联邦政府的做法——'
   '称此举将减少纸币。',
   '据 Wikipedia「Panic of 1857」Remedies 章节；'
   '政策主体：美国总统/联邦政府；动作：撤回小面额银行券、劝导州银行减少发行'),

 'panic-1893': (
   '**财政部的黄金借款**：恐慌期间财政部黄金储备降至危险水平，'
   '迫使克利夫兰总统通过著名的 **Morgan-Belmont 辛迪加**，'
   '向华尔街银行家 **J. P. Morgan** 与英国的**罗斯柴尔德家族借入 6500 万美元黄金**。'
   '（正文另记载 1893 年恐慌后有**四分之一**的铁路里程进入破产接管，'
   '按当时美元计约 18 亿美元，为 1876—1910 年间记录的最大数额。）',
   '据 Wikipedia「Panic of 1893」相关章节；'
   '政策主体：美国财政部/总统；动作：通过私营辛迪加借入6500万美元黄金补充储备'),
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FK】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('\n补写 %d | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
