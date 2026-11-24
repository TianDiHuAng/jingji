# -*- coding: utf-8 -*-
"""续作HO：为单来源的概念条目补中文维基作为第二来源（跨语言对照）。"""
import glob
import json
import os
import ssl
import time
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}

es = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
      for f in glob.glob('data/entries/*.json')}
single = [e for e in es.values() if len(e.get('sources', [])) == 1]
print('单来源条目:', len(single))

# 中文标题候选：用条目标题去掉括号与年份
def cands(title):
    t = title.split('(')[0].split('（')[0].strip()
    return [t]


found = []
for e in single:
    for zh in cands(e['title']):
        api = ('https://zh.wikipedia.org/w/api.php?action=query&format=json&prop=extracts'
               '&exintro=1&explaintext=1&redirects=1&titles=' + urllib.parse.quote(zh))
        try:
            d = json.loads(urllib.request.urlopen(
                urllib.request.Request(api, headers=HDR), timeout=15, context=CTX).read())
            for _, pv in d.get('query', {}).get('pages', {}).items():
                txt = pv.get('extract', '') or ''
                real = pv.get('title', '')
                if len(txt) > 300 and '可能指' not in txt[:60]:
                    found.append((e['id'], real, len(txt)))
                    print('%-26s → zh《%s》%d字符' % (e['id'], real[:24], len(txt)))
                    break
        except Exception as ex:
            pass
        time.sleep(0.3)
        break

print('\n找到中文维基页面:', len(found))
json.dump(found, open('_research/zh_found.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
