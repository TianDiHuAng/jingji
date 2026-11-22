# -*- coding: utf-8 -*-
"""阶段1：合并三批核对结果，生成 data/sources.json（≥80条，逐条 verified 标注）。"""
import json, re, os, urllib.parse

W = json.load(open('_research/verify_wikipedia.json',encoding='utf-8'))
B = json.load(open('_research/verify_books.json',encoding='utf-8')) if os.path.exists('_research/verify_books.json') else []
S = json.load(open('_research/verify_sites.json',encoding='utf-8')) if os.path.exists('_research/verify_sites.json') else {}

def slug(s):
    s = re.sub(r'[^a-z0-9]+','-', s.lower()).strip('-')
    return s[:48] or 'src'

def slug_zh(s, idx):
    """中文标题无 ASCII，用 zh-<序号> 保证 id 合法且唯一"""
    return f'zh-{idx:03d}'

sources = []
seen = set()

def add(sid, title, author, year, typ, url, verified, note, url2=None):
    if sid in seen: return
    seen.add(sid)
    sources.append({
        'id':sid,'title':title,'author':author,'year':year,'type':typ,
        'url':url,'url2':url2,'verified':verified,'note':note,
        'link_ok': True if verified else None
    })

# --- 英文维基：API 确认存在 → verified=true；标题与最后修改年由 API 返回 ---
for title, info in W['en'].items():
    if not info['exists']: continue
    canon = info['canonical']
    enc = urllib.parse.quote(canon.replace(' ','_'))
    url = f'https://en.wikipedia.org/wiki/{enc}'
    year = info.get('touched','') or None
    add('w-en-'+slug(title), canon, 'Wikipedia contributors', year, '权威百科', url, True,
        'Wikipedia API 核对：页面存在（pageid=%s），标题与最后修改时间由 API 返回' % info.get('pageid',0))

# --- 中文维基 ---
for zidx, (title, info) in enumerate([x for x in W['zh'].items() if x[1]['exists']], 1):
    canon = info['canonical']
    if '小行星' in canon or 'asteroid' in canon.lower():  # 核对关键词误命中，剔除
        continue
    enc = urllib.parse.quote(canon.replace(' ','_'))
    url = f'https://zh.wikipedia.org/wiki/{enc}'
    add('w-'+slug_zh(canon,zidx), canon, '维基百科贡献者', info.get('touched','') or None, '权威百科', url, True,
        '中文维基 API 核对：页面存在（pageid=%s）' % info.get('pageid',0))

# --- 学术著作：Open Library 找到记录 → verified=true（作者/年份来自馆藏记录） ---
for b in B:
    if not b.get('found'): continue
    title = b['title']; author = ', '.join(b.get('authors',[])[:2]) or '机构/编者'
    year = b.get('year')
    key = b.get('key','')
    url = 'https://openlibrary.org'+key if key else 'https://openlibrary.org/search?q='+urllib.parse.quote(b.get('query',title))
    add('bk-'+slug(b.get('query',title)), title, author, year, '学术著作', url, True,
        'Open Library 馆藏记录核对：标题/作者/首版年由 API 返回')

# --- 官方机构页：抓取成功 → verified=true ---
ORG_AUTHOR = {
 'fed_history':'Federal Reserve Bank of St. Louis','fed_essay_1907':'Federal Reserve History',
 'fed_essay_greatdep':'Federal Reserve History','nber':'National Bureau of Economic Research',
 'openstax_macro':'OpenStax','openstax_money':'OpenStax','ecb':'European Central Bank',
 'bis':'Bank for International Settlements','worldbank':'World Bank','imf_data':'IMF',
 'georgetown':'IMF','fred':'Federal Reserve Bank of St. Louis','bls':'U.S. Bureau of Labor Statistics',
 'bea':'U.S. Bureau of Economic Analysis','measuringworth':'MeasuringWorth',
 'ourworldindata':'Our World in Data',
}
for k, v in S.items():
    if not v.get('ok'): continue
    title = v.get('title') or k
    add('org-'+slug(k), title, ORG_AUTHOR.get(k,'机构网站'), None, '官方机构', v['url'], True,
        '机构页 HTTP 200 抓取核对：标题 "%s"（%d 字节）' % (title[:50], v.get('bytes',0)))

# --- 反爬/不可达的权威站点：URL 已知但本机无法打开核对 → verified=false ---
BLOCKED = [
 ("britannica-financial-crisis","Financial crisis | Money & Finance","Encyclopaedia Britannica",
  None,"权威百科","https://www.britannica.com/money/financial-crisis","HTTP 403 反爬，无法打开核对标题/年份"),
 ("imf-publications","IMF Publications","International Monetary Fund",
  None,"官方机构","https://www.imf.org/en/Publications","HTTP 403 反爬，无法打开核对"),
 ("investopedia-financial-crisis","Financial Crisis Definition","Investopedia",
  None,"权威百科","https://www.investopedia.com/terms/f/financial-crisis.asp","HTTP 403 反爬，无法打开核对"),
 ("baike-financial-crisis","金融危机","百度百科",
  None,"权威百科","https://baike.baidu.com/item/金融危机","HTTP 403 反爬，无法打开核对"),
 ("bls","U.S. Bureau of Labor Statistics","U.S. Bureau of Labor Statistics",
  None,"官方机构","https://www.bls.gov/","HTTP 403 反爬，无法打开核对"),
]
for sid,title,author,year,typ,url,why in BLOCKED:
    if sid in seen: continue
    sources.append({'id':sid,'title':title,'author':author,'year':year,'type':typ,
        'url':url,'url2':None,'verified':False,'note':why,'link_ok':'blocked'})
    seen.add(sid)

os.makedirs('data', exist_ok=True)
json.dump({'generated':'2026-11-22','count':len(sources),'sources':sources},
          open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

from collections import Counter
print('sources.json 写入', len(sources), '条')
print('类型分布:', dict(Counter(x['type'] for x in sources)))
print('verified=true:', sum(1 for x in sources if x['verified']))
print('verified=false:', sum(1 for x in sources if not x['verified']))
