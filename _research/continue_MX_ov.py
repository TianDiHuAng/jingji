import json
ADD={
'lloyds':'劳合社的业务起源于海上保险，可追溯到约1689年爱德华·劳埃德（Edward Lloyd）在塔街开设的咖啡馆；它是依据《1871年劳合社法》及其后议会法案设立的法人团体，成员既有公司也有个人（传统上称为 Names）。',
'value-at-risk':'VaR 主要用于风险管理、财务控制、财务报告与计算监管资本，但它本身是一种有争议的风险管理工具；与之相关的概念包括回溯测试、压力测试与预期损失（expected shortfall）。',
'devaluation':'与贬值相反、使本币变贵的官方调整称为升值（revaluation）；只改变货币面值而不降低汇率属于货币重新定值（redenomination），不属于贬值。',
'speculative-bubble':'“泡沫”一词用于金融危机，起源于1711—1720年英国南海泡沫；泡沫通常只有在破裂、价格崩跌之后才能被确定地识别。',
'procyclicality':'在财政政策语境中，顺周期财政政策指扩张期增支减税、衰退期减支增税，逆周期财政政策则相反。',
}
FIX={'stagflation':('后该现象获得更广泛关注有经济学家','后该现象获得更广泛关注。有经济学家')}
for eid in set(ADD)|set(FIX):
    p=f'data/entries/{eid}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    ov=e['overview']
    if eid in FIX: a,b=FIX[eid];assert a in ov;ov=ov.replace(a,b)
    if eid in ADD: ov=ov.rstrip('。')+'。'+ADD[eid]
    e['overview']=ov
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s)
    print(eid,len(ov))
