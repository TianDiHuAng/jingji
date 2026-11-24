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

note = """维基第111轮可用。MX-MY：内容抽查验证——审阅 check_kd 的 52 条"未匹配"，发现并修复 3 处"简介称未载、正文却当事实陈述"的不一致。
①审阅 check_kd 全部 52 条"未匹配" key_data：逐一核对后均为合法情形——单位换算（0.4 百万里弗=40万；1900=19亿）、spelled-out 数字（twelve=12、"more than half"=50%）、OWID／世界银行数据（不同来源，不在维基全文中）、中文维基来源（taiwan-bubble）、以及由两年数据推导的增长率。无抄写错误。
②另核 3 条标注"两源有差异"的条目（german-crisis-2022／russian-crisis-2014／venezuela-hyper-2016）——均在 key_data 并列两数、overview 提及口径差异，符合"两源差异并列"规则。
③随机抽查 12 条有全文条目的 overview 数字：36 个数字中 5 个未在全文找到，逐一核对——多为"127号文"这类文号与月份（假阳性）。
④但发现一处真实不一致：dotcom-bubble-2000 的 overview 明确称"现行来源未载 2619%／1000%／900%"，而 timeline 却写"高通股价上涨2619%，多只大盘股涨超1000%"——自相矛盾且违反"不编造数字"。已修复 timeline（改为"涨幅惊人，具体数值待核实"）。
⑤同时清理 finnish-banking-1990 与 panic-1901 的 disclaimer 中复述的未核实数字（"近零升至近20%"、"170/1000 美元"）——未核实数字不应在任何位置复述。
⑥**这是"字段填满"审计无法发现、只有逐条内容抽查才能发现的问题**——印证了从"填充结构"转向"验证内容"的必要。
⑦现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；check_body_num 未匹配 92→90（真实减少 2 个未核实数字）；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 18/18。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作MX-MY', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 52, 'fixed': 3,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18',
    'spot_check': '抽查 52 条未匹配 key_data（均合法）；修复 3 处未核实数字不一致',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 111 轮可用（round 131）**。**内容抽查验证——审阅 check_kd 的 52 条「未匹配」，发现并修复 3 处「简介称未载、正文却当事实陈述」的不一致**。
- **审阅 52 条「未匹配」key_data**：逐一核对后**均为合法情形**——单位换算（0.4 百万里弗=40万；1900=19亿）、spelled-out 数字（twelve=12、「more than half」=50%）、OWID／世界银行数据（不同来源，不在维基全文中）、中文维基来源、以及由两年数据推导的增长率。**无抄写错误。**
- **核 3 条「两源有差异」条目**（german-crisis-2022／russian-crisis-2014／venezuela-hyper-2016）——均在 key_data 并列两数、overview 提及口径差异，符合规则。
- **随机抽查 12 条有全文条目的 overview 数字**：36 个数字中 5 个未在全文找到，多为「127号文」这类文号与月份（假阳性）。
- **发现一处真实不一致**：`dotcom-bubble-2000` 的 overview 明确称「现行来源未载 2619%／1000%／900%」，而 timeline 却写「高通股价上涨2619%，多只大盘股涨超1000%」——**自相矛盾且违反「不编造数字」**。已修复 timeline。
- **同时清理** `finnish-banking-1990` 与 `panic-1901` 的 disclaimer 中复述的未核实数字。
- **这是「字段填满」审计无法发现、只有逐条内容抽查才能发现的问题**——印证了从「填充结构」转向「验证内容」的必要。
- 现状：**641 条**、来源 **742**、页面 **655**；`check_body_num` 未匹配 **92→90**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作MV-MW｜2026-11-24｜状态：641条；6条补第二派schools，两派对照达625条**',
              '**续作MX-MY｜2026-11-24｜状态：641条；内容抽查，修复3处"未核实数字当事实"的不一致**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
