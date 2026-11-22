# -*- coding: utf-8 -*-
"""阶段1 批次2：Open Library 核对学术著作 + 机构页抓取核对。"""
import urllib.request, urllib.parse, ssl, json, time, re, html
c = ssl._create_unverified_context()
UA = {'User-Agent':'EconCrisisBot/1.0 (research; contact: local)','Accept-Language':'en-US,en;q=0.9'}

def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout, context=c).read()

def ol_search(title, author=None):
    params = {'title':title,'limit':'3','fields':'title,author_name,first_publish_year,key,publisher'}
    if author: params['author'] = author
    url = 'https://openlibrary.org/search.json?' + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            d = json.loads(fetch(url))
            docs = d.get('docs',[])
            if docs:
                x = docs[0]
                return {
                    'found':True,
                    'title':x.get('title',''),
                    'authors':x.get('author_name',[])[:3],
                    'year':x.get('first_publish_year'),
                    'key':x.get('key',''),
                    'query':title
                }
            return {'found':False,'query':title}
        except Exception as e:
            if attempt==2: return {'found':False,'query':title,'error':str(e)[:50]}
            time.sleep(1)

BOOKS = [
 ("Manias, Panics, and Crashes","Charles P. Kindleberger"),
 ("This Time Is Different: Eight Centuries of Financial Folly","Carmen M. Reinhart"),
 ("Golden Fetters: The Gold Standard and the Great Depression","Barry Eichengreen"),
 ("The Great Crash 1929","John Kenneth Galbraith"),
 ("Paper Money and Inflation in the Twentieth Century","Peter Bernholz"),
 ("A Monetary History of the United States","Milton Friedman"),
 ("The Ascent of Money","Niall Ferguson"),
 ("Debt: The First 5000 Years","David Graeber"),
 ("The World Economy: A Millennial Perspective","Angus Maddison"),
 ("Capitalism, Socialism and Democracy","Joseph Schumpeter"),
 ("The General Theory of Employment, Interest and Money","John Maynard Keynes"),
 ("Principles of Economics","Alfred Marshall"),
 ("The Wealth of Nations","Adam Smith"),
 ("Das Kapital","Karl Marx"),
 ("The Theory of Industrial Organization","Jean Tirole"),
 ("Banking on the Brink","Bethany McLean"),
 ("The Big Short","Michael Lewis"),
 ("Too Big to Fail","Andrew Ross Sorkin"),
 ("After the Music Stopped","Alan S. Blinder"),
 ("The End of Theory","Richard Bookstaber"),
 ("Lords of Finance","Liaquat Ahamed"),
 ("The Great Depression","Peter Temin"),
 ("Lessons from the Great Depression","Peter Temin"),
 ("The Golden Fetters","Barry Eichengreen"),
 ("Inflation and Development","Maxwell Fry"),
 ("Hyperinflation and the dynamics of the price level","Frederic Mishkin"),
 ("Manias Panics and Crashes A History of Financial Crises","Charles Kindleberger"),
 ("The Crash of 1929",""),
 ("Black Wednesday",""),
 ("The Euro","Joseph Stiglitz"),
 ("Making the Euro Work",""),
 ("Sovereign Debt and the Financial Crisis",""),
 ("The Asian Financial Crisis",""),
 ("Crisis Economics","Nouriel Roubini"),
 ("Gender and the Economic Crisis",""),
]

print('核对著作',len(BOOKS))
books = []
for title, author in BOOKS:
    r = ol_search(title, author if author else None)
    books.append(r)
    time.sleep(0.25)

json.dump(books, open('_research/verify_books.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
found = sum(1 for b in books if b['found'])
print('找到',found,'/',len(BOOKS))
for b in books:
    if b['found']:
        print('OK', (b.get('year') or '?'), b['title'][:40], '|', ','.join(b['authors'][:1]))

# 机构页核对
SITES = {
 'fed_history':'https://www.federalreservehistory.org/',
 'fed_essay_1907':'https://www.federalreservehistory.org/essays/panic-of-1907',
 'fed_essay_greatdep':'https://www.federalreservehistory.org/essays/great-depression',
 'nber':'https://www.nber.org/',
 'openstax_macro':'https://openstax.org/books/principles-macroeconomics-3e/pages/1-introduction',
 'openstax_money':'https://openstax.org/books/principles-macroeconomics-3e/pages/27-money-and-banking',
 'ecb':'https://www.ecb.europa.eu/home/html/index.en.html',
 'bis':'https://www.bis.org/',
 'worldbank':'https://www.worldbank.org/',
 'imf_data':'https://data.imf.org/',
 'georgetown':'https://www.imf.org/en/Data',
 'fred':'https://fred.stlouisfed.org/',
 'bls':'https://www.bls.gov/',
 'bea':'https://www.bea.gov/',
 'measuringworth':'https://www.measuringworth.com/',
 'ourworldindata':'https://ourworldindata.org/',
}
site_res = {}
for k,u in SITES.items():
    try:
        raw = fetch(u, 20)
        txt = re.sub(r'<[^>]+>',' ', raw.decode('utf-8','ignore'))
        mt = re.search(r'<title[^>]*>(.*?)</title>', raw.decode('utf-8','ignore'), re.S|re.I)
        title = html.unescape(re.sub(r'\s+',' ',mt.group(1))).strip() if mt else ''
        site_res[k] = {'ok':True,'status':200,'bytes':len(raw),'title':title[:100],'url':u}
        print('SITE OK',k,title[:50])
    except Exception as e:
        site_res[k] = {'ok':False,'error':str(e)[:60],'url':u}
        print('SITE ERR',k,str(e)[:45])
    time.sleep(0.2)

json.dump(site_res, open('_research/verify_sites.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
