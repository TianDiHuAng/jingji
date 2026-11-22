# -*- coding: utf-8 -*-
"""轮次20 DEEPEN-SEMANTIC 第三批：6条L2案例化（据本地维基语料）。"""
import json
SPEC={
 'china-liquidity-2013':{
  'causal':[
   ('外汇市场监管致资金流入下降 + 银行依赖短期同业融资 → 流动性紧张','w-en-chinese-banking-liquidity-crisis-of-2013'),
   ('2013年6月20日上海银行间隔夜拆借利率从常态<3%飙升至30%；央行(PBOC)未注入资金而要求银行盘活存量','w-en-chinese-banking-liquidity-crisis-of-2013'),
   ('恐慌波及黄金与股市；被视为央行有意收紧影子银行/去杠杆的信号','w-en-chinese-banking-liquidity-crisis-of-2013')],
  'schools':[
   ('央行去杠杆视角','央行刻意不救以整肃同业与影子银行风险','w-en-chinese-banking-liquidity-crisis-of-2013'),
   ('流动性错配视角','银行短期同业负债与长期资产错配导致挤兑式紧张','w-en-chinese-banking-liquidity-crisis-of-2013')],
 },
 'russian-1998':{
  'causal':[
   ('生产率下降+维持卢布高固定汇率+财政赤字+第一次车臣战争军费 → 基本面恶化','w-en-russian-1998'),
   ('1998年8月17日俄罗斯政府与央行让卢布贬值并对债务违约','w-en-russian-1998'),
   ('危机重创周边国家经济(传染)','w-en-russian-1998')],
  'schools':[
   ('固定汇率/财政视角','高固定汇率与长期财政赤字不可持续','w-en-russian-1998'),
   ('外部冲击视角','油价与战争成本及亚洲危机外溢加剧恶化','w-en-russian-1998')],
 },
 'ltcm':{
  'causal':[
   ('LTCM采用高杠杆策略(1994成立，董事含Scholes/Merton) → 组合规模与杠杆极高','w-en-ltcm'),
   ('1998年因高杠杆叠加对亚洲/俄罗斯危机的敞口，四个月亏损46亿美元濒临崩溃','w-en-ltcm'),
   ('纽约联储牵头14家银行出资36亿美元救助，防系统性扩散','w-en-ltcm')],
  'schools':[
   ('高杠杆/模型风险视角','小概率事件叠加高杠杆使模型失效、亏损放大','w-en-ltcm'),
   ('系统性风险/最后贷款人视角','因其关联过广，联储协调私人救助避免系统性冲击','w-en-ltcm')],
 },
 'lebanese-liquidity-2019':{
  'causal':[
   ('央行行长以"金融工程"掩盖经济脆弱性，长期维持不可持续安排 → 2019年8月流动性危机全面显现','w-en-lebanese-liquidity-crisis'),
   ('COVID-19、2020贝鲁特港爆炸、俄乌战争与对叙/真主党制裁加剧危机','w-en-lebanese-liquidity-crisis'),
   ('商业银行关闭、储户取款受限(后续出现储户抢银行事件)','w-en-lebanese-liquidity-crisis')],
  'schools':[
   ('央行金融工程/庞氏视角','以高息吸存与会计手法掩盖失衡，实为不可持续的融资结构','w-en-lebanese-liquidity-crisis'),
   ('外部冲击视角','疫情、爆炸与地缘制裁叠加放大既有脆弱性','w-en-lebanese-liquidity-crisis')],
 },
 'bank-crisis-2023':{
  'causal':[
   ('利率上升使银行持有的国债组合大幅浮亏；Silvergate/Signature 加密敞口暴露','w-en-2023-united-states-banking-crisis'),
   ('硅谷银行(SVB)出售债券亏损引发挤兑，2023年3月10日被接管；3月12日签名银行被关闭','w-en-2023-united-states-banking-crisis'),
   ('美联储贴现窗口放贷约1500亿美元；5月1日第一共和银行被FDIC关闭并售予摩根大通','w-en-2023-united-states-banking-crisis')],
  'schools':[
   ('利率风险/资产负债错配视角','加息使长期债券浮亏，短负债长资产错配致偿付危机','w-en-2023-united-states-banking-crisis'),
   ('挤兑/传染(数字时代)视角','社交媒体加速存款挤兑，信心传染迅速','w-en-2023-united-states-banking-crisis')],
 },
 'pakistan-crisis-2021':{
  'causal':[
   ('2021年末燃料短缺与通胀飙升 → 国际收支与外部融资压力上升','w-en-pakistani-economic-crisis-2021-2024'),
   ('2022年洪灾造成约300亿美元损失；通胀2022年6月创历史高位','w-en-pakistani-economic-crisis-2021-2024'),
   ('2023年初和平时期首次濒临主权违约，后靠IMF等外部支持缓解','w-en-pakistani-economic-crisis-2021-2024')],
  'schools':[
   ('国际收支/外部融资视角','长期外部失衡与储备不足导致违约风险','w-en-pakistani-economic-crisis-2021-2024'),
   ('外部冲击视角','洪灾与全球能源/粮价上涨放大脆弱性','w-en-pakistani-economic-crisis-2021-2024')],
 },
}
for eid,spec in SPEC.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['pending_notes']=d.get('pending_notes','')+' 【轮次20】causal_chain/schools案例化（据本地维基语料）。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'案例化 causal',len(d['causal_chain']),'schools',len(d['schools']))
