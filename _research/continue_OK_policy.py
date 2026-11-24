# -*- coding: utf-8 -*-
"""续作OK：为 3 条 case 补 policy_response（事实均取自其已引专属来源的本地缓存，未引入外部/新事实）。

- nixon-shock：正文已含政策，补充"90天/10%"精确值（缓存有），提炼 policy_response。
- creditanstalt：原 overview 为 stub（"待核实补充"），据 w-en-creditanstalt 缓存改写，并加救助 policy_response。
- drexel：补"监管与结局"句（SEC/NYSE/纽联储存疑→和解→第11章破产，救助未落实），提炼 policy_response。
"""
import json

def add_pr(eid, pr_holder, pr_view, pr_basis, pr_src, note):
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    d['policy_response'] = [{'holder': pr_holder, 'view': pr_view, 'basis': pr_basis, 'sources': [pr_src]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' ' + note)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%-16s policy_response 已加' % eid)

# 1) nixon-shock：精确化正文（90 天、10%），再提炼
p = 'data/entries/nixon-shock.json'
d = json.load(open(p, encoding='utf-8'))
d['overview'] = d['overview'].replace(
    '包括**冻结工资与物价、对进口加征附加税**，以及**单方面取消美元对黄金的直接国际兑换**',
    '包括**冻结工资与物价（为期 90 天，依据 1970 年《经济稳定法》）、对进口加征 10% 附加税**，以及**单方面取消美元对黄金的直接国际兑换**')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
add_pr('nixon-shock', '美国政策当局（尼克松政府）',
       '1971 年 8 月 15 日宣布的一揽子措施包括：为期 90 天的工资与物价冻结（依据 1970 年《经济稳定法》）、'
       '对进口加征 10% 附加税，以及单方面取消美元对黄金的直接兑换。',
       '据本条目正文与专属来源提炼；具体经济效果评价待核实',
       'w-en-nixon-shock', '【续作OK｜round148】正文补"90天/10%"精确值并加 policy_response。')

# 2) creditanstalt：改写 stub 正文 + 救助 policy_response
p = 'data/entries/creditanstalt.json'
d = json.load(open(p, encoding='utf-8'))
d['overview'] = (
    'Creditanstalt（k. k. priv. Österreichische Credit-Anstalt für Handel und Gewerbe）1855 年创立于维也纳，'
    '长期由罗斯柴尔德家族主导，是奥匈帝国时期的重要银行。**1931 年它的失败具有历史性后果，被视为引发大萧条的首批重大银行倒闭之一**，'
    '并成为中欧银行危机的引爆点。**政策应对**：奥地利总理奥托·恩德尔(Otto Ender)组织救助，'
    '由**奥地利政府、奥地利国家银行(Oesterreichische Nationalbank)与罗斯柴尔德家族**共同分担成本，'
    '并**否决了社会民主党主张的国有化方案**；1933 年末由多爾富斯(Dollfuß)下令、1934 年该行与维也纳银行协会(Wiener Bankverein)'
    '及下奥地利贴现公司(Niederösterreichische Escompte-Gesellschaft)的健全部分合并。此后 1938 年并入德意志银行体系，'
    '1945 年国有化，1997 年被 Bank Austria 收购。**与危机的关系**：它展示了"单一重要银行的失败如何经同业敞口与信心渠道'
    '传导为区域性乃至全球性危机"，是 1931 年中欧连锁银行危机的起点。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
add_pr('creditanstalt', '奥地利政策当局',
       '1931 年危机中，总理恩德尔组织救助，由奥地利政府、奥地利国家银行与罗斯柴尔德家族共同分担成本，'
       '否决了社会民主党主张的国有化；1934 年该行与维也纳银行协会及下奥地利贴现公司的健全部分合并。',
       '据本条目正文与专属来源提炼；救助规模/效果待核实',
       'w-en-creditanstalt', '【续作OK｜round148】原 overview 为 stub，据 w-en-creditanstalt 缓存改写并加 policy_response。')

# 3) drexel：补"监管与结局"句 + policy_response
p = 'data/entries/drexel.json'
d = json.load(open(p, encoding='utf-8'))
if '监管与结局' not in d['overview']:
    d['overview'] = d['overview'].rstrip() + (
        '**监管与结局**：在证券交易委员会(SEC)、纽约证交所与纽约联储对重组计划存疑后，'
        '德崇管理层判定其无法维持独立；**政府救助最终未成现实**，公司转而与检察官 Giuliani 达成和解，'
        '并于 1990 年 2 月申请《破产法》第 11 章破产以避免被 SEC 查封。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
add_pr('drexel', '美国监管与司法当局',
       'SEC、纽约证交所与纽约联储对德崇的重组计划存疑，公司无法维持独立；政府救助未落实，'
       '德崇最终与检察官 Giuliani 达成和解并于 1990 年 2 月申请第 11 章破产以避免被 SEC 查封。',
       '据本条目正文与专属来源提炼；问责与和解细节待核实',
       'w-en-drexel', '【续作OK｜round148】补"监管与结局"句并加 policy_response。')
