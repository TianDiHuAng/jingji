# -*- coding: utf-8 -*-
"""续作ON：为 nigeria-debt / angola-oil-dependence / ems 补 policy_response（事实取自各自已引来源的本地缓存）。"""
import json

def load(eid):
    return json.load(open('data/entries/%s.json' % eid, encoding='utf-8'))
def save(eid, d):
    json.dump(d, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# nigeria-debt
d = load('nigeria-debt')
d['overview'] = d['overview'].rstrip() + (
    ' **政策应对**：2005—06 年尼日利亚与巴黎俱乐部(Paris Club)达成协议，'
    '以约 **120 亿美元**现金回购大部分欠款、约 **180 亿美元**债务被减免，'
    '成为**首个全额偿清巴黎俱乐部债务的非洲国家**。')
d['policy_response'] = [{'holder': '尼日利亚政府与巴黎俱乐部',
    'view': '2005—06 年与巴黎俱乐部达成协议：以约 120 亿美元现金回购大部分欠款、约 180 亿美元债务获减免，成为首个全额清偿巴黎俱乐部债务的非洲国家。',
    'basis': '据本条目正文与专属来源提炼；协议细节以来源为准', 'sources': ['w-en-nigeria-econ']}]
d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作ON｜round151】据 w-en-nigeria-econ 缓存补巴黎俱乐部减免并加 policy_response。')
save('nigeria-debt', d); print('nigeria-debt ok')

# angola-oil-dependence
d = load('angola-oil-dependence')
d['overview'] = d['overview'].rstrip() + (
    ' **政策应对**：1987 年政府宣布经济自由化、鼓励私人投资；1998 年启动改革，'
    '2000 年 4 月起接受国际货币基金组织(IMF)的职员监督计划(SMP)；并借助世界银行推进私有化（首家为 BCI 银行）。')
d['policy_response'] = [{'holder': '安哥拉政府与国际机构',
    'view': '1987 年宣布经济自由化、鼓励私人投资；1998 年启动改革；2000 年 4 月起接受 IMF 职员监督计划(SMP)；并借助世界银行推进私有化（首家为 BCI 银行）。',
    'basis': '据本条目正文与专属来源提炼；效果评价待核实', 'sources': ['w-en-angola-econ']}]
d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作ON｜round151】据 w-en-angola-econ 缓存补自由化/IMF/私有化并加 policy_response。')
save('angola-oil-dependence', d); print('angola-oil-dependence ok')

# ems（正文已含 ERM/ECU，直接提炼）
d = load('ems')
d['policy_response'] = [{'holder': '欧洲共同体成员国（EMS 制度设计）',
    'view': '以欧洲货币单位(ECU)为篮子货币、各成员国货币维持波动区间(ERM)，越界须干预或调整中心汇率；德国马克与德国央行逐渐成为体系锚；后续 Delors 计划分三阶段走向单一货币与欧洲央行。',
    'basis': '据本条目正文与专属来源提炼；运行效果与危机待核实', 'sources': ['w-en-ems']}]
d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作ON｜round151】据正文提炼 policy_response（ERM 制度设计）。')
save('ems', d); print('ems ok')
