import json
ADD={
'informal-economy':'意大利自1987年起把非正规活动的估算计入GDP，估计使其GDP增加约18%；2014年若干欧洲国家按国际核算标准把卖淫与毒品交易计入官方GDP，使GDP增加3%至7%。“非正规部门”一词的最初用法归于刘易斯（W. Arthur Lewis）1955年提出的经济发展模型。',
'black-market':'黑市不同于灰色市场（商品通过合法但非官方、未经授权的渠道流通）与白色市场（交易合法且公开）；现金因难以追踪而仍是非法交易的首选媒介，常见动机包括走私、逃税或规避监管，以及规避价格管制与配给。',
'sovereign-default':'政府有时通过通胀或货币贬值摆脱部分实际债务负担，这并非通常意义的违约，因为债务仍被兑付，只是所用货币实际价值降低；当市场担心政府无法偿债而要求大幅提高利率时，即被称为主权债务危机，依赖短期债券融资的政府尤其脆弱。',
'financialization':'密歇根大学的克里普纳（Greta Krippner）把金融化定义为一种“利润越来越多地通过金融渠道而非贸易与商品生产获得”的积累模式；也有学者主张更窄的用法，即股东价值作为公司治理模式的兴起，或资本市场型金融体系相对银行主导型体系的上升。',
'interest-rate-parity':'利率平价的两个核心假设是资本自由流动与本外币资产完全可替代；该条件并不总是成立，这为抛补利率套利留下了获取无风险利润的机会。',
}
for eid,t in ADD.items():
    p=f'data/entries/{eid}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    e['overview']=e['overview'].rstrip('。')+'。'+t
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s)
    print(eid,len(e['overview']))
