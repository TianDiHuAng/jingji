# -*- coding: utf-8 -*-
"""续作：用库内未使用的verified来源新增更多经济学概念(L2)。"""
import json
def svg(t,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(t)}：概念示意</text>"]
    for x,lb in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)
D=[
 ('herd-behavior','羊群行为(群体行为)','理论',
  '个体在群体中模仿他人决策、放弃独立判断的行为倾向。',
  '羊群行为指个体放弃自身信息、跟随大众决策的倾向。在金融市场中可放大追涨杀跌与泡沫/恐慌，是行为金融学的重要概念。其成因涉及信息不对称、声誉与从众心理。具体研究待核实。',
  [('信息不对称/不确定 → 个体参考他人行为','w-en-herd-behavior'),('模仿与从众 → 行为趋同、放大价格波动','w-en-herd-behavior'),('追涨杀跌 → 泡沫或恐慌','w-en-speculative-bubble')],
  [('行为金融视角','从众与信息瀑布放大市场波动','w-en-herd-behavior'),('有效市场视角','认为群体行为多可被基本面解释','w-en-speculative-bubble')],
  ['w-en-herd-behavior','w-en-speculative-bubble']),
 ('depression-economics','经济萧条','理论',
  '持续且严重的产出下降与高失业，比一般衰退更深更久。',
  '经济萧条(economic depression)指长期、深度的经济收缩与高失业，显著严重于一般衰退（如1929大萧条）。界定标准并无统一阈值，学界多以持续时间与深度判断。具体划分待核实。',
  [('需求骤降/金融体系失灵 → 产出深度下滑','w-en-depression-economics'),('失业高企、通缩与债务负担 → 自我强化','w-en-great-depression'),('长期低于潜在产出','w-en-depression-economics')],
  [('凯恩斯视角','需求不足致长期萧条，需强力干预','w-en-great-depression'),('货币视角','货币收缩加深萧条','w-en-monetary-policy')],
  ['w-en-depression-economics','w-en-great-depression']),
 ('economic-recession','经济衰退','理论',
  '经济活动普遍、持续数月的显著下降（常以连续两季GDP负增长为经验标准）。',
  '经济衰退(recession)指总产出、就业与收入普遍且持续数月下降的时期。常用"连续两个季度GDP负增长"作经验判别，但正式判定由专门机构（如美国NBER）依多指标综合。具体标准待核实。',
  [('总需求/供给冲击 → 产出与就业下降','w-en-recession'),('收入与消费走弱 → 衰退自我强化','w-en-business-cycle'),('政策刺激 → 复苏','w-en-fiscal-policy')],
  [('需求管理视角','可用财政货币缓释衰退','w-en-fiscal-policy'),('周期视角','衰退是经济周期的一部分','w-en-business-cycle')],
  ['w-en-recession','w-en-business-cycle']),
 ('classical-economics','古典经济学','理论',
  '18—19世纪以市场自发调节、劳动价值论等为特征的经济学传统（斯密、李嘉图、马歇尔等）。',
  '古典经济学是18世纪后期至19世纪的经济学传统，以亚当·斯密《国富论》为奠基，强调分工、市场与"看不见的手"的自发协调，并发展出劳动价值论等。后经马歇尔等综合为新古典经济学。具体论述待核实。',
  [('分工与市场交换 → 提高生产率与国民财富','bk-the-wealth-of-nations'),('价格与"看不见的手" → 自发协调资源配置','bk-the-wealth-of-nations'),('边际分析与均衡 → 新古典综合','bk-principles-of-economics')],
  [('古典/自由市场视角','市场能自发协调、政府角色有限','bk-the-wealth-of-nations'),('凯恩斯批判视角','市场不能自动出清，需干预','bk-principles-of-economics')],
  ['bk-the-wealth-of-nations','bk-principles-of-economics']),
 ('long-depression','长期萧条(1873–1896)','其他',
  '1873年后欧美持续约二十年的价格下跌与增长放缓时期。',
  '长期萧条(Long Depression)指1873年恐慌之后欧美持续约二十年的通货紧缩与增长放缓（约1873—1896年）。关于其是否名副其实存在争论（部分观点仅为价格下跌而实际产出增长）。具体界定待核实。',
  [('1873年恐慌后 → 长期价格下跌与增长放缓','w-en-long-depression'),('金本位下的通缩压力','w-en-gold-standard'),('产出与就业的结构性调整','w-en-panic-of-1873')],
  [('通缩/金本位视角','金本位与通缩延长了低迷','w-en-gold-standard'),('修正视角','或主要是价格下跌而非真实产出萎缩','w-en-long-depression')],
  ['w-en-long-depression','w-en-panic-of-1873']),
]
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    entry={'id':eid,'title':title,'level':'L2','tier':'重要','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat,
      'one_line':ol,'overview':ov,'timeline':[],
      'causal_chain':[{'step':st,'sources':[s]} for st,s in causal],'key_data':[],
      'schools':[{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[s]} for h,v,s in schools],
      'policy_response':[],'comparison':'经济学/经济史概念，与其他概念互补；具体争论待核实。',
      'svg':svg(title,[causal[0][0][:12],causal[1][0][:12],causal[2][0][:12]]),
      'sources':srcs,'related':[],'needs_verification':True,
      'pending_notes':'概念条目：定义/机理据来源与标准口径，具体数据待核实。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('新增',eid)
cov=json.load(open('coverage.json',encoding='utf-8')); have={e['id'] for e in cov['entries']}
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    if eid in have: continue
    cov['entries'].append({'id':eid,'level':'L2','tier':'重要','status':'written','source_count':len(srcs),'needs_verification':1,'last_updated':'2026-11-23','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat})
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('total',cov['total'])
