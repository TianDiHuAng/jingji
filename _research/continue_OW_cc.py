# -*- coding: utf-8 -*-
"""续作OW：为 4 条缺 causal_chain 的案例补因果链（据各自正文机制与已引来源，不引入新事实）。"""
import json

CC = {
 'bank-holiday': [
   {'step':'1933-02-14 起密歇根州率先宣布 8 天银行假日，其他州相继跟进 → 挤兑从一州蔓延至全国','sources':['w-en-bank-holiday']},
   {'step':'罗斯福于 1933 年 3 月宣布全国银行假日，暂停全部银行营业以止住挤兑','sources':['w-en-bank-holiday']},
   {'step':'国会通过《紧急银行法》(EBRA, 1933-03-09)，授权美联储增发钞票、银行经审核后择优复业','sources':['w-en-bank-holiday']},
 ],
 'recession-1960-1961': [
   {'step':'美联储自 1958 年起收紧货币、叠加财政紧缩 → 总需求回落','sources':['w-en-recession-1960-1961']},
   {'step':'1960-04—1961-02 衰退，GDP 下降约 1.4 个百分点，历时约 10 个月（NBER 判定）','sources':['org-nber']},
   {'step':'此后开启 1961—1969 年美国史上第三长扩张期','sources':['w-en-recession-1960-1961']},
 ],
 'recession-1969-1970': [
   {'step':'通胀已在上升（充分就业下赤字支出扩大）→ 政策转向紧缩','sources':['w-en-recession-1969-1970']},
   {'step':'货币与财政双紧缩 → 1969-12—1970-11 温和衰退，GDP 仅降约 0.6 个百分点，历时约 11 个月（NBER 判定）','sources':['org-nber']},
 ],
 'taper-tantrum': [
   {'step':'2013 年 FOMC 仅暗示将缩减(taper)资产购买、尚未真正收紧 → 市场预期长期利率上行','sources':['w-en-quantitative-easing']},
   {'step':'全球债券收益率急升 → 新兴市场资本外流、货币贬值','sources':['w-en-quantitative-easing']},
 ],
}
for eid, cc in CC.items():
    p='data/entries/%s.json'%eid; d=json.load(open(p,encoding='utf-8'))
    if d.get('causal_chain'):
        print(eid,'已有 causal_chain，跳过'); continue
    d['causal_chain']=cc
    d['pending_notes']=(d.get('pending_notes','')+' 【续作OW｜round158】据正文机制与已引来源补 causal_chain。')
    json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'causal_chain 已补（%d 步）'%len(cc))
