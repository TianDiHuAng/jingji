# BACKLOG.md — 待办队列（轮次26起点）

优先级：核心＞重要＞补充；复核/修复优先于新增；覆盖稀疏维度优先。

## 网络状态（关键）
- 维基网络出口不可用：DNS污染(解析到Facebook IP) + 已知维基IP直连返回301 → 维基内容整体无法获取（已诊断，记BLOCKERS）

## 饱和评估
- 核心29全L3、重要59全L2（层级全达标）
- **唯一已知未决缺口：2020新冠股灾** — 因网络出口阻塞无法核对来源，按"不编造"不硬凑
- 其余所有权威大纲/读者问题/矩阵缺口均已覆盖；累计案例化33条L2
- 结论：饱和受外部网络阻塞制约，非内容缺口

## 待执行（轮次26）

| 序 | id | 类型 | 优先级 | 依赖 |
|---|---|---|---|---|
| 1 | DEEPEN-SEMANTIC-7 | 深化 | P2 | 剩余有本地语料的通用模板L2（asian/black-monday已做，余少量）| 本地 |
| 2 | QA-CONSISTENCY | 复核 | P2 | 全站数据一致性/口径抽查 | 本地 |
| 3 | 抽检 | 质量闸 | P1 | 10% | — |
| 4 | NEW-2020-crash | 新条目 | P1 | 2020崩盘 | 需网络恢复 |

## 轮次25已完成（移出）
- ✅ DEEPEN-SEMANTIC 第六批：6条案例化（asian-1997/black-monday-1987 两核心L3 + brexit-2016/panic-1825/south-america-2002/ghana-2017）
- ✅ 网络出口诊断（DNS污染）→ 2020崩盘记BLOCKER不硬凑
- ✅ 自检事实一致

## 结构性空白（非缺口）
- 理论制度单元按类型归「制度/理论」；20世纪上半×货币（1931英镑危机无独立页）；反爬来源5条；3单源数值已跳过；预测性话题跳过

## 质量注意
- 案例化据原文不编造；L3有deep_svg；数值年份对照原文；来源id对照sources.json

## 饱和进度
- zero_gap_streak：0（2020崩盘外部阻塞未决）
- saturated=false

## 待建概念清单（round 78 重新校验）

> **说明**：原清单编制于 round 37，长期未复核，导致 round 77 依它建了已存在的
> `externalities`／`var`（站内实为 `externality`／`value-at-risk`）。
> 下表已按**当前实际状态**重写，并给出每项的核实结论。

### 已完成／已有覆盖（不必再建）

| 概念 | 状态 |
|---|---|
| `externalities` | externality（已有，id 不同） |
| `var` | value-at-risk（已有，id 不同） |
| `common-pool` | 本轮新建 |
| `pigouvian-tax` | 本轮新建 |
| `actuarial` | 本轮新建 |
| `bullion` | 本轮新建 |
| `lloyds` | 本轮新建 |
| `deindustrialization` | 本轮新建 |
| `tax-capacity` | fiscal-capacity 已覆盖 |
| `supervision` | bank-regulation／macroprudential 已覆盖 |
| `government-bailout` | bailout 已覆盖 |

### 真实缺口（按优先级）

| 概念 | 核实结论 |
|---|---|
| `bank-resolution` | 维基无独立页面（round 46 验证），相关机制见 bad-bank／bank-failure |
| `sacrifice-ratio` | 维基无独立页面；相关内容见 phillips-curve／disinflation |
| `term-premium` | 维基无独立页面；相关内容见 yield-curve／risk-premium |
| `regulatory-arbitrage` | 维基重定向到 Arbitrage（通用页），不宜作专属来源 |
| `taper-tantrum` | 维基重定向到 Quantitative easing（通用页） |
| `disclosure` | 维基 Disclosure 仅 2.8k 字符、Transparency (market) 5.2k；价值中等，暂缓 |
| `leading-indicator` | 可用 Economic indicator（9k 字符），待建 |
| `self-insurance` | 缺；与 deposit-insurance 不等价 |
| `risk-pooling` | 缺；与各类 risk 条目不等价 |
| `secured-lending` | 缺；与 interbank-lending 不等价 |
| `audit-failure` | 缺；与 bank-failure 不等价 |
| `bank-holiday` | 缺；1933 年美国银行停业事件，维基 Bank holiday 页为英国公共假日（不可用） |
| `rogue-trader` | 缺；可用 Rogue trader 相关页面（待测） |
| `agriculture` | 缺；范围过宽，暂缓 |
| `short-term-rate` | interest-rate 部分覆盖 |

**核实方法**：先查 `data/entries/` 的实际 id 与标题（不只比对清单），
再测维基页面是否为**专属页**（通用页/重定向页不作专属来源）。
