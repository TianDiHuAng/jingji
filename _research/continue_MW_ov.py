import json
ADD={
'structural-adjustment':'。这些政策通常围绕扩大私有化、放开贸易与外国投资、平衡政府赤字展开，所附的条件性条款因其对社会部门的影响而受到批评；批评者认为对穷国的财务压力近乎胁迫，使其别无选择。1990年代末以来，世界银行等支持者开始以“减贫”来表述结构改革的目标。',
'asset-liability-mismatch':'。“原罪”一词由艾肯格林（Barry Eichengreen）、豪斯曼（Ricardo Hausmann）与帕尼扎（Ugo Panizza）提出，指多数国家无法以本币在境外借款；他们2002年的研究认为，宏观政策与制度的弱点与原罪在统计上无关，唯一稳健的决定因素是国家规模。',
}
for eid,t in ADD.items():
    p=f'data/entries/{eid}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    ov=e['overview'].rstrip('。');e['overview']=ov+t
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s)
    print(eid,len(e['overview']))
