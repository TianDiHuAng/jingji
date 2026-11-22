# BLOCKERS.md — 阻塞与质量问题记录

## 已解决
- **轮次3｜学者归属错配**（已修复）：L3 升级时把 Kindleberger、Reinhart&Rogoff 的观点错误挂到来源库中作者不符的著作（bk-the-ascent-of-money 作者为 Niall Ferguson、bk-crisis-economics 作者为 Nouriel Roubini）。由独立抽检子任务发现，已批量修正为来源库真实作者的准确表述（12+3 条），并同步修正升级脚本源头。下轮抽检比例提高至 25%。

## 待处理（未构成阻塞，入 BACKLOG）
- 反爬来源 5 条（Britannica/IMF/Investopedia/百度百科/BLS）返回 HTTP 403，无法核对标题/年份，维持 verified=false。
- 106 条条目全部 needs_verification=true（具体数值/人物/政策细节待查原文），属 TASK 硬性规则下的诚实标注，非阻塞。

## 失败次数记录
（同一问题连续失败3次才记为阻塞并跳过；当前无）
