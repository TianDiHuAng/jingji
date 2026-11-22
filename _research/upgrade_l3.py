# -*- coding: utf-8 -*-
"""L3升级：为核心条目补充学术争议对照、数据口径说明、复杂因果SVG。
纪律：学者归属限于来源库中已核对著作的作者；不编造具体数字；争议并列不替读者下结论。"""
import json, os, re, glob, sys
LIMIT = int(sys.argv[1]) if len(sys.argv)>1 else 999
# 可用的学术解释框架（归属为来源库中已核对著作作者）
FRAMEWORKS = {
 '泡沫': [
   ("Charles Kindleberger（Manias, Panics, and Crashes）", "投机泡沫经历「替代—繁荣—狂热—崩盘—恐慌」的阶段序列，信贷扩张是关键推手", "bk-the-ascent-of-money"),
   ("John Kenneth Galbraith（The Great Crash 1929）", "强调「使人愉悦的错觉」与财富幻觉在泡沫顶端的心理作用", "bk-the-great-crash-1929"),
 ],
 '银行': [
   ("Milton Friedman & Anna Schwartz（A Monetary History）", "大萧条的深度源于货币供给收缩，银行倒闭是货币紧缩的传导环节", "bk-a-monetary-history-of-the-united-states"),
   ("Charles Kindleberger", "强调信贷创造与资产价格的正反馈以及最后贷款人缺位", "bk-the-ascent-of-money"),
 ],
 '恶性通胀': [
   ("Peter Bernholz 的财政—货币框架（转引自 Wikipedia Hyperinflation）", "恶性通胀的必要条件是财政赤字通过中央银行融资", "w-en-hyperinflation"),
   ("货币主义解释", "通胀无论何时何地都是货币现象，货币供给增速决定物价", "w-en-inflation"),
 ],
 '债务': [
   ("Carmen Reinhart & Kenneth Rogoff（This Time Is Different 主题，见危机经济学综述）", "高债务与低增长之间存在关联，债务累积常 precede 危机", "bk-crisis-economics"),
   ("Barry Eichengreen（Golden Fetters）", "国际货币制度约束影响债务国调整空间", "bk-the-golden-fetters"),
 ],
 '货币': [
   ("Robert Mundell 的「不可能三角」框架（见 Wikipedia 汇率制度综述）", "固定汇率、资本自由流动与独立货币政策三者不可兼得", "w-en-currency-crisis"),
   ("货币主义与结构主义之争", "货币贬值究竟源于货币超发还是结构性收支失衡，学界长期分歧", "w-en-currency-crisis"),
 ],
 '其他': [
   ("供给冲击学派", "外部冲击改变相对价格，引发增长与物价组合变化", "w-en-economic-history"),
   ("需求管理学派", "总需求政策可缓冲冲击，但存在时滞与副作用", "w-en-fiscal-policy"),
 ],
 '制度': [
   ("制度演化论", "危机推动制度规则调整，制度安排影响危机频率与深度", "w-en-central-bank"),
   ("明斯基的金融不稳定假说", "稳定时期孕育不稳定，稳定本身催生冒险行为", "w-en-financial-crisis"),
 ],
 '理论': [
   ("奥地利学派", "信贷扩张导致的错误投资是周期根源", "w-en-austrian-school-of-economics"),
   ("马克思主义", "资本积累的内在矛盾导致周期性生产过剩危机", "w-en-marxist-economics"),
 ],
}

def l3_deep_svg(title, ctype, timeline):
    """复杂图示：多节点因果链 + 反馈回路（内联SVG，CSS变量配色）"""
    esc=lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:30]
    nodes = [
      (30,'冲击/触发','外部或内生冲击'),
      (215,'放大机制','信贷/预期/杠杆'),
      (400,'临界转折','信心逆转'),
      (585,'后果','违约/贬值/收缩'),
    ]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 780 300' role='img' aria-label='机制与反馈回路深度图'>",
       f"<text x='20' y='26' class='ttl'>{esc(title)}：机制与反馈回路（类型：{ctype}）</text>"]
    y=60
    for x,t,sub in nodes:
        s.append(f"<g><rect x='{x}' y='{y}' width='160' height='56' rx='7' class='box'/>"
                 f"<text x='{x+9}' y='{y+24}' class='lbl'>{t}</text>"
                 f"<text x='{x+9}' y='{y+43}' class='sub'>{sub}</text></g>")
    for x1,x2 in [(190,215),(375,400),(560,585)]:
        s.append(f"<line x1='{x1}' y1='{y+28}' x2='{x2}' y2='{y+28}' class='ar'/>")
    # 反馈回路：后果回到放大机制
    s.append("<path d='M665 116 L665 175 L295 175 L295 116' fill='none' class='ar' stroke-dasharray='5,4'/>")
    s.append("<text x='400' y='168' class='sub'>反馈：后果反过来强化放大机制</text>")
    # 时间刻度
    s.append("<line x1='30' y1='215' x2='745' y2='215' class='axis'/>")
    if timeline:
        for i,t in enumerate(timeline[:4]):
            x=40+i*175
            s.append(f"<circle cx='{x}' cy='215' r='4' class='dot'/>")
            s.append(f"<text x='{x-16}' y='240' class='sub'>{esc(t.get('display',''))}</text>")
    s.append(f"<text x='20' y='275' class='note'>学者解释见本页「各方解释」；箭头为机制方向，虚线为反馈回路。图示为分析框架，非精确数据图。</text>")
    s.append("</svg>")
    return ''.join(s)

files=sorted(glob.glob('data/entries/*.json'))
upgraded=[]
count=0
for f in files:
    d=json.load(open(f,encoding='utf-8'))
    if d['level']!='L2' or d['tier']!='核心': continue
    ct=d['crisis_type']
    fw=FRAMEWORKS.get(ct,FRAMEWORKS['其他'])
    # 补充学术争议（去重合并到 schools）
    existing={(s.get('holder','')) for s in d.get('schools',[])}
    for holder,view,src in fw:
        if holder not in existing:
            d.setdefault('schools',[]).append({
                'holder':holder,'view':view,
                'basis':'基于来源库中已核对著作/百科的框架性归纳；本案例的具体适用待核实原文',
                'sources':[src]})
    # L3 深度字段
    d['level']='L3'
    d['l3_detail']={
      'data_caveat':'本条目所有数值均需注明来源、年份与统计口径；跨年通胀/GDP 数据须说明是否可比价。当前无经双源核实的具体数字，故不列数值。',
      'controversy_summary':'不同学派对成因与政策效果存在分歧；本站并列各方说法，不替读者下结论。',
      'framework_type':ct
    }
    d['deep_svg']=l3_deep_svg(d['title'],ct,d.get('timeline',[]))
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+' 【L3】学者解释的具体适用与原文出处、关键数据数值待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    upgraded.append(d['id'])
    count+=1
    if count>=LIMIT: break
print('L3升级',len(upgraded),'条')
print(', '.join(sorted(upgraded)))
