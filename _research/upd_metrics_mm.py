# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts

c = counts(es)
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))
ncmp = sum(1 for e in es if e.get('comparison'))
nsch = sum(1 for e in es if e.get('schools'))
reln = [len(e.get('related', [])) for e in es]

note = """维基第108轮可用。MH-MM：为全部 63 条案例补齐 comparison，覆盖率达 641/641；并修复 check_pages 的一个子串匹配伪阳性 bug。
①本轮分四批为 63 条缺 comparison 的条目补写结构性对比（一律对比 related 中已存在的条目，每条说明两者机制差异，不新增无据数字）：第一批 12、第二批 9（3 条已有跳过）、第三批 21、第四批 21。
②对比的原则：只说结构性差异——如「负债端挤兑 vs 资产端损失」（bank-crisis-2023 vs subprime）、「资产充足却脆弱」（northern-rock）、「无本币可贬 vs 有汇率工具」（希腊 vs 阿根廷）、「慢性通缩 vs 金融崩溃型大萧条」（long-depression vs great-depression）。
③修复 check_pages 的 bug：其「文案与导航一致性」检查用子串匹配判断 id 是否被提及，导致 inflation 误命中 hyperinflation、otc 误命中无关词。已改为词边界正则匹配 (?<![a-z0-9-])id(?![a-z0-9-])。这是第 10 次工具缺陷，也是「检查器本身误报」的又一例。
④配套修复：写 comparison 引用了大量 related 条目，用既定扫描脚本（识别「见 xxx」与反引号 id）批量补全 related 并对称化；因 3 字母 id（imf）不被 {3,} 正则匹配，个别手工补入。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；comparison """ + str(ncmp) + """/641（全覆盖）、schools """ + str(nsch) + """、related 平均 """ + str(round(sum(reln) / len(reln), 1)) + """ 条；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作MH-MM', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 63, 'reviewed': 63, 'fixed': 64,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0；comparison 641/641 + 自测 18/18',
    'spot_check': '63 条案例补 comparison 达全覆盖；修复 check_pages 子串匹配伪阳性',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 108 轮可用（round 128）**。**为全部 63 条案例补齐 comparison，覆盖率达 641/641**；并修复 check_pages 的一个**子串匹配伪阳性 bug**。
- **本轮分四批为 63 条缺 comparison 的条目补写结构性对比**（一律对比 related 中已存在的条目，每条说明「两者机制差异」，不新增无据数字）。
- **对比的原则**：只说**结构性差异**——如「负债端挤兑 vs 资产端损失」（bank-crisis-2023 vs subprime）、「资产充足却脆弱」（northern-rock）、「无本币可贬 vs 有汇率工具」（希腊 vs 阿根廷）、「慢性通缩 vs 金融崩溃型大萧条」（long-depression vs great-depression）。
- **修复 check_pages 的 bug**：其「文案与导航一致性」检查用**子串匹配**判断 id 是否被提及，导致 `inflation` 误命中 `hyperinflation`、`otc` 误命中无关词。已改为**词边界正则**匹配。**这是第 10 次工具缺陷，也是「检查器本身误报」的又一例。**
- **配套修复**：写 comparison 引用了大量 related 条目，用既定扫描脚本批量补全 related 并对称化；因 3 字母 id（`imf`）不被 `{3,}` 正则匹配，个别手工补入。
- 现状：**641 条**、来源 **742**、页面 **655**；**comparison 641/641（全覆盖）**、schools 636、related 平均 **7.5** 条；**ERRORS 0、WARNINGS 0**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作ME-MG｜2026-11-24｜状态：641条；质量审计+补11条schools两派观点**',
              '**续作MH-MM｜2026-11-24｜状态：641条；63条案例补comparison达全覆盖，修复check_pages伪阳性**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', ncmp, '| schools', nsch, '| avg', avg)
