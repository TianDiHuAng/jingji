# -*- coding: utf-8 -*-
"""阶段1 来源核对批次1：Wikipedia en/zh 批量 API 核对标题存在性 + 最后修改年。"""
import urllib.request, urllib.parse, ssl, json, time, re
c = ssl._create_unverified_context()
UA = {'User-Agent':'EconCrisisBot/1.0 (research; contact: local)'}

def api_titles(lang, titles):
    """一次最多50个标题，返回 {title: {'exists':bool,'canonical':str,'touched':str,'missing':bool}}"""
    base = f'https://{lang}.wikipedia.org/w/api.php'
    res = {}
    for i in range(0, len(titles), 40):
        chunk = titles[i:i+40]
        params = {
            'action':'query','format':'json','formatversion':'2',
            'titles':'|'.join(chunk),'prop':'info|pageprops','redirects':'1',
            'inprop':'url'
        }
        url = base + '?' + urllib.parse.urlencode(params)
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers=UA)
                d = json.loads(urllib.request.urlopen(req, timeout=30, context=c).read())
                break
            except Exception as e:
                if attempt==2:
                    print('BATCH FAIL', lang, i, str(e)[:60]); d={'query':{'pages':[]}}
                time.sleep(1)
        norm = {}
        for r in d.get('query',{}).get('redirects',[]):
            norm[r['to']] = r['from']
        for p in d.get('query',{}).get('pages',[]):
            t = p.get('title','')
            key = norm.get(t, t)
            res[key] = {
                'exists': not p.get('missing',False),
                'canonical': t,
                'touched': p.get('touched','')[:4],
                'pageid': p.get('pageid',0)
            }
        time.sleep(0.3)
    return res

EN = [
 "Financial crisis","Tulip mania","South Sea Company","Mississippi Company",
 "Panic of 1792","Panic of 1819","Panic of 1825","Panic of 1837","Panic of 1857",
 "Long Depression","Baring crisis","Panic of 1893","Panic of 1907",
 "Hyperinflation in the Weimar Republic","Wall Street crash of 1929","Great Depression",
 "Hungarian pengő","1973 oil crisis","1979 oil crisis","Latin American debt crisis",
 "Japanese asset price bubble","Black Wednesday","Mexican peso crisis","Dot-com bubble",
 "Argentine economic crisis (1999–2002)","Hyperinflation in Zimbabwe",
 "Subprime mortgage crisis","Great Recession","Euro area crisis","Greek government-debt crisis",
 "Russian financial crisis (2014–2016)","Venezuelan hyperinflation","Turkish economic crisis (2018–present)",
 "Lebanese liquidity crisis","Sri Lankan economic crisis (2019–2024)","Gold standard",
 "Central bank","Bretton Woods system","Business cycle","Austrian school of economics",
 "Marxist economics","Minskyan economics","Banking School","Hyperinflation","Economic history",
 "2008 financial crisis","Federal Reserve","Savings and loan crisis","Bank run",
 "Debt crisis","Currency crisis","Speculative bubble","Financial contagion","Panic of 1901",
 "Shōwa financial crisis","Chinese hyperinflation (1937–1950)","Kindleberger's Manias, Panics, and Crashes",
 "List of financial crises","Panic of 1873","Bengal Bubble of 1769","Copper Panic of 1789",
 "Danish state bankruptcy of 1813","Panic of 1847","Panic of 1866","Paris Bourse crash of 1882",
 "Panic of 1884","Arendal crash","Australian banking crisis of 1893","Panic of 1896",
 "Shanghai rubber stock market crisis","Financial crisis of 1914","Early Soviet hyperinflation",
 "Panic of 1930","Greek hyperinflation (1941–1946)","Kennedy Slide of 1962",
 "1973–1974 stock market crash","Secondary banking crisis","Steel crisis","1976 sterling crisis",
 "Brazilian hyperinflation","Souk Al-Manakh stock market crash","Chilean crisis of 1982",
 "Israeli bank stock crisis","Cameroonian economic crisis","Rhode Island banking crisis",
 "Hyperinflation in Serbia and Montenegro","Venezuelan banking crisis of 1994",
 "October 27, 1997 mini-crash","South American economic crisis of 2002","Stock market downturn of 2002",
 "Chinese stock bubble of 2007","Great Recession in Russia","Post-2008 Irish banking crisis",
 "Blue Monday Crash (2009)","Venezuelan banking crisis of 2009–2010","Energy crisis in Venezuela",
 "Syrian economic crisis (2011–present)","August 2011 stock markets fall",
 "Chinese Banking Liquidity Crisis of 2013","Venezuelan economic crisis","Puerto Rican government-debt crisis",
 "Brexit stock market crash","Ghana banking crisis","Turkish economic crisis","2023 United States banking crisis",
 "Chinese real estate crisis","Pakistani economic crisis (2021–2024)","German economic crisis (2022–present)",
 "Lender of last resort","Deposit insurance","Central bank independence","Too big to fail",
 "Moral hazard","Systemic risk","Credit crunch","Bank failure","Sovereign default",
 "Currency devaluation","Quantitative easing","Fiscal policy","Monetary policy","Inflation",
 "Unemployment","Recession","Depression (economics)","Flash crash","Black Monday (1987)",
 "Asian financial crisis","1997 Asian financial crisis","Dot-com bubble","Initial public offering",
 "Mortgage-backed security","Collateralized debt obligation","Credit default swap","Subprime lending",
 "Quantitative tightening","Business cycle theory","Real business cycle theory","Effective market hypothesis",
]

ZH = [
 "金融危机","经济大萧条","南海泡沫事件","鬱金香狂熱","亚洲金融危机","次贷危机",
 "日本泡沫经济","互联网泡沫","恶性通货膨胀","金本位","中央银行","布雷顿森林体系",
 "欧洲主权债务危机","全球金融危机","经济史","1929年华尔街股灾"," big bang",
 "1929年经济大萧条","石油危机","拉丁美洲债务危机","阿根廷经济危机","俄罗斯金融危机",
 "津巴布韦恶性通胀","委内瑞拉经济危机","货币政策","财政政策","失业","通货膨胀",
 "经济周期","中央银行","存款保险","最后贷款人","明斯基"," asteroid",
]

print('核对英文维基标题:', len(EN))
en_res = api_titles('en', EN)
print('核对中文维基标题:', len(ZH))
zh_res = api_titles('zh', ZH)

json.dump({'en':en_res,'zh':zh_res}, open('_research/verify_wikipedia.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
en_ok = sum(1 for v in en_res.values() if v['exists'])
zh_ok = sum(1 for v in zh_res.values() if v['exists'])
print('英文存在', en_ok, '/', len(EN))
print('中文存在', zh_ok, '/', len(ZH))
print('英文缺失:', [k for k,v in en_res.items() if not v['exists']][:30])
