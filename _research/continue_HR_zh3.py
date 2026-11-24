# -*- coding: utf-8 -*-
"""续作HR：为剩余 29 个单来源条目再试中文维基（多候选标题）。"""
import json
import ssl
import time
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}

CAND = {
 'actuarial': ['精算学', '精算師'],
 'bullion': ['金條', '貴金屬'],
 'buyback': ['股份回購', '股票回購'],
 'common-pool': ['公共池塘资源', '共有資源'],
 'convergence': ['經濟趨同', '收敛'],
 'counterparty-risk': ['交易對手風險', '信用風險'],
 'deindustrialization': ['去工業化'],
 'demand': ['需求', '需求曲線'],
 'dividend': ['股息', '股利'],
 'effective-demand': ['有效需求'],
 'eurodollar': ['歐洲美元'],
 'expectations': ['預期 (經濟學)', '理性预期'],
 'fractional-reserve': ['部分准备金银行', '存款準備金'],
 'inequality': ['贫富差距', '收入分配'],
 'junk-bond': ['垃圾债券', '高收益債券'],
 'labour-market': ['勞動市場', '劳动力市场'],
 'modigliani-miller': ['莫迪利安尼-米勒定理', 'MM理論'],
 'payment-system': ['支付系統'],
 'population': ['人口'],
 'property-rights': ['產權', '財產權'],
 'proprietary-trading': ['自營交易'],
 'recession': ['经济衰退', '衰退 (經濟)'],
 'specialization': ['分工', '專業化'],
 'subordination': ['次級債', '次级贷款'],
 'tax-incidence': ['稅負轉嫁', '税收归宿'],
 'toxic-assets': ['不良資產', '有毒资产'],
 'utility': ['效用 (經濟學)', '效用'],
}

out = []
for eid, zh_list in CAND.items():
    for zh in zh_list:
        api = ('https://zh.wikipedia.org/w/api.php?action=query&format=json&prop=extracts'
               '&exintro=1&explaintext=1&redirects=1&titles=' + urllib.parse.quote(zh))
        try:
            d = json.loads(urllib.request.urlopen(
                urllib.request.Request(api, headers=HDR), timeout=12, context=CTX).read())
            for _, pv in d.get('query', {}).get('pages', {}).items():
                txt = pv.get('extract', '') or ''
                real = pv.get('title', '') or ''
                if len(txt) > 250 and '可能指' not in txt[:60] and '可以指' not in txt[:60]:
                    out.append((eid, real, zh, len(txt)))
                    print('%-24s → zh《%-14s》(查:%s) %d字符' % (eid, real[:14], zh, len(txt)))
                    break
        except Exception:
            pass
        time.sleep(0.25)

print('\n命中:', len(out))
json.dump(out, open('_research/zh_found2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
