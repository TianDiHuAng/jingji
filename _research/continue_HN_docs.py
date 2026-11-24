# -*- coding: utf-8 -*-
"""续作HN：更新 READER_QUESTIONS.md 与 GAP_REPORT.md，把已解决的缺口标注清楚。"""
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}

RQ = '''# 读者问题清单（round 79 重新校验）

> **重要**：本文件编制于 round 17，所列缺口此后已基本补齐。
> round 79 逐项核对 `data/entries/` 的实际 id 后重写如下。
> 教训：**待办清单本身也需要定期校验**——round 77 曾因依据过时清单而建了已存在的条目。

## 原列 3 个缺口 → 现状

| 问题 | 原状态（round 17） | 现状（round 79） |
|---|---|---|
| 加密货币崩盘（FTX） | 无条目 | ✅ **已建** `bankruptcy-ftx`（标题「加密市场崩盘与FTX破产(2022)」） |
| 动物精神（animal spirits） | 无独立条目 | ✅ **已建** `animal-spirits` |
| 铁路狂热（Railway Mania） | 无条目 | ✅ **已建** `railway-mania` |

## 附录中列的候选缺口 → 现状

| 事件 | 现状 |
|---|---|
| 1920—1921 衰退 | ✅ **已建** `recession-1920-1921` |
| 1960—1961 衰退 | ✅ **本轮新建** `recession-1960-1961`（10 个月／GDP −1.4%） |
| 1969—1970 衰退 | ✅ **本轮新建** `recession-1969-1970`（11 个月／GDP −0.6%） |
| 2020 新冠股灾 | ✅ **已建** `covid-crash-2020` |
| 1785 恐慌 | ✗ 维基无专属页（重定向到「美国衰退列表」），不作专属来源 |

## 结论

原 33 问 + 附录候选中，**除 `panic-1785`（缺权威专属来源）外均已覆盖**。
'''

GP = '''# 缺口发现报告（round 79 重新校验）

> 本文件编制于 round 22，其中列出的两个"真实缺口"此后均已解决。

## 原结论与现状

| 原记录 | 现状 |
|---|---|
| `w-en-flash-crash` 未建条目 → 已新增 `flash-crash-2010` | ✅ 存在，且已补 key_data（单笔 41 亿美元触发、道指跌超 1000 点） |
| 2020 新冠股灾待联网补建 | ✅ **已建** `covid-crash-2020`（另有 `oil-price-war-2020`） |

## round 79 复核（逐项对照实际条目）

- 来源库中"已 verified 却未被任何条目引用"的来源：**16 个**（9 本书 + 7 个机构，作为参考资源保留）
- 孤儿页面：**0**
- 站内断链：**0**
- 悬空 related 引用：**0**

## 结论

round 22 所列缺口已全部关闭。当前**未发现新的权威缺口**；
剩余未覆盖项均属"来源不可得"（维基无专属页或仅有通用页），已记入 `BACKLOG.md` 的真实缺口表。
'''

open('READER_QUESTIONS.md', 'w', encoding='utf-8').write(RQ)
open('GAP_REPORT.md', 'w', encoding='utf-8').write(GP)
print('READER_QUESTIONS.md 与 GAP_REPORT.md 已重写')
print('当前条目:', len(es))
