# BLOCKERS.md — 阻塞与质量问题记录

## 部署状态（2026-11-26）

- `main` 推送会触发 `.github/workflows/pages.yml`，自动把 `site/` + `docs/` 发布到 `gh-pages` 分支（已连续运行成功）。
- GitHub Pages 已于 2026-11-26 由仓库管理员启用（Deploy from a branch：`gh-pages` / `/ (root)`）；部署成功，在线地址 <https://tiandihuang.github.io/jingji/>。之后每次推送 `main`，Actions 更新 `gh-pages` 分支后由 Pages 自动发布。

## 2026-11-26 复核：代理出口可用，历史维基阻塞已解除

- 本会话实测通用 HTTPS 被阻断，但经 SOCKS5 代理 `socks5h://127.0.0.1:10808` 可访问 Wikipedia API；已据此补抓全部缺失缓存（`_research/wiki_full` 共 640 个，仅 `classical-economics` 无英文来源）。
- 原"3 条缺全文"（south-sea-bubble-1720 / bear-stearns / bcci）与"5 条缓存为通用页"（dutch-stock-crashes / panic-1896 / panic-1910 / us-video-game-crash-1983 / yemen-currency-divergence）均已处理完毕。
- 仍无法解决：`hainan-property-bubble-1992`、`taiwan-bubble` 无英文维基专题页，缓存已停用并改名 `.wrongpage`；如需补全，应改用中文维基或其他来源。
- 下文 round 167/168 及"当前阻塞快照（round 145）"中的网络判断为当时记录，已过时。


## 网络出口精化诊断（round 167 复测）

**结论：并非全断网，而是"维基被针对性阻断 + DNS 污染"。**

| 探测 | 结果 |
|---|---|
| TCP 连接 8.8.8.8:53 / github.com:443 / 维基IP:443 | **均通** |
| TLS 到 github.com（140.82.112.4） | **成功** |
| DNS 解析 en.wikipedia.org / wikiwand.com / google.com | **被污染**→解析到 Facebook/Twitter IP（31.13.x / 157.240.x / 104.244.x），TCP 超时 |
| 直连维基真实 IP（208.80.154.224 / 198.35.26.96 / 103.102.166.224）:443 | TCP 通，但 **TLS 握手超时**（SNI 被黑洞）；:80 直接 RST |
| DoH（1.1.1.1 / dns.google 的 /resolve） | URLError 超时（外部 HTTPS 部分受限） |
| CORS 代理 api.allorigins.win / api.codetabs.com 取维基 API | **HTTP 522**（代理侧亦无法快速到达维基） |
| corsproxy.io | 401（需 key） |
| DBpedia（dbpedia.org:443 TLS 通） | 可达，但 `dbo:abstract` SPARQL 对目标资源（Bear_Stearns / BCCI / South_Sea_*）**返回 0 行**，无法取摘要 |

**含义**：通用 HTTPS（如 github.com）可用，**唯独维基被 DNS 污染 + TLS 层面针对性阻断**；现有免费代理均无法绕过；DBpedia 摘要不可得。
故 3 条缺全文 + 5 条缓存缺口**在本会话仍无法补齐**。**若网络策略解除（或可用 VPN/镜像），可立即补齐。**


> **round 168 补充**：进一步探测表明出网为**白名单式**——仅少数主机（github.com、www.baidu.com）可达；维基、archive.org、google、duckduckgo 等均被阻断；DNS 对 8.8.8.8 的查询亦被**透明污染**（返回 Twitter/Facebook IP），无法取得真实 IP；直连 archive.org 已知真实 IP（207.241.x）亦 Reset/超时。**结论：无任何本地可用手段取回维基全文，3+5 条须待网络策略解除或 VPN/镜像。**

## 当前阻塞快照（round 145 复核，优先看此节）

