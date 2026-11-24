# -*- coding: utf-8 -*-
"""续作HL：重写 BACKLOG 的"待建概念"部分，用当前实际状态替代 round 37 的过时清单。"""
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}
titles = {e['title'] for e in es}

# 本轮已核实的状态分类
DONE = [('externalities', 'externality（已有，id 不同）'),
        ('var', 'value-at-risk（已有，id 不同）'),
        ('common-pool', '本轮新建'),
        ('pigouvian-tax', '本轮新建'),
        ('actuarial', '本轮新建'),
        ('bullion', '本轮新建'),
        ('lloyds', '本轮新建'),
        ('deindustrialization', '本轮新建'),
        ('tax-capacity', 'fiscal-capacity 已覆盖'),
        ('supervision', 'bank-regulation／macroprudential 已覆盖'),
        ('government-bailout', 'bailout 已覆盖'),
        ]
GAP = [
    ('bank-resolution', '维基无独立页面（round 46 验证），相关机制见 bad-bank／bank-failure'),
    ('sacrifice-ratio', '维基无独立页面；相关内容见 phillips-curve／disinflation'),
    ('term-premium', '维基无独立页面；相关内容见 yield-curve／risk-premium'),
    ('regulatory-arbitrage', '维基重定向到 Arbitrage（通用页），不宜作专属来源'),
    ('taper-tantrum', '维基重定向到 Quantitative easing（通用页）'),
    ('disclosure', '维基 Disclosure 仅 2.8k 字符、Transparency (market) 5.2k；价值中等，暂缓'),
    ('leading-indicator', '可用 Economic indicator（9k 字符），待建'),
    ('self-insurance', '缺；与 deposit-insurance 不等价'),
    ('risk-pooling', '缺；与各类 risk 条目不等价'),
    ('secured-lending', '缺；与 interbank-lending 不等价'),
    ('audit-failure', '缺；与 bank-failure 不等价'),
    ('bank-holiday', '缺；1933 年美国银行停业事件，维基 Bank holiday 页为英国公共假日（不可用）'),
    ('rogue-trader', '缺；可用 Rogue trader 相关页面（待测）'),
    ('agriculture', '缺；范围过宽，暂缓'),
    ('short-term-rate', 'interest-rate 部分覆盖'),
]

NEW_BLOCK = '''## 待建概念清单（round 78 重新校验）

> **说明**：原清单编制于 round 37，长期未复核，导致 round 77 依它建了已存在的
> `externalities`／`var`（站内实为 `externality`／`value-at-risk`）。
> 下表已按**当前实际状态**重写，并给出每项的核实结论。

### 已完成／已有覆盖（不必再建）

| 概念 | 状态 |
|---|---|
''' + ''.join('| `%s` | %s |\n' % (a, b) for a, b in DONE) + '''
### 真实缺口（按优先级）

| 概念 | 核实结论 |
|---|---|
''' + ''.join('| `%s` | %s |\n' % (a, b) for a, b in GAP) + '''
**核实方法**：先查 `data/entries/` 的实际 id 与标题（不只比对清单），
再测维基页面是否为**专属页**（通用页/重定向页不作专属来源）。
'''

p = 'BACKLOG.md'
s = open(p, encoding='utf-8').read()
# 替换从"## 待补建概念清单"到文件末尾的全部内容
import re
m = re.search(r'\n## 待补建概念清单.*\Z', s, re.S)
if m:
    s = s[:m.start()] + '\n' + NEW_BLOCK
    open(p, 'w', encoding='utf-8').write(s)
    print('BACKLOG 待建概念部分已重写')
else:
    s = s.rstrip() + '\n\n' + NEW_BLOCK
    open(p, 'w', encoding='utf-8').write(s)
    print('BACKLOG 追加待建概念部分')
print('当前条目:', len(es), '| 概念:', sum(1 for e in es if e['unit'].startswith('U6')))
