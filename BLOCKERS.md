# BLOCKERS.md — 阻塞与质量问题记录

## 已解决
- **轮次3｜学者归属错配**（已修复）：L3 升级时把 Kindleberger、Reinhart&Rogoff 的观点错误挂到来源库中作者不符的著作（bk-the-ascent-of-money 作者为 Niall Ferguson、bk-crisis-economics 作者为 Nouriel Roubini）。由独立抽检子任务发现，已批量修正为来源库真实作者的准确表述（12+3 条），并同步修正升级脚本源头。下轮抽检比例提高至 25%。

## 待处理（未构成阻塞，入 BACKLOG）
- 反爬来源 5 条（Britannica/IMF/Investopedia/百度百科/BLS）返回 HTTP 403，无法核对标题/年份，维持 verified=false。
- 106+条条目全部 needs_verification=true（具体数值/人物/政策细节待查原文），属 TASK 硬性规则下的诚实标注，非阻塞。
- **单源数值最终处理（轮次5补入，轮次6/7/8三次核查）**：
  - 黑色星期四12.9M股 → 轮次8找到法语维基第二来源，已双源印证 ✅
  - 马克汇率320(1922中)、房价跌幅30% → 三轮核查（en/zh/de/es/fr维基+Fed/NBER+机构页）无可访问第二来源，按AUTONOMOUS第六条"连续失败3次记BLOCKERS并跳过"，正式跳过，维持待核实。
  - 家庭净资产13万亿 → 三轮核查无第二来源，且英文维基Great Recession记为11万亿（分歧已记条目note），维持待核实，正式跳过。
  说明：结论限于本机可访问页面范围（Britannica/IMF/Investopedia/BLS返回403未纳入）。

## 失败次数记录
（同一问题连续失败3次才记为阻塞并跳过；当前无）
