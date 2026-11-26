# 概念条目 → 危机案例 关联说明

本目录记录 2026-11-26「第 3 项：概念条目补关联案例」的人工映射与执行脚本。

## 文件

- `concepts.tsv`：432 个 U6 概念条目的 id / 标题 / 当时案例链接数 / 一句话（工作底稿）
- `cases.tsv`：209 个案例条目的 id / 标题 / 时期 / 地区 / 一句话（工作底稿）
- `map.py`：概念 id → 案例 id 列表的**人工映射表**（本目录唯一事实来源）
- `apply.py`：把 `map.py` 合并进 `data/entries/*.json` 的脚本（只追加、不删除，排序并保持 CRLF）
- `README.md`：本说明

## 判断规则

1. 只收「该概念能解释案例的传导机制」或「该案例是该概念的典型例证」的组合；
2. 不按 `crisis_type` 批量套用，不按字母序/标题关键词自动生成；
3. 不为了凑覆盖率把机构条目（ADB、AfDB、AIIB、EBRD、IDB、IAIS、IOSCO、OECD 等）强行关联到无关案例；
4. 跨类链接保持**单向**（概念→案例），案例页不因新增链接而回指；站点渲染时按 `unit` 自动分组为「相关概念 / 相关危机案例」。

## 覆盖结果（2026-11-26）

- 概念条目总数：432
- 至少 1 条案例链接的概念条目：**101 → 272**
- 概念→案例边：**145 → 442**（净增 297 条，未删除既有链接）
- 相关映射的典型类别：
  - 银行/货币机制：`bank-run`、`deposit-insurance`、`lender-of-last-resort`、`moral-hazard`、`maturity-transformation` 等 → 北岩、Danat、罗得岛、储贷危机、大陆伊利诺伊等
  - 货币/汇率：`hyperinflation`、`currency-crisis`、`currency-board`、`dollarization`、`original-sin` 等 → 魏玛、津巴布韦、亚洲 1997、阿根廷 2001、土耳其 2018 等
  - 债务/主权：`sovereign-default`、`debt-restructuring`、`haircut-finance`、`odious-debt` 等 → 阿根廷 2001、希腊、斯里兰卡、海地独立债务等
  - 市场/工具：`securitization`、`cds`、`spv`、`value-at-risk`、`margin-call` 等 → 次贷、AIG、安然、LTCM、Archegos、英国 LDI 等
  - 泡沫/危机：`speculative-bubble`、`herd-behavior`、`ponzi-scheme`、`minsky-theory` 等 → 郁金香、南海、麦道夫、阿尔巴尼亚、次贷等

## 重跑

```bash
python -X utf8 _research/related/apply.py   # 幂等：已在 related 中的 id 不会重复添加
python -X utf8 tools/check.py
python -X utf8 tools/gen_site.py
```

修改映射前请先确认案例 id 在 `data/entries/` 中存在（`apply.py` 会拒绝未知概念 id；未知案例 id 会被忽略并在校验时暴露）。
