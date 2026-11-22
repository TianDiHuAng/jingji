# BACKLOG.md — 待办队列（轮次3生成）

优先级规则：核心＞重要＞补充；被引用多的优先；覆盖稀疏维度优先；复核/修复优先于新增。

## 队列（按执行顺序）

| id | 类型 | 优先级 | 依据（缺口来源） |
|---|---|---|---|
| L3-batch1 | 升级L3 | 核心-P0 | 缺口发现方法1：26条核心全停L2，TASK要求L3给核心 |
| L3-batch2 | 升级L3 | 核心-P0 | 同上（16条） |
| NEW-banking-crises | 新条目×9 | 重要-P1 | 方法6权威大纲对照：List_of_banking_crises 发现9条遗漏且有可核对维基页 |
| FIX-lowsrc | 修复来源 | 核心-P1 | 方法5：6条理论条目来源数<2（austrian-theory等） |
| REVIEW-pending | 复核待核实 | 补充-P2 | 方法4：106/106 待核实，抽核心条目复核数值 |

## L3-batch1 明细（核心条目前10条，优先标志性案例）
1. tulip-mania-1637（已L2，样板深化）
2. south-sea-bubble-1720
3. wall-street-1929
4. great-depression
5. weimar-hyper-1921
6. hungarian-hyper-1945
7. subprime-crisis-2007
8. euro-area-crisis
9. greek-debt-crisis
10. latin-american-debt-1975

## L3-batch2 明细（核心条目后16条）
gold-standard, central-bank, bretton-woods, business-cycle, minsky-theory, oil-crisis-1973, panic-1857, panic-1873, panic-1907, mississippi-bubble-1720, mexican-peso-1994, argentina-crisis-2001, japan-asset-bubble-1990, dotcom-bubble-2000, zimbabwe-hyper-2007, venezuela-hyper-2016

## NEW-banking-crises 明细（新条目，来源已核对存在）
black-friday-1869, russian-1998, uruguay-2002, finnish-banking-1990, indian-1991, cypriot-2013, myanmar-2003, henan-2022, ltcm

## 执行说明
- 本轮先执行 L3-batch1（10任务），剩余配额按质量闸结果决定
- 每完成10任务运行 check.py + git commit
- 新条目单轮≤10条（协议四），本轮9条合规
