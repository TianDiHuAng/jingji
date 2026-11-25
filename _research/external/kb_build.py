# Kindleberger 阶段标注：只给条目时间线中已有事件标阶段（编者归纳），无法判断的留空
import json
S=['替代性冲击','繁荣（信贷扩张）','狂热','困境','厌恶（崩溃）']
A,B,C,D,E=S
M={'tulip-mania-1637':{0:A,1:B,2:C,3:E},'south-sea-bubble-1720':{1:A,2:C,4:E},
'dotcom-bubble-2000':{0:A,1:C,3:E},'japan-asset-bubble-1990':{0:A,1:B,2:B,3:E},
'hainan-property-bubble-1992':{0:A,1:C,2:E},'taiwan-bubble':{1:C,2:E},'railway-mania':{0:B,1:E},
'panic-1825':{0:C,1:E},'encilhamento-1890':{1:B,2:E},'albania-pyramid-1997':{0:C,1:E},
'bengal-bubble-1769':{0:C,1:E},'wall-street-1929':{0:D,1:E,2:E,3:E},'us-video-game-crash-1983':{0:D,1:E},
'chinese-stock-bubble-2007':{0:C,1:E},'shanghai-rubber-1910':{0:C,1:E}}
rows=[]
for k,m in M.items():
    e=json.load(open(f'data/entries/{k}.json',encoding='utf-8'));tl=e['timeline']
    st={s:[] for s in S}
    for i,s in m.items():
        t=tl[i];st[s].append({'year':t.get('year'),'event':t.get('event') or t.get('text','')})
    rows.append({'id':k,'stages':st})
json.dump({'stages':S,'note':'阶段划分为本库编者依据 Kindleberger《疯狂、惊恐和崩溃》五阶段框架所作的归纳，不是来源原文；事件文字取自各条目时间线，无法判断的阶段留空。','rows':rows},open('data/kindleberger.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(rows))