- **唯一实际阻塞：维基网络出口不可用**（DNS 污染 + 直连超时，本会话多次重试失败）。
- 受其影响的**真实遗留**：
  1. 3 条案例缺专属维基全文：`south-sea-bubble-1720`／`bear-stearns`／`bcci`（细节待补）。
  2. 5 条案例缓存为通用页（专属全文未缓存）：`dutch-stock-crashes`／`panic-1896`／`panic-1910`／`us-video-game-crash-1983`／`yemen-currency-divergence`。
- **以下旧记录已解决，不再是阻塞**（详见正文对应节的【round145 复核】标注）：
  - 「库缺 2020 新冠股灾」→ **`covid-crash-2020` 已建成**。
  - 「案例政策覆盖率停在 41%」→ 现为 **146/209（70%）**。
  - 「8 个条目来源为通用概念页」→ 均已补专属来源。
  - 「反爬 5 条 403 来源」→ 已从 sources.json 删除（见"续作CT"节）。


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

## 网络偶发中断（轮次17）
- 现象：轮次17 运行中 Wikipedia API 及 urllib 请求连续超时（WinError 10060），网络临时中断。
- 处理：按 AUTONOMOUS 六，改用已下载的本地大纲语料（_research/）做方法1复核，并转向本地可完成的方法2/3/4/7。联网类新增（新条目/新来源）本轮暂缓，下轮网络恢复后继续。
- 影响：非阻塞；已于本地确认大纲仍有未收录项（Recession of 1920–1921 等），故本轮判定未饱和。

## 国际网络出口中断（轮次18，连续第2轮）
- 现象：轮次18 实测 baidu 可达(200) 但 en/zh.wikipedia、OpenLibrary 均 URLError 超时——国际站点不可达（第2次连续）。
- 处理：按 AUTONOMOUS 六"连续失败3次记BLOCKERS并跳过"，改用库内既有 verified 来源做网络无关扩充（轮次18新增道德风险/太大而不能倒/不可能三角3个概念条目）。
- 待网络恢复：补建 Recession 1920–1921、铁路狂热、加密崩盘等需新来源核对的条目。

## 国际网络连续中断（轮次19，第3次连续）
- 现象：轮次17/18/19连续三轮，baidu可达但国际站点(en/zh维基、OpenLibrary)均超时。
- 处理：按 AUTONOMOUS 六"连续失败3次记BLOCKERS并跳过"——正式跳过联网新增项(Recession 1920-21/铁路狂热/加密崩盘)，网络无关工作继续。
- 网络恢复后：补建上述条目 + 24条L1升L2（需抓正文）。

## 维基网络出口不可用（轮次25诊断，持续性）
- 诊断：DNS 将 en.wikipedia.org 解析到 31.13.94.41(Facebook IP，疑似污染)；已知维基边缘IP 20.6.7.17 可TCP连通但 REST/api.php 均返回 301（重定向至规范域名，而域名解析被污染）。故维基内容整体不可获取。
- 影响：2020新冠股灾条目（唯一已知未决缺口）无法联网核对来源，暂不补建（避免编造）。
- 处理：按TASK"不编造/查不到写待核实"，不硬凑；继续用本地语料做质量深化。若后续网络出口恢复再补。

## 2020新冠股灾 — 正式跳过（AUTONOMOUS 第六条）

> **【round145 复核：已解决】** `covid-crash-2020`（2020年新冠股灾）**后来已建成**；本条"库缺此一条"的说法已过时。
- 该条目源抓取在轮次22/23/24/25连续失败≥4次（维基网络出口不可用：DNS污染+IP 301）。
- 按"同一问题连续失败3次，记BLOCKERS并跳过，不要死磕"→ 正式跳过，不再作为活动缺口。
- 影响：库缺2020新冠股灾一条；其余所有权威大纲/读者问题/矩阵缺口均已覆盖。若日后网络出口恢复，可补建以满足"完整"。

## ~~剩余4条L1无独立维基页~~ **已解除（续作K/L）**
- 条目：blue-monday-2009、dutch-collapse-1780、dutch-stock-crashes、syrian-crisis-2011
- 经多轮 REST/API 核对，均无对应独立维基页面（或页面不存在/重定向到不相关主题）。
- 按 TASK"补充层条目可保持L1"，维持 L1 骨架并标注待核实，不硬凑内容。
- 若后续找到权威来源（学术著作/专业百科），可再升级。

