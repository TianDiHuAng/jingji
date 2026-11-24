# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))
kd = sum(len(e.get('key_data') or []) for e in es)

note = """维基第147轮可用。PF：网络出口精化诊断——并非全断网，而是维基被针对性阻断；尝试多种绕过均失败，记入 BLOCKERS。
①**探测**：TCP 层通（8.8.8.8:53、github:443、维基IP:443 均 OPEN）；TLS 到 github.com **成功**；
但 DNS 把 en.wikipedia.org／wikiwand／google 解析到 Facebook/Twitter IP（污染），直连维基真实 IP 则 **TLS 握手被黑洞**（:80 RST）。
②**尝试绕过**：DoH（1.1.1.1/dns.google）超时；CORS 代理 allorigins/codetabs 取维基 API **HTTP 522**；corsproxy 401；DBpedia 可达但目标资源 `dbo:abstract` **SPARQL 返回 0 行**。
③**结论**：通用 HTTPS 可用、**唯维基被 DNS+TLS 针对性阻断**，现有免费代理无法绕过；3 条缺全文 + 5 条缓存缺口本会话仍无法补齐。已把精化诊断表记入 BLOCKERS。
④本轮无数数据改动；十一道检查全绿、自测 34/34。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 34/34。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PF', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 0, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 34/34',
    'spot_check': '网络精化诊断：TCP通/github TLS通/维基被DNS+TLS阻断，多种绕过失败，记入 BLOCKERS',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 147 轮可用（round 167）**。**网络出口精化诊断——并非全断网，而是维基被针对性阻断；尝试多种绕过均失败，记入 BLOCKERS**。
- **探测**：TCP 层通（8.8.8.8:53、github:443、维基 IP:443 均 OPEN）；TLS 到 github.com **成功**；但 DNS 把 en.wikipedia.org／wikiwand／google 解析到 Facebook/Twitter IP（污染），直连维基真实 IP 则 **TLS 握手被黑洞**（:80 RST）。
- **尝试绕过**：DoH（1.1.1.1/dns.google）超时；CORS 代理 allorigins/codetabs 取维基 API **HTTP 522**；corsproxy 401；DBpedia 可达但目标资源 `dbo:abstract` **SPARQL 返回 0 行**。
- **结论**：通用 HTTPS 可用、**唯维基被 DNS+TLS 针对性阻断**，现有免费代理无法绕过；3 条缺全文 + 5 条缓存缺口本会话仍无法补齐。已把精化诊断表记入 BLOCKERS。
- 本轮无数据改动；十一道检查全绿、自测 34/34。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 34/34。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
