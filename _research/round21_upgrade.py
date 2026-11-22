# -*- coding: utf-8 -*-
"""轮次21：将3条待联网新条目补足L2结构（据REST摘要原文，不编造）。"""
import json
def svg(title,ct,a='触发/背景',b='传导机制',cc='后果'):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：机制示意（{ct}）</text>"]
    for x,t,sub in [(20,a,'背景'),(270,b,'扩散'),(520,cc,'结果/政策')]:
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='78' class='lbl'>{t}</text><text x='{x+9}' y='96' class='sub'>{sub}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)
DATA={
 'railway-mania':{
  'causal':[('铁路股价格上涨 → 投机者投入更多资金 → 价格进一步上涨（正反馈）','w-en-railway-mania'),
            ('1846年狂热达顶峰（议会当年通过263项设立铁路公司的法案）','w-en-railway-mania'),
            ('股价最终崩盘','w-en-railway-mania')],
  'schools':[('非理性泡沫视角','典型的价格上涨自我强化的投机正反馈，直至崩盘','w-en-railway-mania'),
             ('技术革命/基本面视角','铁路是真实的运输技术革命，投资有基本面基础但被过度放大','w-en-speculative-bubble')],
 },
 'recession-1920-1921':{
  'causal':[('一战结束后14个月、战时需求与财政货币扩张退潮 → 需求与物价回落','w-en-recession-1920-1921'),
            ('1920年1月—1921年7月的急剧通缩型收缩（美英等国）','w-en-recession-1920-1921'),
            ('通缩幅度相对实际产出降幅异常大','w-en-recession-1920-1921')],
  'schools':[('战后调整/货币政策视角','战时扩张退潮与紧缩货币政策导致剧烈通缩','w-en-business-cycle'),
             ('需求冲击视角','总需求骤降带来产出与物价同步下跌','w-en-recession-1920-1921')],
 },
 'bankruptcy-ftx':{
  'causal':[('FTX曾为全球第三大加密交易所、用户超百万；账户存在约80亿美元缺口','w-en-bankruptcy-ftx'),
            ('2022年11月客户提款激增，暴露资金缺口 → 引发挤兑式崩塌','w-en-bankruptcy-ftx'),
            ('FTX于2022年11月启动破产（Bahamas）','w-en-bankruptcy-ftx')],
  'schools':[('挤兑/流动性视角','提款激增暴露资不抵债，类似银行挤兑','w-en-bankruptcy-ftx'),
             ('治理/欺诈视角','客户资金被挪用、治理失效是深层原因（后续司法程序）','w-en-financial-crisis')],
 },
}
for eid,spec in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'; ct=d['crisis_type']
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基摘要归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['policy_response']=[{'holder':'政策/监管当局','view':'应对与评价待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    d['comparison']=f'与同为「{ct}」类案例共享机制，差异在时期、地区与制度环境；具体待核实。'
    d['svg']=svg(d['title'],ct)
    d['needs_verification']=True
    d['pending_notes']='L2：causal_chain/schools据维基摘要；时间线、具体数值与政策细节待核实补充。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→L2')
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']='L2'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage同步')
