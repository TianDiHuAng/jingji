# REPORT.md — 项目摘要

**轮次 143｜2026-11-24｜状态：持续维护与质量验证中（非饱和）；维基网络出口不可用**

> 说明：本文件此前停留在轮次 25（当时 135 条／212 来源，并标注 SATURATED）。
> 此后条目大幅扩充、增加多项自动检查，本文件长期未被同步更新（一处**陈旧文档**，已于本轮修正）。
> 以下为**当前实际状态**。

**当前：总条目 641、来源 749 条、站点 659 页；`key_data` 675 条、timeline 事件 1026 条、comparison 641 条。**（本行为机器可核对的状态摘要，更新数据时须同步。）

## 一、规模概览

| 项 | 数值 |
|---|---|
| 条目总数 | **641**（案例 **209** / 概念 **432**） |
| 层级 | L2 607、L3 34 |
| 来源库 | **740**（全部 verified） |
| 站点页面 | **655**（14 静态页 + 641 条目页） |
| key_data 行 / timeline 事件 | 464 / 658 |
| comparison 覆盖 | **641/641** |
| 两派及以上 schools 的条目 | 634 |

## 二、质量保障（自动化）

- **十一道检查全绿**：`check.py`（R1–R22 + R4b/R12b，覆盖数据类型、来源、嵌套来源、SVG、枚举词汇、内容字段、coverage 一致性等）、
  `check_links`（断链）、`check_quality`（HTML 结构，含任意字面 `**` 检测）、`check_kd`/`check_body_num`/`check_polnum`（数字溯源，两级判据）、
  `check_sources`、`check_docs`（文档与真实数据一致）、`check_filler`（套话/占位/整段重复）、`check_pages`（首页/验证页/矩阵数字一致 + 站点完整性）。
- **自测 23/23**：`tools/selftest.py` 对 R1/R4b/R7/R8/R9/R10/R12/R12b/R17/R18/R19/R20、文案导航一致性、check_filler、check_links、check_quality、matrix 合计等**逐一注入已知错误**，确认每个检查确实能捕获。

## 三、质量建设要点（round 100–142 摘要）

- **验证"验证方法"**：发现并修复多个检查器自身缺陷——`check_kd` 假匹配（数字出现即判通过）、缺"亿/万↔billion/million"换算；
  `check_pages` 子串匹配 id 伪阳性（已改词边界）；`check_quality` 只抓成对 `**`、漏孤立 `**`；R4b 变量作用域只查 1 条。均加自测防回归。
- **内容逐条抽查**（round 131–134）：修复 `blue-monday-2009` 事件张冠李戴（把 2009-03 美股数字安到 2009-01 英国银行股事件）、
  14 处 key_data 来源错标、若干日期/免责声明瑕疵。
- **陈旧产出物治理**：`HEALTH_CHECK.md`、`COVERAGE_MATRIX.md`（matrix.html 592→641）、`coverage.json`（6 处字段）、本 `REPORT.md`——
  均已修正并部分纳入自动检查（矩阵合计断言、R12b coverage 字段一致性）。

## 四、遗留（受网络不可用所限）

1. **3 条案例缺专属维基全文**：`south-sea-bubble-1720`／`bear-stearns`／`bcci`——本会话网络持续超时，其概述仅据条目内已核事实与机制撰写，**具体细节待补**。
2. **6 条缓存为通用页**：`dutch-stock-crashes`／`panic-1896`／`panic-1910`／`us-video-game-crash-1983`／`yemen-currency-divergence`（另 `recession` 属正常）——条目内容与引用正确，仅本地无法逐数核对。
3. **部分数字仅弱匹配**：多为 OWID/机构数据（不在维基全文）或推导值，**不代表错误**，需人工判断。
4. **成果未备份到 GitHub（需人工处理）**：远程仓库 `TianDiHuAng/jingji` 的 `pushed_at` 停在 2026-11-22（约 round 25），此后本地约 415 个提交未推送；本会话无 GitHub token，无法自动推送。**建议有凭证时 `git push origin main`。** 详见 `BACKLOG.md`。

以上 1–3 均已在 `BACKLOG.md`／各条目 `pending_notes` 标注，网络恢复即可补齐。

> 网络诊断（round 167–168）：出网为**白名单式**——github／baidu 等少数可达，维基被 DNS 污染 + TLS 黑洞双重拦截，archive.org 与各种 CORS 代理均不可用，DBpedia 摘要端点返回空。故维基内容在本会话无法取回。

## 五、下一步

- 继续核验"不在检查清单上的产出物"与内容准确性（逐条抽查已趋收敛）。
- 网络恢复后：补抓上列缺全文/缺缓存的来源；扩充 3 条案例细节。
- 项目**未判定饱和**：仍有可做的本地质量工作与（网络恢复后的）内容补全。
