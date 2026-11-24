# -*- coding: utf-8 -*-
"""续作IO：新建 taper-tantrum（2013年缩减恐慌）。

来源说明：无专属维基页；实质记述位于「Quantitative easing」页面中关于 tapering 的章节。
本条目明确标注该来源为"通用页中的相关章节"，而非专属页——以便读者判断可信度等级。
"""
import glob
import json

EID = 'taper-tantrum'
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}
titles = {e['title'] for e in es}
if EID in ids or '缩减恐慌' in titles:
    print('已存在，跳过')
    raise SystemExit

SID = 'w-en-quantitative-easing'
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
if SID not in {s['id'] for s in sj['sources']}:
    sj['sources'].append({'id': SID, 'title': 'Quantitative easing', 'author': 'Wikipedia contributors',
                          'year': '2026', 'type': '权威百科',
                          'url': 'https://en.wikipedia.org/wiki/Quantitative_easing', 'url2': None,
                          'verified': True, 'link_ok': True,
                          'note': 'Wikipedia API 核对（本会话抓取全文）；**对 taper-tantrum 条目属通用页**，'
                                  'tapering 记述见其相关章节'})
    sj['count'] = len(sj['sources'])
    json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('注册来源:', SID)

D = {
 'id': EID, 'title': '2013年缩减恐慌', 'level': 'L2', 'tier': '重要',
 'unit': 'U5 21世纪', 'period': '21世纪', 'region': '全球', 'crisis_type': '货币',
 'one_line': '美联储仅暗示将缩减资产购买，即引发全球债券收益率飙升与新兴市场资本外流。',
 'overview': (
   '缩减恐慌(taper tantrum) 指 **2013 年**美联储仅**暗示**将缩减（taper）资产购买规模、'
   '尚未真正收紧政策，就引发全球债券收益率急升与新兴市场资本外流的市场动荡。'
   '**背景**：2012 年 12 月 12 日，美国联邦公开市场委员会(FOMC)宣布把开放式资产购买'
   '从每月 **400 亿美元**增至 **850 亿美元**。'
   '**触发**：**2013 年 6 月 19 日**，时任美联储主席伯南克宣布将**有条件地**缩减 QE——'
   '具体表述为：若经济数据持续向好，可在 **2013 年 9 月**的政策会议上把购债规模'
   '从每月 850 亿美元**降至 650 亿美元**；并暗示购债计划可在**2014 年中期**结束。'
   '他强调并未宣布加息。'
   '**市场反应**的关键在于"预期"而非"行动"：政策尚未改变，长期利率却已大幅上行，'
   '资金从新兴市场回流——这说明**前瞻指引本身就是一种政策工具**，'
   '其表述变化足以产生实质的全球金融条件收紧。'),
 'timeline': [
   {'year': 2012, 'event': '12月12日 FOMC 宣布把开放式资产购买从每月 400 亿增至 850 亿美元'
                           '（据 Wikipedia Quantitative easing）'},
   {'year': 2013, 'event': '6月19日伯南克宣布有条件缩减 QE：若数据向好，9月会议可把购债'
                           '从 850 亿降至 650 亿美元/月，并暗示 2014 年中期结束'
                           '（据 Wikipedia Quantitative easing）'},
   {'year': 2013, 'event': '市场在政策未变的情况下提前反应——长期利率上行、资本从新兴市场流出'
                           '（"缩减恐慌"由此得名）'},
 ],
 'schools': [
   {'holder': '预期渠道视角',
    'view': '央行沟通本身即政策：即便购债规模未变，只要**预期**改变，长端利率与跨境资本流'
            '就会调整——这使"前瞻指引"成为需要谨慎使用的工具',
    'sources': [SID]},
   {'holder': '新兴市场脆弱性视角',
    'view': '资本外流的冲击大小取决于接收国的基本面（外债水平、经常账户赤字、'
            '外汇储备充足度）；同一冲击在不同经济体造成的影响差异极大',
    'sources': [SID]},
 ],
 'key_data': [
   {'label': 'FOMC 宣布的开放式购债规模（2012.12）', 'value': 85, 'unit': '十亿美元/月', 'year': 2012,
    'comparable_price': False,
    'note': '原文：an increase in the amount of open-ended purchases from $40 billion to $85 billion per month；'
            '单一来源待核实（来源为通用页的相关章节，非专属页）。',
    'sources': [SID]},
   {'label': '伯南克暗示的缩减后购债规模', 'value': 65, 'unit': '十亿美元/月', 'year': 2013,
    'comparable_price': False,
    'note': '原文：the Fed could scale back its bond purchases from $85 billion to $65 billion a month；'
            '单一来源待核实。',
    'sources': [SID]},
 ],
 'comparison': (
   '与**实际加息冲击**的区别：缩减恐慌中联邦基金利率**未变**，冲击完全来自预期与期限溢价；'
   '这使它成为"沟通即政策"的教科书案例。'
   '与**1994 年债券大屠杀**的相似处：两者都是长端利率在政策转向预期下急升；'
   '差别在于 2013 年的传导渠道更偏跨境资本流动。'
   '与**2018 年新兴市场动荡**的关系：后者同样由美元利率上行触发，机制一脉相承。'),
 'related': [r for r in ('quantitative-easing', 'monetary-transmission', 'capital-control',
                         'sudden-stop', 'term-premium', 'federal-reserve-act')
             if r in ids],
 'sources': [SID],
 'needs_verification': True,
 'pending_notes': '【续作IO】无专属维基页；内容据「Quantitative easing」页面中 tapering 章节归纳，'
                  '**来源性质为通用页的相关章节**。市场反应的具体幅度（如 10 年期收益率升幅、'
                  '新兴市场货币贬值幅度）待补权威数据后录入。',
}

json.dump(D, open('data/entries/%s.json' % EID, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新建:', EID)

cov = json.load(open('coverage.json', encoding='utf-8'))
if EID not in {e['id'] for e in cov['entries']}:
    cov['entries'].append({'id': EID, 'level': 'L2', 'tier': '重要', 'status': 'written',
                           'source_count': 1, 'needs_verification': 1, 'last_updated': '2026-11-24',
                           'unit': 'U5 21世纪', 'period': '21世纪', 'region': '全球',
                           'crisis_type': '货币'})
    cov['total'] = len(cov['entries'])
    json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total:', cov['total'])
