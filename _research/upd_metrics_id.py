# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)

note = (
    '维基第68轮可用。IC-ID：**核查危机理论类，补充 original-sin，并自我纠正一处"定义充数据"**。'
    '①核查 20 个危机理论概念，**16 项已覆盖**（minsky-theory／debt-deflation／'
    'balance-sheet-recession／sudden-stop／self-fulfilling／contagion／original-sin／twin-crises／'
    'bank-run／liquidity-trap／debt-overhang／credit-crunch／fire-sale／'
    'asset-liability-mismatch／procyclicality／financial-accelerator）。'
    '②剩余的 `currency-mismatch` 经查**已被 `original-sin` 覆盖**（后者概述即"货币错配使这些国家'
    '在贬值时承受资产负债表冲击"），不另建；`doom-loop`／`disclosure`／`bank-resolution` 的维基页'
    '均无专属页面或为通用页，不作专属来源。'
    '③**补充 `original-sin`**：抓取其专属页全文（12,562 字符），补 timeline 3 条'
    '（1999 Eichengreen-Hausmann 提出／2001 与 Panizza 扩展为 OSIN1-3／2003 转向"原罪的赎免"），'
    '并把概述扩写为包含三个指标定义与**六个决定因素**（发展水平／货币可信度／债务负担／'
    '汇率制度／收益率曲线斜率／投资者基础规模）。'
    '④**自我纠正**：起初把"OSIN 取值范围 0—1""3 个指标""6 个决定因素"写成 3 条 key_data，'
    '随后意识到这些是**概念定义而非具体数值数据**，放进 key_data 会让读者误以为该条目有量化证据；'
    '已全部移除（key_data 3 → 0），并在 pending_notes 注明"具体国别指标值待补来源后再录"。'
    '同时修正 timeline 中一处中英混杂错字。'
    '⑤现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、timeline ' + str(tl) + '、'
    'key_data ' + str(tk) + '。**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IC-ID', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 20, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿',
    'spot_check': '危机理论 16/20 覆盖；original-sin 补充并移除定义性 key_data',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 68 轮可用（round 87）**。**核查危机理论类，补充 `original-sin`，并自我纠正一处"定义充数据"**。
- **危机理论类核查**：20 个概念中 **16 项已覆盖**（minsky-theory／debt-deflation／balance-sheet-recession／sudden-stop／self-fulfilling／contagion／original-sin／twin-crises／bank-run／liquidity-trap／debt-overhang／credit-crunch／fire-sale／asset-liability-mismatch／procyclicality／financial-accelerator）。
- 剩余判定：
  - `currency-mismatch` —— **已被 `original-sin` 覆盖**（后者概述即"货币错配使这些国家在贬值时承受资产负债表冲击"），不另建
  - `doom-loop`／`disclosure`／`bank-resolution` —— 维基无专属页或仅通用页，不作来源
- **补充 `original-sin`**（据专属页全文 12,562 字符）：
  - timeline 3 条：**1999** Eichengreen-Hausmann 提出／**2001** 与 Panizza 扩展为 OSIN1–3／**2003** 转向"原罪的赎免"
  - 概述扩写：三指标定义（OSIN 均为"1 − 本币计价证券占比"，0—1）+ **六个决定因素**（发展水平／货币可信度／债务负担／汇率制度／收益率曲线斜率／投资者基础规模）
- **④ 自我纠正**：起初把"OSIN 取值范围 0—1""3 个指标""6 个决定因素"写成 3 条 `key_data`，随后意识到这些是**概念定义而非具体数值数据**——放进 `key_data` 会让读者误以为该条目有量化证据。**已全部移除（3 → 0）**，并注明"具体国别指标值待补来源后再录"。另修正 timeline 一处中英混杂错字。
- 现状：**635 条**、来源 733、页面 649。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IB｜2026-11-24｜状态：635条；概念类别审计，新建资本充足率与LCR**',
              '**续作IC-ID｜2026-11-24｜状态：635条；危机理论核查，original-sin补充并纠"定义充数据"**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
