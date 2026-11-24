# -*- coding: utf-8 -*-
"""续作CQ：新增中世纪晚期危机(U1)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20,270,520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

entry = {
 'id': 'crisis-late-middle-ages',
 'title': '中世纪晚期危机(14世纪)',
 'level': 'L2', 'tier': '重要',
 'unit': 'U1 早期—17世纪', 'period': '早期—17世纪', 'region': '欧洲', 'crisis_type': '其他',
 'one_line': '14世纪欧洲人口、政治与宗教的全面危机：大饥荒与黑死病使人口减少10%—15%，至约1500年才恢复。',
 'overview': ('中世纪晚期危机是欧洲中世纪晚期一系列事件的总称，涉及**大范围人口崩溃、政治动荡与宗教剧变**。'
   '这些事件共同终结了欧洲数百年相对稳定的时期，并重塑了区域社会结构；'
   '该危机期与区域气候由"中世纪暖期"转向"小冰期"相吻合。'
   '核心事件是 **1315—1317年的大饥荒** 与 **1347—1351年的黑死病**，二者造成极高死亡率——'
   '大饥荒堪称欧洲史上最严重者之一，**可能使人口减少10%以上**；'
   '饥荒与瘟疫（并被战争加剧）合计造成欧洲人口约 **10%—15%** 的死亡；'
   '黑死病在疫病存在的地区致死率约 **30%—60%**。'
   '人口直到 **约1500年** 才恢复到危机前水平。'
   '局部数据可反映冲击的烈度：法兰西圣阿努尔夫修道院周边葡萄园产量到 **1317年下降达 80%**；'
   '**1319—20年英格兰与威尔士** 庄园账册记录的牛群损失达 **62%**。'
   '同期战争与起义频发（百年战争、玫瑰战争、阿尔马尼亚克-勃艮第内战、拜占庭-奥斯曼战争等），'
   '天主教会经历西方教会大分裂，神圣罗马帝国在大空位期(1247—1273)后中央权威衰落。'
   '该案例是"人口-气候-疾病-战争"复合冲击的经典样本。具体归因权重待核实。'),
 'timeline': [
   {'year':1315,'display':'1315—1317年','event':'大饥荒，欧洲人口可能减少10%以上','sources':['w-en-crisis-late-middle-ages']},
   {'year':1317,'display':'1317年','event':'法兰西圣阿努尔夫修道院周边葡萄产量下降达80%','sources':['w-en-crisis-late-middle-ages']},
   {'year':1320,'display':'1319—1320年','event':'英格兰与威尔士庄园牛群损失62%','sources':['w-en-crisis-late-middle-ages']},
   {'year':1347,'display':'1347—1351年','event':'黑死病，疫区致死率约30%—60%','sources':['w-en-crisis-late-middle-ages']},
   {'year':1500,'display':'约1500年','event':'欧洲人口才恢复至危机前水平','sources':['w-en-crisis-late-middle-ages']},
 ],
 'causal_chain': [
   {'step':'气候转向小冰期 → 农业减产与饥荒（1315—1317）','sources':['w-en-crisis-late-middle-ages']},
   {'step':'人口营养不良与流动 → 黑死病(1347—1351)致死率30%—60%','sources':['w-en-crisis-late-middle-ages']},
   {'step':'人口锐减 → 劳动力稀缺、地租与工资关系重构；战争与宗教分裂叠加','sources':['w-en-crisis-late-middle-ages']},
 ],
 'key_data': [
   {'label':'大饥荒人口损失(下界)','value':-10,'unit':'%（可能超过10%）','year':1317,'comparable_price':False,
    'note':'原文：It was arguably the worst in European history, possibly reducing the population by more than 10%；单一来源待核实。','sources':['w-en-crisis-late-middle-ages']},
   {'label':'饥荒与瘟疫合计致死比例(下界)','value':10,'unit':'%（欧洲人口，10%—15%区间下界）','year':1351,'comparable_price':False,
    'note':'原文：resulted in the death of an estimated 10% to 15% of Europe\'s population；单一来源待核实。','sources':['w-en-crisis-late-middle-ages']},
   {'label':'饥荒与瘟疫合计致死比例(上界)','value':15,'unit':'%（10%—15%区间上界）','year':1351,'comparable_price':False,
    'note':'原文：10% to 15% of Europe\'s population；单一来源待核实。','sources':['w-en-crisis-late-middle-ages']},
   {'label':'黑死病在疫区致死率(上界)','value':60,'unit':'%（30%—60%区间上界）','year':1351,'comparable_price':False,
    'note':'原文：It was fatal to an estimated 30% to 60% of the population where the disease was present；单一来源待核实。','sources':['w-en-crisis-late-middle-ages']},
   {'label':'圣阿努尔夫修道院周边葡萄产量降幅(1317)','value':-80,'unit':'%（达）','year':1317,'comparable_price':False,
    'note':'原文：The wine production from the vineyards surrounding the Abbey of Saint-Arnould in France decreased as much as 80% by 1317；单一来源待核实。','sources':['w-en-crisis-late-middle-ages']},
   {'label':'英格兰与威尔士牛群损失(1319—20)','value':-62,'unit':'%','year':1320,'comparable_price':False,
    'note':'原文：Manorial accounts of cattle populations in the year 1319–20 mention a 62% loss in England and Wales alone；单一来源待核实。','sources':['w-en-crisis-late-middle-ages']},
 ],
 'schools': [
   {'holder':'马尔萨斯式视角','view':'人口相对资源过剩使危机成为"正人口学"调整','basis':'据饥荒与人口数据归纳；具体争论待核实','sources':['w-en-crisis-late-middle-ages']},
   {'holder':'外生冲击视角','view':'气候转折与病原体是主导变量，人口压力是背景','basis':'据气候与小冰期记载归纳','sources':['w-en-crisis-late-middle-ages']},
 ],
 'policy_response': [],
 'comparison': ('与其后以货币与金融为核心的危机不同，中世纪晚期危机是**实体冲击**（气候、疾病、战争）主导的复合危机；'
   '但人口锐减带来的劳动力稀缺与地租下降，长期改变了欧洲的要素价格结构。'
   '与1340年代佛罗伦萨银行业崩溃（见 bardi-family）同期发生，二者性质不同但相互叠加。具体异同待核实。'),
 'svg': svg('中世纪晚期危机', ['气候转冷→饥荒', '黑死病(致死30-60%)', '人口至1500年才恢复']),
 'sources': ['w-en-crisis-late-middle-ages'],
 'related': [],
 'needs_verification': True,
 'pending_notes': 'L2：据维基全文；单源待核实（原条目仅一个来源，属"其他"类复合危机，非金融事件）。【续作CQ】'
}

json.dump(entry, open('data/entries/crisis-late-middle-ages.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('新增 crisis-late-middle-ages')

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
if 'w-en-crisis-late-middle-ages' not in ex:
    meta = json.load(open('_research/r99_data.json', encoding='utf-8'))['crisis-late-middle-ages']
    sd['sources'].append({'id':'w-en-crisis-late-middle-ages','title':meta['title'],
      'author':'Wikipedia contributors','year':'2026','type':'权威百科',
      'url':'https://en.wikipedia.org/wiki/Crisis_of_the_late_Middle_Ages','url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia API(full extract)核对(本会话抓取)'})
    sd['count']=len(sd['sources'])
    json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增来源 w-en-crisis-late-middle-ages')
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
if entry['id'] not in {e['id'] for e in cov['entries']}:
    cov['entries'].append({'id':entry['id'],'level':'L2','tier':'重要','status':'written',
      'source_count':1,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':entry['unit'],'period':entry['period'],'region':entry['region'],'crisis_type':entry['crisis_type']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
