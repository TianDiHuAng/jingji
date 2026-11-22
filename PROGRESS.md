# 进度（PROGRESS.md）

> 自动模式：每次启动先读本文件，执行一轮完整循环（A→G），结束前更新。饱和前不写 ALL_DONE。

## 当前状态
- 模式：自动扩充（AUTONOMOUS.md 协议）
- 当前轮次：4（已完成）
- 上轮（轮次4）完成：
  - FIX-lowsrc：新增5个核对来源，6条理论条目补至双源
  - NEW-banking-crises：新增9条银行危机条目（双源），同步 scope.md / COVERAGE_MATRIX.md / 站点
  - REVIEW-pending：26条核心条目数值复核，无编造数字
  - 25%抽检4条全PASS（auditor-r4），抽检后优化2条来源引用
  - check.py 115条 0 error、check_links.py 126页 0 error
- 下一轮起点（轮次5）：
  1. REVIEW-values：挑标志性案例补入经双源核实的具体数值（若来源可支撑）
  2. L2-important-deepen：覆盖稀疏维度的重要条目深化
  3. NEW-outline-2：权威大纲剩余遗漏（需找替代权威来源）
  4. 抽检维持25%（连续2轮无缺陷后可降回10%）
- 层级现状：L1 52（+9）/ L2 37 / L3 26；总计115条、来源194条

## 轮次记录
| 轮次 | 日期 | 新增 | 升级L3 | 修复 | 抽检 | 检查 | 下一轮起点 |
|---|---|---|---|---|---|---|---|
| 0 | 2026-11-22 | 样板2 | — | — | — | PASS | 手动批量 |
| 1 | 2026-11-22 | 104 | — | — | 4 PASS | PASS | 站点生成 |
| 2 | 2026-11-22 | — | — | — | — | PASS | 自动模式 |
| 3 | 2026-11-22 | 0 | 26 | 15 | 3(2修) | PASS | 补源+新条目 |
| 4 | 2026-11-22 | 9 | 0 | 8 | 4(25%)PASS | PASS | REVIEW-values+深化 |

## 状态文件
- BACKLOG.md / METRICS.json / SATURATION.json / GAP_REPORT.md / BLOCKERS.md / DECISIONS.md

（未写 ALL_DONE — 自动模式以饱和为准；当前 saturated=false）
