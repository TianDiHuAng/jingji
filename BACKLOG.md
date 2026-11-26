# BACKLOG.md — 待办与缺口（round 144 重新校验）

> 原文件停在"轮次26起点"，其"待建概念/真实缺口"表长期未复核，导致多条**其实早已建成**的条目仍被列为缺口
> （与 round 77 依过时清单重复建条目的教训同源）。本文件按当前实际状态重写。

## 当前状态

- 条目 **641**（案例 209 / 概念 432）、来源 **746**、页面 **659**；十一道检查全绿、自测 35/35。
- 层级：L2 607、L3 34（L1 为 0）。

## 网络状态（关键，仍未恢复）

- 维基网络出口不可用：**DNS 污染 + 直连超时**（本会话多次重试均失败）→ 维基内容整体无法获取。
- 影响：见"网络相关遗留"。**这是当前唯一的硬约束**。

## 网络相关遗留（网络恢复后处理）

1. **3 条案例缺专属维基全文**：`south-sea-bubble-1720`／`bear-stearns`／`bcci`——
   概述仅据条目内已核事实与机制撰写，**具体细节待补**（已在各自 pending_notes 标注）。
2. **5 条案例缓存为通用页**（专属来源全文未缓存）：`dutch-stock-crashes`／`panic-1896`／`panic-1910`／
   `us-video-game-crash-1983`／`yemen-currency-divergence`——条目内容与引用正确，仅本地无法逐数核对。
   **补抓方法**：用 Wikipedia API 按专属来源 title 抓 extract，覆盖写入 `_research/wiki_full/<id>.txt`，再跑 `check_kd` / `check_body_num`。

## 概念缺口（已核实，暂不建）

| 概念 | 核实结论 |
|---|---|
| `sacrifice-ratio` | 维基无专属页；相关内容见 phillips-curve／disinflation → **不单建** |
| `term-premium` | 维基无专属页；相关内容见 yield-curve／risk-premium → **不单建** |
| `regulatory-arbitrage` | 重定向到 Arbitrage（通用页），不宜作专属来源 → **不建** |
| `audit-failure` | 无专属页（Audit failure 为空） → **不建** |
| `disclosure` | Disclosure 页面价值中等、Transparency(market) 一般 → **暂缓** |
| `rogue-trader` | Rogue trader 页过短（约 1.8k 字符）→ **暂缓** |
| `short-term-rate` | interest-rate 已部分覆盖 → **不单建** |
| `agriculture` | 范围过宽，非金融危机专属 → **不建** |

> 上述多为"无专属来源/范围过宽"，属**来源可得性**限制，非内容未做。

## 已建成（此前曾列为"待建概念"，现均已有条目）

`bank-resolution`、`taper-tantrum`、`leading-indicator`、`self-insurance`、`risk-pooling`、
`secured-lending`、`bank-holiday`、`common-pool`、`pigouvian-tax`、`actuarial`、`bullion`、
`lloyds`、`deindustrialization`。

（`externalities`→实为 `externality`；`var`→实为 `value-at-risk`；`tax-capacity`→`fiscal-capacity`；
`supervision`→`bank-regulation`/`macroprudential`；`government-bailout`→`bailout`——均已有覆盖。）

## 已完成的历史待办（留档）

- **R21 英文占比超标**（round 110 记录 33 条）：round 111 全部改写为中文，归零。
- **R22 内容过短**（round 112 记录 335 条）：round 113–126 共 14 轮全部扩写，归零。
- **覆盖矩阵陈旧**：round 141 重生成 COVERAGE_MATRIX.md（592→641）。
- **coverage.json 字段陈旧**：round 142 同步 6 处字段。
- **REPORT.md 陈旧**：round 143 重写（原停在 round 25）。

## 质量注意（长期有效）

- 案例化据原文不编造；L3 应有 deep_svg；数值/年份对照原文；来源 id 对照 sources.json；
  未核实数字不在任何位置（含免责声明）以事实陈述或复述。
- 文档/派生产出物（REPORT／HEALTH_CHECK／COVERAGE_MATRIX／coverage.json）须随数据更新，已部分纳入自动检查。

## 备份风险（round 169 记录，需人工处理）

远程仓库 `https://github.com/TianDiHuAng/jingji`（public）最新 `pushed_at = 2026-11-22T07:31Z`（约 round 25），
此后**本地约 415 个提交（round 26–169）尚未推送到 GitHub**。本会话环境**无 GitHub token**，无法自动推送。
**建议**：在有凭证的环境执行 `git push origin main`（git 网络栈若不通，可用 GitHub Git Data API），以备份全部工作。
