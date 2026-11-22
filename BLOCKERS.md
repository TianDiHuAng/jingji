# BLOCKERS.md — 阻塞与质量问题记录

## 已解决
- **轮次3｜学者归属错配**（已修复）：L3 升级时把 Kindleberger、Reinhart&Rogoff 的观点错误挂到来源库中作者不符的著作（bk-the-ascent-of-money 作者为 Niall Ferguson、bk-crisis-economics 作者为 Nouriel Roubini）。由独立抽检子任务发现，已批量修正为来源库真实作者的准确表述（12+3 条），并同步修正升级脚本源头。下轮抽检比例提高至 25%。

## 待处理（未构成阻塞，入 BACKLOG）
- 反爬来源 5 条（Britannica/IMF/Investopedia/百度百科/BLS）返回 HTTP 403，无法核对标题/年份，维持 verified=false。
- 106+条条目全部 needs_verification=true（具体数值/人物/政策细节待查原文），属 TASK 硬性规则下的诚实标注，非阻塞。
- **4条单源数值（轮次5补入，轮次6子任务全面核查、轮次7复评）**：马克汇率320(1922中)、黑色星期四12.9M股、房价跌幅30%、家庭净资产13万亿 —— 轮次6联网核查仅在可访问的 Wikipedia/Fed 页面找到单源；第2次核查（轮次7）未新增来源。按 AUTONOMOUS 第六条"同一问题连续失败3次记BLOCKERS并跳过"，此为第2次，暂维持待核实。注意：13万亿数值另见英文维基 Great Recession 记为11万亿，已在条目 note 记录分歧。

## 失败次数记录
（同一问题连续失败3次才记为阻塞并跳过；当前无）
