# -*- coding: utf-8 -*-
"""审计维基全文缓存是否放错页面（只读，不改数据）。
判据：①缓存头部无来源行或来源不在条目 sources 中；②同一页面被多个条目共用（多为通用页面）。"""
import json,glob,os,re,hashlib,collections
E={json.load(open(f,encoding='utf-8'))['id']:json.load(open(f,encoding='utf-8')) for f in glob.glob('data/entries/*.json')}
info={};byhash=collections.defaultdict(list);bysrc=collections.defaultdict(list)
for i,e in E.items():
    p=f'_research/wiki_full/{i}.txt'
    if not os.path.exists(p): continue
    t=open(p,encoding='utf-8').read();lines=t.split('\n',2)
    title=lines[0][2:].strip() if lines[0].startswith('# ') else None
    m=re.match(r'# source (\S+)',lines[1]) if len(lines)>1 else None
    src=m.group(1) if m else None
    h=hashlib.md5(t.split('\n',2)[-1][:5000].encode()).hexdigest()
    info[i]=(title,src);byhash[h].append(i)
    if src: bysrc[src].append(i)
flag=collections.defaultdict(list)
for i,(title,src) in info.items():
    if not src: flag[i].append('无来源头')
    elif src not in E[i]['sources']: flag[i].append(f'来源{src}不在条目sources')
for h,ids in byhash.items():
    if len(ids)>1:
        for i in ids: flag[i].append('与'+','.join(x for x in ids if x!=i)+'缓存相同')
for s,ids in bysrc.items():
    if len(ids)>1:
        for i in ids: flag[i].append(f'来源{s}被{len(ids)}个条目缓存共用')
print(f'缓存 {len(info)} 个，可疑 {len(flag)} 个')
for i in sorted(flag): print(i,'|',info[i][0],'|',info[i][1],'|','；'.join(flag[i]))
