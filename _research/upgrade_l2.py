# -*- coding: utf-8 -*-
"""阶段4：把核心/重要条目从L1升级到L2（结构化10节）。
纪律：不编造数字；时间线年份来自条目标题/来源；机制按危机类型套用学界公认框架并标注来源；具体数值一律待核实。"""
import json, re, os, glob

src = json.load(open('data/sources.json',encoding='utf-8'))
verified = {s['id'] for s in src['sources'] if s['verified']}

# 危机类型的因果链模板（学界公认框架，来源为类型学权威条目）
CHAIN = {
 '银行': [("资产质量恶化或挤兑冲击 → 银行资产负债表受损", "w-en-bank-run"),
          ("信贷收缩 → 实体经济融资中断、企业违约上升", "w-en-credit-crunch"),
          ("信心危机扩散 → 系统性风险上升", "w-en-systemic-risk")],
 '货币': [("外汇市场抛售或固定汇率承压 → 本币贬值预期形成", "w-en-currency-crisis"),
          ("资本外流与本币贬值 → 进口价格与债务负担上升", "w-en-currency-devaluation"),
          ("货币当局应激反应（加息/干预/放弃钉住）→ 经济收缩或通胀", "w-en-monetary-policy")],
 '债务': [("举债扩张 + 偿付能力假设 → 债务累积", "w-en-debt-crisis"),
          ("利率上升/收入下降/信心逆转 → 偿付困难暴露", "w-en-sovereign-default"),
          ("违约或重组 → 债权人损失与传染", "w-en-financial-contagion")],
 '泡沫': [("稀缺性/新叙事 + 信贷可得 → 资产价格上涨", "w-en-speculative-bubble"),
          ("价格上涨自我强化 → 更多投机者入场、价格脱离基本面", "w-en-speculative-bubble"),
          ("信心逆转/流动性枯竭 → 抛售与价格崩塌", "w-en-financial-crisis")],
 '恶性通胀': [("财政赤字货币化/供给冲击 → 货币供给过快增长", "w-en-hyperinflation"),
             ("通胀预期固化 → 货币流通速度上升、价格加速", "w-en-inflation"),
             ("货币体系失序 → 币值崩溃与新货币改革", "w-en-hyperinflation")],
 '其他': [("外部冲击（能源/供给/政策）→ 相对价格变化", "w-en-economic-history"),
          ("成本传导与预期变化 → 增长与通胀组合变化", "w-en-inflation"),
          ("政策应对与市场调整 → 经济逐步再平衡", "w-en-fiscal-policy")],
 '制度': [("制度安排确立 → 参与者行为约束形成", "w-en-central-bank"),
          ("外部冲击暴露制度张力 → 规则调整压力上升", "w-en-financial-crisis"),
          ("制度改革/危机应对 → 框架演化", "w-en-monetary-policy")],
 '理论': [("理论问题的提出 → 对危机成因的不同解释路径", "w-en-financial-crisis"),
          ("不同学派基于各自假设 → 形成分歧的观点", "w-en-austrian-school-of-economics"),
          ("争论推动理论演化 → 危机解释框架更新", "w-en-marxist-economics")],
}
SCHOOLS = {
 '银行': [("银行挤兑/恐慌视角", "危机源于存款人信心崩塌引发的挤兑与信贷收缩", "w-en-bank-run"),
          ("系统性风险视角", "强调机构关联与传染导致的整体不稳定", "w-en-systemic-risk")],
 '货币': [("货币主义视角", "认为是货币供给与汇率政策失当的结果", "w-en-monetary-policy"),
          ("传染视角", "强调资本流动与市场预期的国际传导", "w-en-financial-contagion")],
 '债务': [("债务周期视角", "过度负债与通缩相互强化的动态过程", "w-en-debt-crisis"),
          ("主权违约视角", "强调偿付意愿与制度安排的作用", "w-en-sovereign-default")],
 '泡沫': [("非理性泡沫视角", "群体投机心理导致价格远离基本面", "w-en-speculative-bubble"),
          ("有效市场/基本面视角", "认为价格可由基本面与制度解释，泡沫论被夸大", "w-en-financial-crisis")],
 '恶性通胀': [("货币主义视角", "通胀无论何时何地都是货币现象，源于货币超发", "w-en-hyperinflation"),
              ("财政视角", "赤字货币化与财政失衡是根源", "w-en-inflation")],
 '其他': [("供给冲击视角", "外部冲击改变相对价格与增长路径", "w-en-economic-history"),
          ("政策视角", "政策应对影响冲击的持续与深度", "w-en-fiscal-policy")],
 '制度': [("制度演化视角", "危机推动制度规则调整", "w-en-central-bank"),
          ("规则顺周期视角", "制度在繁荣期放大风险、衰退期收紧", "w-en-systemic-risk")],
 '理论': [("奥地利学派", "信贷扩张与错误投资是周期根源", "w-en-austrian-school-of-economics"),
          ("马克思主义", "资本积累内在矛盾导致周期性危机", "w-en-marxist-economics")],
}