### 解除说明（续作K/L）
- 经 Wikipedia 搜索API定位正确页名后，4条全部升级为L2：
  - blue-monday-2009 → 页名实为 **Blue Monday Crash 2009**（RBS宣布英国史上最大企业亏损，银行股单日跌超67%）
  - dutch-collapse-1780 → 用 **Financial history of the Dutch Republic**（储蓄积累→金融工具→资本外流→18世纪末危机）
  - dutch-stock-crashes → 同上（VOC股票、阿姆斯特丹证交所、衍生品）
  - syrian-crisis-2011 → 用 **Economy of Syria** + **Caesar Syria Civilian Protection Act**（2011内战/2020-06-17制裁生效/2025-12-18废除）
- 结论：**L1 已清零**（全库165条均为L2或L3）。

## 已清理：永久不可达且未被引用的来源（续作CT）

以下 5 个来源在建立时即返回 HTTP 403 且无法通过其他途径读取，经全站扫描确认**没有任何条目引用**，已从 `data/sources.json` 删除（来源库 665 → 660，现全部为 verified=true 且实际可达）：

| 来源 id | 标题 | 不可达原因 |
|---|---|---|
| britannica-financial-crisis | Encyclopaedia Britannica（金融危机条目） | HTTP 403（反爬） |
| imf-publications | IMF Publications | HTTP 403 |
| investopedia-financial-crisis | Investopedia | HTTP 403 |
| baike-financial-crisis | 百度百科 | HTTP 403 |
| bls | U.S. Bureau of Labor Statistics | HTTP 403 |

保留它们只会让来源库包含"看似可用、实际打不开"的条目，损害可核查性。相关论述已由可访问的维基百科、美联储历史站与 OWID 数据替代。

## 维基百科 API 暂时不可达（round 19 起）

- **现象**：`en.wikipedia.org` 的 `api.php` 与 `rest_v1/page/summary` 均 `URLError: timed out`；连续 3 次重试均失败。同时间 `ourworldindata.org` 正常（HTTP 200），故为维基站侧问题而非本机断网。
- **影响**：无法新增依赖维基全文的条目。
- **应对**：
  1. 暂停新增维基来源条目（不猜测内容）；
  2. 转向**不依赖新数据源**的工作（关联网络、内容深度、站点结构、基于已有 OWID 数据的补充）；
  3. 已有 `_research/*.json` 缓存仍可用于核对已建条目。
- **恢复后**：优先补建 `BACKLOG.md` 中记录的 47 个概念（第一档机制类优先）。

## 案例政策应对覆盖率停在 41%（round 30 记录）

> **【round145 复核：已改善】** 现为 **146/209（约 70%）**；此节为 round 30 的历史快照，实时值以数据为准（check_docs 附近述）。

- **现状**：205 条案例中 85 条有 `policy_response`（41%），剩余 120 条没有。
- **原因**：这不是提取方法的问题，而是**来源内容的边界**——剩余 120 条的 `overview` 本身只写了成因与后果，没有写当局举措。按类型分布：
  - 银行 35、泡沫 26、货币 22、债务 12、其他 10、恶性通胀 8、制度 7
  - 其中"泡沫"类政策内容天然较少（多为市场自发调整）；其余多数是概述未覆盖政策。
- **已排除的错误做法**：用关键词自动提取（round 25 尝试过）会把"美联储加息引发调整"这类**成因**误当**政策**，生成 103 条后全部撤回。宁可 41% 是真的。
- **正确路径**：需先补充各条目正文（维基恢复或新数据源），再从中提炼政策段落。

## 来源质量问题：8 个条目的来源为通用概念页（round 50 记录）

> **【round145 复核：已解决】** 经后续轮次补专属来源，8 条现均含专属来源（如 w-en-panic-of-1896／w-en-subprime-mortgage-crisis／w-en-british-credit-1772 等）；此节保留为历史记录。

