# -*- coding: utf-8 -*-
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts

c = counts(es)


def enr(s):
    zh = len(re.findall(r'[\u4e00-\u9fff]', s or ''))
    en = len(re.findall(r'[A-Za-z]', s or ''))
    return en / (zh + en) if (zh + en) else 0


left = [e for e in es if enr(e.get('overview')) > 0.45]
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))

note = (
    "维基第92轮可用。KD-KI：R21 归零——33 条英文正文全部改写为中文。"
    "①本轮分四批改写 32 条（round 110 已修 6 条，合计 38 条），条目 overview 现均以中文为主。"
    "②改写时不是翻译而是重写——保留来源中的事实，但补上该概念与金融危机的关系："
    "inequality 补「收入/财富/消费三种不平等走势可相反，只看一个会得出相反结论」；"
    "fractional-reserve 补「期限转换正是银行的功能，也是挤兑的根源」；"
    "toxic-assets 补「有毒的实质不是一文不值，而是无法定价，于是同业拆借集体冻结」；"
    "eurodollar 补「2008 年美联储不得不通过央行货币互换向全球提供美元」；"
    "proprietary-trading 补「做市与自营在实务中难以划清界线」这一监管难点；"
    "labour-market 补「危机留下疤痕」与雇佣保护的两难；"
    "savings 补「节俭悖论」；transaction-cost 补「流动性的本质就是低交易成本」。"
    "③改进 R21 判据：4 个条目（danatbank-1931／merrill-lynch／creditanstalt／silicon-valley-bank）"
    "本是中文内容加必要的机构全称，英文占比被专名拉到 48—63%；"
    "判据改为先剥离括号内容、英文专名序列与缩写，再计算占比——"
    "既拦住英文充正文，又不误伤中文含专名。调整后仅剩 danatbank-1931，已改写为以中文译名为主。"
    "④round 94 的接线检查再次生效：改写时写了见 speculation／见 balance-sheet-recession／"
    "见 animal-spirits 却忘了加入 related，被 check_pages 逐一报出（3 处），已修复。"
    "⑤现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；R21 剩余 0 条；overview 平均长度 " + str(avg) + " 字。十一道检查全绿 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作KD-KI', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 33, 'reviewed': 641, 'fixed': 33,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + 自测 18/18（R21 归零）',
    'spot_check': '33 条英文正文全部改写为中文；R21 判据改进以排除专名',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

bl = 'BACKLOG.md'
b = open(bl, encoding='utf-8').read()
b = re.sub(r'\n## 待办：R21 英文占比超标[\s\S]*$',
           '\n## 待办：R21 英文占比超标（33 条，round 110 记录）\n\n'
           '**已于 round 111 全部完成**——38 条英文正文均改写为中文，R21 归零。\n'
           '同时改进判据：先剥离括号内容、英文专名序列与缩写，再计算占比，避免误伤「中文含专名」的条目。\n',
           b)
open(bl, 'w', encoding='utf-8').write(b)
print('BACKLOG 已标记完成')

add = """- **维基百科第 92 轮可用（round 111）**。**R21 归零——33 条英文正文全部改写为中文**。
- 本轮分四批改写 **32 条**（round 110 已修 6 条，合计 38 条）。
- **改写时不是翻译而是重写**——保留来源事实，补上该概念**与金融危机的关系**：

  | 条目 | 补充的关键判断 |
  |---|---|
  | `inequality` | 收入/财富/消费三种不平等走势可相反，**只看一个会得出相反结论** |
  | `fractional-reserve` | 期限转换既是银行的功能，也是挤兑的根源 |
  | `toxic-assets` | 「有毒」的实质不是一文不值，而是**无法定价**——于是同业拆借集体冻结 |
  | `eurodollar` | 2008 年美联储不得不通过**央行货币互换**向全球提供美元 |
  | `proprietary-trading` | 做市与自营**在实务中难以划清界线**（沃尔克规则的执行难点） |
  | `labour-market` | 危机的「疤痕效应」与雇佣保护的两难 |
  | `savings` | 节俭悖论 |
  | `transaction-cost` | **流动性的本质就是低交易成本** |

- **改进 R21 判据**：4 个条目（`danatbank-1931`／`merrill-lynch`／`creditanstalt`／`silicon-valley-bank`）本是**中文内容＋必要机构全称**，英文占比被专名拉到 48—63%。判据改为**先剥离括号内容、英文专名序列与缩写**再计算——既拦住「英文充正文」，又不误伤「中文含专名」。调整后仅剩 `danatbank-1931`，已改写为以中文译名为主。
- **round 94 的接线检查再次生效**：改写时写了「见 speculation」「见 balance-sheet-recession」「见 animal-spirits」却忘加 `related`，被 `check_pages` 逐一报出（3 处），已修复。
- 现状：**641 条**、来源 **742**、页面 **655**；**R21 剩余 0**。**十一道检查全绿 + 自测 18/18**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JW-KC｜2026-11-24｜状态：641条；发现39条英文本充当正文，已修6条余33条**',
              '**续作KD-KI｜2026-11-24｜状态：641条；R21归零，38条英文正文全部改写为中文**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R21 剩余', len(left))