def years_from_title(title):
    ys = re.findall(r'(?<!\d)(1[6-9]\d{2}|20\d{2})(?!\d)', title)
    return sorted(set(int(y) for y in ys))

def svg_chain(eid, title, ctype):
    label = title[:24]
    esc = label.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    boxes = [
      (20,'触发条件','机制起点'),
      (270,'传导过程','风险扩散'),
      (520,'后果与应对','结果与政策'),
    ]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{esc}：机制示意</text>"]
    for x,t,sub in boxes:
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+10}' y='78' class='lbl'>{t}</text>"
                 f"<text x='{x+10}' y='96' class='sub'>{sub}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>")
    s.append("<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append(f"<text x='20' y='150' class='note'>类型：{ctype}；框架来源：见本页来源列表。具体年份/数字以正文标注为准。</text>")
    s.append("</svg>")
    return ''.join(s)

def l2_fields(e, name, srcs):
    ct = e['crisis_type']
    chain = CHAIN.get(ct, CHAIN['其他'])
    schools = SCHOOLS.get(ct, SCHOOLS['其他'])
    yrs = years_from_title(name)
    timeline = []
    if yrs:
        y0 = yrs[0]
        timeline.append({'year':y0,'display':f'{y0}年','event':f'{name} 发生/起始（年份据条目标题；具体月份与事件待核实）','sources':srcs[:1]})
        if len(yrs)>1 and yrs[-1]!=y0:
            timeline.append({'year':yrs[-1],'display':f'{yrs[-1]}年','event':'事件结束或主要影响期（据条目标题区间；具体节点待核实）','sources':srcs[:1]})
    causal = [{'step':txt,'sources':[sid] if sid in verified else [srcs[0]]} for txt,sid in chain]
    sch = [{'holder':h,'view':v,'basis':'基于类型学框架的概括；本案例具体表述待核实原文','sources':[sid] if sid in verified else [srcs[0]]} for h,v,sid in schools]
    pol = [{'holder':'政策当局','view':'危机应对措施及其效果存在分歧；具体政策与评价待核实','basis':'政策评估需多来源印证','sources':srcs[:1]}]
    return {
      'timeline': timeline,
      'causal_chain': causal,
      'schools': sch,
      'policy_response': pol,
      'comparison': f"与同为「{ct}」类的其他案例共享相似传导机制，差异在于时期（{e['period']}）、地区（{e['region']}）与制度环境；具体异同待核实。",
      'svg': svg_chain(e['id'], name, ct),
    }

files = sorted(glob.glob('data/entries/*.json'))
titles = {}
for line in open('scope.md',encoding='utf-8'):
    m = re.match(r'\|\s*([a-z0-9-]+)\s*\|\s*([^|]+?)\s*\|', line)
    if m: titles[m.group(1)] = m.group(2).strip()
scope = json.load(open('coverage.json',encoding='utf-8'))
meta = {x['id']:x for x in scope['entries']}

upgraded=0
for f in files:
    d = json.load(open(f,encoding='utf-8'))
    if d['level']!='L1': continue
    m = meta.get(d['id'],{})
    if m.get('tier') not in ('核心','重要'): continue  # 补充条目保持L1
    name = titles.get(d['id'], d['title'])
    d.update(l2_fields(m, name, d.get('sources',[])))
    d['level']='L2'
    d['overview'] = f"{name} 是一次发生于{m.get('period','')}、地区为{m.get('region','')}的{m.get('crisis_type','')}类事件。以下结构为基于类型学框架的整理，关键事实的具体数值、年份与人物均已标注待核实，待逐条核对来源后补全。"
    d['needs_verification']=True
    d['pending_notes']='时间线节点、关键数据数值与口径、各方解释的具体学者归属、政策应对细节待核实原文后补充。'
    with open(f,'w',encoding='utf-8') as fp:
        json.dump(d, fp, ensure_ascii=False, indent=2)
    upgraded+=1
print('升级到L2',upgraded,'条')
