# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)
from kdclass import counts
c = counts(es)

note = (
    '维基第72轮可用。IM：**新建 3 条（1 案例 + 2 概念），全部有专属维基页**。'
    '①**`bank-holiday`（1933 年美国银行假日）**——此前因维基 "Bank holiday" 页只是'
    '英国公共假日（1,363 字符，与 1933 年无关）而被记入缺口；'
    '本轮找到真正的专属页 **Emergency Banking Act of 1933**（5,807 字符）。'
    '可核实事实：**1933.2.14** 密歇根州率先宣布**八天**银行假日、恐惧跨州蔓延、'
    '数周内各州相继停业；**3.9** 国会通过《紧急银行救济法》（1917 年《与敌国贸易法》修正案），'
    '**授权十二家联邦储备银行以"良好资产"为担保发行额外货币**；'
    '**3.13** 复业后储户排队存回现金、**两周内回流超过停业前合法提取额的一半**；'
    '**3.15** 华尔街复市、道指涨 **8.26 点**；同年《1933 年银行法》设立 FDIC。'
    '②**`risk-pooling`（风险池）**与**`self-insurance`（自我保险）**——两条风险管理制度概念，'
    '各含两派观点（分散化 vs 相关性风险／成本效率 vs 尾部风险）。'
    '③**一个判断修正**：此前把 `w-en-bank-regulation`／`w-en-bank-run`／`w-en-recession` 等'
    '视为"通用页"并担心条目依赖它们；复核后确认——**这些页对相应概念条目恰是专属页**，不是缺陷。'
    '真正意义上的通用页是 `w-en-financial-crisis`（被 104 个案例引用作背景），属合理用法。'
    '④现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、timeline ' + str(tl) + '、key_data ' + str(tk) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IM', 'date': '2026-11-24', 'new_entries': 3, 'upgraded': 3, 'reviewed': 7, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（639 条、653 页）',
    'spot_check': '新建 bank-holiday／risk-pooling／self-insurance',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：636**（案例 207 / 概念 429）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：737**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：650**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 72 轮可用（round 91）**。**新建 3 条（1 案例 + 2 概念）**。
- **① `bank-holiday`（1933 年美国银行假日）**——此前因维基 "Bank holiday" 页只是**英国公共假日**（1,363 字符，与 1933 年无关）而被记入缺口；本轮找到真正的专属页 **Emergency Banking Act of 1933**（5,807 字符）。可核实事实：

  | 时间 | 事件 |
  |---|---|
  | **1933.2.14** | 密歇根州率先宣布**八天**银行假日，恐惧跨州蔓延，数周内各州相继停业 |
  | **3.9** | 国会通过《紧急银行救济法》（1917 年《与敌国贸易法》修正案），**授权十二家联邦储备银行以"良好资产"为担保发行额外货币** |
  | **3.13** | 复业后储户排队存回现金，**两周内回流超过停业前合法提取额的一半** |
  | **3.15** | 华尔街复市，道指涨 **8.26 点** |
  | 同年 | 《1933 年银行法》通过，设立 **FDIC** |

- **② `risk-pooling`（风险池）**与 **`self-insurance`（自我保险）**——两条风险管理制度概念，各含两派观点（分散化 vs **相关性风险**／成本效率 vs **尾部风险**）。
- **③ 一个判断修正**：此前把 `w-en-bank-regulation`／`w-en-bank-run`／`w-en-recession` 视为"通用页"并担心条目依赖它们；复核后确认——**这些页对相应概念条目恰是专属页**，不是缺陷。真正意义的通用页是 `w-en-financial-crisis`（被 104 个案例引用作背景），属合理用法。
- 现状：**639 条**（案例 208／概念 431）、来源 **740**、页面 **653**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IK-IL｜2026-11-24｜状态：636条；sifi补认定机制，shadow-banking补监管沿革**',
              '**续作IM｜2026-11-24｜状态：639条；新建1933银行假日与两条风险管理概念**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 页面', pages)
