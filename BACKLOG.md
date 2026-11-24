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

## 待补建概念清单（续作DG 交叉引用发现，47 个）

建立条目关联时发现以下概念被引用但库中不存在。按价值排序，优先补建前两档：

**第一档（机制/制度，优先）**
`bank-resolution`（银行处置）、`counterparty-risk`（对手方风险）、`toxic-assets`（有毒资产）、
`junk-bond`（垃圾债券）、`sacrifice-ratio`（牺牲率）、`payment-system`（支付系统）、
`disclosure`（信息披露）、`market-failure`（市场失灵）、`prisoners-dilemma`（囚徒困境）、
`property-rights`（产权）、`transaction-cost`（交易成本）、`rent-seeking`（寻租）

**第二档（基础经济学概念）**
`savings`、`investment`、`demand`、`growth`、`population`、`recession`、`inequality`、
`labour-market`、`specialization`、`agriculture`、`tax-capacity`、`tax-incidence`、
`short-term-rate`、`secured-lending`、`self-insurance`、`risk-pooling`、`actuarial`、
`leading-indicator`、`deindustrialization`、`supervision`、`rogue-trader`、`audit-failure`、
`bank-holiday`、`bullion`、`var`（风险价值）、`common-pool`、`pigouvian-tax`、`lloyds`

**注**：`credit-anstalt` 实际 id 为 `creditanstalt`；`clearing` 无独立条目，相关机制见 `netting`。

## 续作EF 新发现的 19 个基础概念（round 37）

建立关联时发现以下概念被引用但不存在，**多为经济学最基础的概念**：

`growth`（增长）、`expectations`（预期）、`utility`（效用）、`recession`（衰退）、
`market-failure`（市场失灵）、`rent-seeking`（寻租）、`externalities`（外部性）、
`disclosure`（信息披露）、`dividend`（股息）、`equity-premium`（股权溢价）、
`term-premium`（期限溢价）、`convergence`（收敛）、`counterparty-risk`（对手方风险）、
`effective-demand`（有效需求）、`proprietary-trading`（自营交易）、
`regulatory-arbitrage`（监管套利）、`subordination`（次级化）、
`taper-tantrum`（缩减恐慌）、`special-drawing-rights`（特别提款权，实际有 `sdr`）

**观察**：本站概念覆盖偏向"金融专门术语"，而基础经济学地基不完整。补建时应优先处理
`growth`／`expectations`／`utility`／`recession`／`market-failure`／`rent-seeking` 六项。
