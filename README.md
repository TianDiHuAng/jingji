# 经济史与金融危机案例库

一个数据驱动、机器校验、诚实标注的静态知识库网站，按「时期 × 地区 × 危机类型」组织 106 个案例与理论制度条目。

## 目录结构

```
.
├── scope.md              范围清单（三份权威大纲取并集，106条）
├── coverage.json         覆盖数据（层级/状态/来源数/待核实）
├── COVERAGE_MATRIX.md    覆盖矩阵（时期×类型×地区 + 空白清单）
├── DECISIONS.md          无人值守决策记录
├── PROGRESS.md           进度与续跑起点（含 ALL_DONE）
├── REPORT.md             项目报告（统计/验证/空白格子）
├── RECHECK.md            批次复检报告
├── data/
│   ├── sources.json      来源库（180条，逐条核对 verified）
│   └── entries/*.json    106 个条目（L1/L2）
├── tools/
│   ├── check.py          数据层校验器 R1–R15
│   ├── gen_site.py       静态站点生成器
│   ├── check_links.py    站点终检（链接/SVG/图片禁用）
│   ├── check_quality.py  HTML结构检查（标题层次/重复id/meta/表格th等10项）
│   ├── check_kd.py       key_data 数值可核对性（对照来源全文）
│   ├── check_polnum.py   policy_response 数字核对（含亿/万换算）
│   ├── check_sources.py  来源可达性抽样（verified=true 是否真可达）
│   ├── check_body_num.py 正文数字溯源（overview/comparison/one_line）
│   └── check_docs.py     文档统计一致性（PROGRESS/REPORT 与真实数据）
└── site/
    ├── index.html        首页
    ├── style.css         浅/深双模式样式（CSS变量）
    ├── unit-*.html       单元页 ×6
    ├── <id>.html         条目页 ×106
    └── index-all / timeline / sources / matrix 页
```

## 复现

```bash
python tools/check.py         # 数据校验：0 error
python tools/gen_site.py      # 生成 site/，自动核验站内断链
python tools/check_links.py   # 站点终检：0 error
python tools/check_quality.py # HTML结构检查：0 problem
python tools/check_kd.py      # key_data 数值核对：对照来源全文
python tools/check_polnum.py  # 政策段数字核对：392个全部可溯源
python tools/check_sources.py # 来源可达性抽样（默认30个）
python tools/check_body_num.py # 正文数字溯源（排除年份引用）
python tools/check_docs.py    # 文档统计一致性核对
```

## 设计原则

- **数据驱动**：改 JSON 重跑生成器即可，不手改 HTML
- **机器校验强制诚实**：双源规则、待核实、争议并列由 check.py 拒绝坏数据
- **诚实标注**：不编造数字/日期/人名；查不到标「待核实」；关键事实需两个 verified 来源
- **零依赖**：纯静态 HTML+CSS，无 JS、无图片，图示全为内联 SVG
