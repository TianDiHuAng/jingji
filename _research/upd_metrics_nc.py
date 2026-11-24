# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))

note = """维基第112轮可用。NB-NC：抽查 timeline 数字，发现并修正一处**严重的"事件张冠李戴 + 无来源数字"**。
①系统抽查：对全部有全文的条目，提取 timeline 中"带单位数字"，核对是否在来源全文或自身 key_data 中——得 59 条"可疑"。
②逐一抽验（重点看几个）：确认绝大多数是**假阴性**——因缺"亿↔billion"换算（如"12亿美元"=原文 "$1.2 billion"、"420亿"="$42 billion"、"750亿"="$75 billion"），均已在来源中。抽查 albania/bank-crisis-2023/madoff/greek-debt/latin-american/dubai/mexican 等均证实数字属实。
③**但发现一处真实且严重的错误**：`blue-monday-2009` 的 one_line/overview/timeline 描述的是"**2009 年 3 月 2 日道指跌破 7000 点、标普 676 点**"，而其专属来源 `w-en-blue-monday-crash-2009` 实际描述的是"**2009 年 1 月 19 日英国银行股暴跌（RBS 公布英国史上最大亏损、股价跌逾 67%、政府持股升至 70%）**"；**7000/676 等数字在所引任何来源中都不存在**——两段不同事件被混为一谈，且含无来源数字。而 key_data 那三条（67%／280 亿英镑／70%）本已正确引自该来源，说明是"正文错、数据对"。
④**修正**：one_line/overview/timeline 全部改为与来源一致的 1 月 19 日英国银行股事件（RBS 巨亏 -67%、Lloyds -33%、Barclays -10%、HSBC -6%、次日续跌、政府拟持股 70%）；删除无来源的 3 月美股数字；crisis_type 由"泡沫"改为"银行"；comparison 与 `brexit-crash-2016` 中的相关表述同步更新；pending_notes 记录原委，并注明"2009 年 3 月美股见底约 676 点为另一事件，如需要应另建条目并补来源"。
⑤**教训**：这是**只有逐条比对"正文数字 vs 专属来源内容"才能发现**的错误——它通过了所有自动检查（数字有标注、结构完整），却犯了"把 A 事件的数字安到 B 事件上"的错。再次证明**抽查验证不可替代**。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 18/18。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NB-NC', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 59, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18',
    'spot_check': '抽查 timeline 数字（59 条疑点，多为换算假阴性）；修正 blue-monday-2009 的事件张冠李戴',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 112 轮可用（round 132）**。**抽查 timeline 数字，发现并修正一处严重的「事件张冠李戴 + 无来源数字」**。
- **系统抽查**：对全部有全文条目，提取 timeline 中「带单位数字」，核对是否在来源全文或自身 key_data 中——得 59 条「可疑」。
- **逐一抽验**：绝大多数是**假阴性**——因缺「亿↔billion」换算（「12亿美元」=原文「$1.2 billion」、「420亿」=「$42 billion」、「750亿」=「$75 billion」），均已在来源中。
- **但发现一处真实且严重的错误**：`blue-monday-2009`：

  | 位置 | 内容 |
  |---|---|
  | one_line／overview／timeline | 「**2009 年 3 月 2 日道指跌破 7000 点、标普 676 点**」 |
  | 专属来源 `w-en-blue-monday-crash-2009` | 「**2009 年 1 月 19 日英国银行股暴跌**（RBS 英国史上最大亏损、股价跌逾 67%、政府持股升至 70%）」 |

  **两段不同事件被混为一谈**，且 7000/676 在所引任何来源中都不存在。而 key_data 那三条（67%／280 亿英镑／70%）本已正确引自该来源——**是「正文错、数据对」**。

- **修正**：one_line／overview／timeline 全部改为与来源一致的 **1 月 19 日英国银行股事件**（RBS 巨亏 -67%、Lloyds -33%、Barclays -10%、HSBC -6%、次日续跌、政府拟持股 70%）；删除无来源的 3 月美股数字；`crisis_type` 由「泡沫」改为「银行」；`brexit-crash-2016` 的相关表述同步更新。
- **教训**：这是**只有逐条比对「正文数字 vs 专属来源内容」才能发现**的错误——它**通过了所有自动检查**（数字有标注、结构完整），却犯了「把 A 事件的数字安到 B 事件上」的错。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作MX-MY｜2026-11-24｜状态：641条；内容抽查，修复3处"未核实数字当事实"的不一致**',
              '**续作NB-NC｜2026-11-24｜状态：641条；修正blue-monday-2009事件张冠李戴+无来源数字**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