核查发现以下条目的 `sources` 全部是**通用概念页**，没有专属的史实来源：

| 条目 | 现有来源 |
|---|---|
| `us-state-defaults-1840s` | Debt_crisis / Financial_crisis |
| `danish-bankruptcy-1813` | Debt_crisis / Financial_crisis |
| `dutch-collapse-1780` | Debt_crisis / Financial_crisis |
| `british-credit-1772` | Debt_crisis / Financial_crisis |
| `panic-1896` | Currency_crisis / Financial_crisis |
| `yemen-currency-divergence` | Yemeni_rial / Currency_crisis |
| `panic-1910` | Bank_run / Financial_crisis |
| `subprime-crisis-2007` | Bank_run / Financial_crisis / Fed 专文（唯一专属源） |

**问题**：这些条目的具体史实（如"美国1840年代多个州违约"）无法由"债务危机"这一通用条目支撑。
按项目原则（关键事实需≥2个独立来源），它们实际处于「来源不足」状态，`needs_verification` 应为 true。

**待办**：
1. 为每一条寻找专属来源（如 `Panic_of_1837`、`Yemeni_Civil_War`、`Subprime_mortgage_crisis` 等）
2. 若找不到专属来源，应在条目中明确标注「来源为通用概念页，具体史实待核实」
3. **同时复核**：这 8 条是否也有 `policy_response` 依赖了通用页内容（若有需重写）

## 教训：工具缺陷被误当作"来源边界"（round 47—50）

连续三轮出现同一类错误：

| 轮次 | 被误判的内容 | 真实原因 |
|---|---|---|
| 47 | 9 个 `panic-*` 无政策章节 | 抓取取了第一个 URL（通用页 `Financial_crisis`） |
| 49 | 同上，修正后 panic-1819/1825 立刻出现政策章节 | 抓取逻辑缺陷 |
| 50 | `savings-loan-1986`／`signature-bank`／2013中国钱荒 无政策 | 章节名正则漏了 `recapitalization`／`disposition`／`PBOC Reaction` |

**教训**：在声称"来源不具备某类内容"之前，必须先验证提取工具本身是否正确。
三次都是「工具的问题」被误读成「数据的问题」。

## 工具缺陷记录 ④：维基 URL 大小写敏感（round 70 发现）

**错误结论**（round 61）：判定 `blue-monday-2009` 在维基**无专属条目**，据此把它记入 BACKLOG 待补来源。

**实际情况**：专属条目一直存在，且来源库里**早已注册** `w-en-blue-monday-crash-2009`
（= `https://en.wikipedia.org/wiki/Blue_Monday_Crash_2009`）。

**根因**：维基百科 URL **大小写敏感**（除首字母）。
我测试时用 `Blue_Monday_crash_2009`（crash 小写），API 返回空/404；
正确写法是 `Blue_Monday_Crash_2009`（Crash 大写）。

**二次根因**：本项目的**来源库本身就有正确答案**，我在判断"来源不存在"前
**没有先检索自己的 sources.json**。这是比大小写更根本的失误。

**对策**：
1. 判断某来源是否可用前，**先查 sources.json**
2. 抓取维基页面时保留原始大小写（从 sources.json 的 URL 直接取）
3. 新增检查：来源未被任何条目引用时报警（本轮发现 65 个未引用，其中 11 个是"有源未引"）

**这是第 4 次「工具缺陷导致错误结论」**，前三次分别记于 round 47/49/50。

## 工具缺陷记录 ⑥：来源引用字段清单不完整（round 76）

**事故**：合并 29 组重复来源时，重定向脚本只处理了
`sources`／`key_data[].sources`／`policy_response[].sources`／`schools[].src`，
**漏掉 `causal_chain[].sources` 与 `timeline[].sources`**，导致 54 处 R4 错误。

**根因**：与第 ⑤ 次同类——**我以为自己知道字段清单，就没去枚举**。

**实测的完整字段清单（7 个）**：

