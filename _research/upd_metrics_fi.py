# -*- coding: utf-8 -*-
import json, glob
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
rest = [e for e in cases if not e.get('policy_response')]
pct = wp * 100 // len(cases)

note = (
    '维基第31轮可用。FG/FH/FI三步，案例政策覆盖 56%→' + str(pct) + '%（' + str(wp) + '/' + str(len(cases)) + '）。'
    '**关键发现：抓取逻辑缺陷**——此前脚本"取第一个维基来源 URL"，'
    '而多个 panic-* 条目的首个来源是通用页 Financial_crisis（42005字符，章节为 Types/Banking crisis/Currency crisis），'
    '导致我把它们的政策章节误判为"通用讨论"而跳过。'
    '修正：改为按"slug 与条目 id 的词重叠数"打分、跳过通用页（Financial_crisis/Bank_run/Bank/Bailout/Stock_market_crash），'
    '重抓45个案例，随即在 panic-1819/1825 等条目中发现了真正的政策章节。'
    '这是"检查工具本身的缺陷"，与前几轮的教训同类。'
    '本轮补写8条：委内瑞拉2016（放弃2003年起的价格与货币管制，2019年9月54%交易用美元、马拉开波86%）、'
    '叙利亚（2025.8宣布去两个零、12.29公布新钞）、乌拉圭（1962年授权美元存款的长期美元化制度）、'
    '第二合众国银行（抑制州银行纸币无序扩张）、日本泡沫（BoJ贴现率5.00%→2.50%属成因、1993年财政扩张属应对且效果不及预期）、'
    '希腊（支出增87% vs 税收增31%；评估结构改革不足需紧缩）、'
    '1825恐慌（推动1855有限责任法、1856/1862公司法）、1819恐慌（第二合众国银行两大监管目标）。'
    '剩余' + str(len(rest)) + '个案例按类型：' + str(dict(Counter(e['crisis_type'] for e in rest))) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FG-FI', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 8, 'reviewed': 84, 'fixed': 1,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '案例政策覆盖 56%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FF（再补10条，案例政策56%）',
              '- 当前轮次：续作FG-FI（修正抓取逻辑后补8条，案例政策60%）')
entry = '''- **维基百科第 31 轮可用**。案例政策覆盖 **56% → 60%（123/205）**。
- **本轮的关键发现：抓取逻辑本身有缺陷**。
  - 此前脚本"取第一个维基来源 URL"，而多个 `panic-*` 条目的**首个来源是通用页** `Financial_crisis`（42005 字符，章节为 Types / Banking crisis / Currency crisis…）
  - 结果我把它们的政策章节**误判为"通用讨论"而跳过**
  - 修正：按"slug 与条目 id 的**词重叠数**"打分，并跳过通用页（`Financial_crisis` / `Bank_run` / `Bank` / `Bailout` / `Stock_market_crash`），重抓 **45 个**案例——随即在 `panic-1819`、`panic-1825` 中发现了真正的政策章节
  - **这是"检查工具本身的缺陷"**，与前几轮（分类器、统计口径、HTML 结构检查）的教训同类
- 本轮补写 8 条：

  | 案例 | 政策应对 |
  |---|---|
  | 委内瑞拉 2016 | 放弃 2003 年起的价格与货币管制；2019年9月 **54%** 交易用美元（马拉开波 86%） |
  | 叙利亚 | 2025.8 宣布**去两个零**；12.29 央行公布新钞面额 |
  | 乌拉圭 2002 | **1962 年**授权美元存款的长期美元化制度安排 |
  | 第二合众国银行 | 抑制州银行纸币无序扩张（监管职能） |
  | 日本泡沫 1990 | BoJ 贴现率 **5.00%→2.50%**（成因）；1993 年财政扩张（应对，**效果不及预期**） |
  | 希腊债务危机 | 支出增 **87%** vs 税收增 **31%**；评估结构改革不足、需紧缩 |
  | 1825 恐慌 | 推动 **1855 有限责任法**、1856/1862 公司法 |
  | 1819 恐慌 | 第二合众国银行两大监管目标（恢复兑换＋扩大信贷可及性） |
- 剩余 86 个案例无政策章节，按类型：泡沫 22 / 银行 23 / 货币 14 / 债务 10 / 恶性通胀 6 / 其他 6 / 制度 5。
- 三道检查全绿。现状：**625 条**、来源 727、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FF｜2026-11-24｜状态：625条；案例政策覆盖56%**',
              '**续作FG-FI｜2026-11-24｜状态：625条；案例政策覆盖60%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 案例政策', wp, '/', len(cases), '=', pct, '%')
print('剩余按类型:', dict(Counter(e['crisis_type'] for e in rest)))