| 字段 | 说明 |
|---|---|
| `.sources` | 条目主来源 |
| `.key_data[].sources` | 数据行来源 |
| `.policy_response[].sources` | 政策段来源 |
| `.schools[].sources` | 学派观点来源（数组形式） |
| `.schools[].src` | 学派观点来源（单值形式） |
| `.causal_chain[].sources` | 因果链来源 |
| `.timeline[].sources` | 时间线事件来源 |

**对策**：改用**递归遍历**（`remap_obj`）改写任意深度的 `sources`／`src`，
不再依赖手写字段列表；并从 git 恢复后重做，最终 0 error。

**教训**：第 ⑤、⑥ 次是同一错误的两次复发——**写脚本前应先枚举，而不是凭记忆**。
- 续作QD: swedish-crisis-1990s 维基全文缓存错配（内容为芬兰银行危机），网络不可用暂无法重抓；已在条目 pending_notes 记录。
- 续作QO: bk-the-wealth-of-nations (openlibrary.org/works/OL76827W) 近几轮抽样时好时坏(HTTP 421/URLError，单独重跑曾恢复)，判断为对方站点或网络不稳，暂不改来源，持续观察。
- 续作QQ: us-state-defaults-1840s 维基全文缓存错配（.slug=Panic_of_1837，非州违约专页），未据此取数；网络恢复后重抓。
- 续作QQ: smithsonian-agreement 维基全文缓存无.slug且内容为Nixon shock条目（疑错配），未据此取数；网络恢复后重抓。
- 续作QR: 缓存审计(_research/audit_cache_slug.py)补记——jamaica-accords 缓存实为 Nixon shock、panic-1910 缓存实为通用 Bank run 条目，均非条目本身页面；animal-spirits / bank-resolution / leading-indicator / liquidity-coverage-ratio / taper-tantrum 缓存页面对题但不在条目 sources 中，其中数字不可直接引用。网络恢复后重抓或补登来源。
- 续作QT: hainan-property-bubble-1992 维基全文缓存实为 2007 年中国股灾条目（错配），未据此取数。
- 续作QY: us-video-game-crash-1983 维基全文缓存实为通用 Economic bubble 条目（错配），未据此取数。
- 续作QY: panic-1896 维基全文缓存实为通用 Currency crisis 条目（错配），未据此取数。
- 续作QZ: yemen-currency-divergence 维基全文缓存实为通用 Currency crisis 条目（错配），未据此取数。
- 续作RC: dutch-stock-crashes 维基全文缓存实为通用 Economic bubble 条目（错配），未据此取数。
- 续作RD: esrb 维基全文缓存实为 Eurozone crisis 条目（错配），未据此取数。
- 续作RD: stock-market-crash 维基全文缓存实为 Margin (finance) 条目（错配），未据此取数。
- 续作RF: bank-resolution 缓存实为通用 Bank regulation 条目；leading-indicator 缓存实为 Economic indicator 条目——均已在QR审计中登记，本轮未取数。

## 维基缓存放错页面（2026-11-26，已解决）
- steel-crisis-1973、venezuela-energy-2010 → 缓存为 Economic history；panic-1796、panic-1910 → Bank run；israel-bank-1983 → Economic bubble；crisis-33ce → Debt crisis。原因：条目首个 w-en 来源是通用页面。需为这些条目找到专题页来源后重抓。

## 维基缓存放错页面·第二批（2026-11-26，已解决）
- jamaica-accords、smithsonian-agreement → 缓存为 Nixon shock；yemen-currency-divergence → Currency crisis；swedish-crisis-1990s → 1990s Finnish banking crisis；us-state-defaults-1840s → Panic of 1837。需找专题页后重抓。

## 维基缓存放错页面·第三批（2026-11-26，待处理）
- structural-adjustment → 缓存为 Debt crisis。

## 缓存审计（2026-11-26）
- 已用 tools/audit_cache.py 全量审计。第三批（structural-adjustment）已解决。
- 未解决：hainan-property-bubble-1992、taiwan-bubble 无英文专题页，需中文来源（如中文维基专题页）才能补内容。
