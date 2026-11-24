# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts
c = counts(es)
import re


def enr(s):
    zh = len(re.findall(r'[\u4e00-\u9fff]', s or ''))
    en = len(re.findall(r'[A-Za-z]', s or ''))
    return en / (zh + en) if (zh + en) else 0


left = sorted([(e['id'], round(enr(e.get('overview')) * 100)) for e in es
               if enr(e.get('overview')) > 0.45], key=lambda x: -x[1])

note = (
    '维基第91轮可用。JW-KC：**发现 39 个条目以英文摘要充当正文——已完成 6 条改写，余 33 条记为待办**。'
    '①**发现路径**：先完成最后一条单薄概念 `subordination`（183→567 字，含"被降低的是收债权位而非债务本身"、'
    '三种形态、与二级资本及 bail-in 的关系）；随后扫描"既无 timeline 也无 key_data"的概念，'
    '得 343 条——但逐一查看后判断**多数为纯抽象概念（机会成本、弹性、边际效用），无时序与数值本属合理**，'
    '不强行补。**转而检查"完全没有 schools"的 16 条**，由此打开真正的缺口。'
    '②**关键发现**：那 16 条的 overview **全是英文**，格式为「（据 Wikipedia「X」摘要归纳）+ 英文原文 + 待核实」，'
    '系早期批量生成。遂全库扫描：**39 个条目 overview 英文占比 >45%（多为 94—96%）**。'
    '**中文站点的主体内容不应是英文**——这是比 schools 缺失更严重的问题。'
    '③**加入 R21 检查**（overview 英文占比须 ≤45%），首次运行即捕获 **39 条**。'
    '④**首批改写 6 条为中文**：`market-failure`（市场失灵：帕累托效率、1958 年首次使用、'
    '词源溯至密尔与西季威克、公共品/时间不一致/信息不对称/竞争不足/外部性，'
    '并说明金融监管的正当性正建立于此）、`utility`（效用的规范与描述两种含义、序数效用不可人际比较）、'
    '`recession`（广泛收缩、触发因素、识别门槛无唯一标准）、'
    '`prisoners-dilemma`（1950 年 Flood 与 Dresher 于兰德公司设计；'
    '**与挤兑的关系**：对每家银行"先跑"都理性，存款保险/最后贷款人/银行假日正是改变支付结构）、'
    '`counterparty-risk`（比"违约"更宽——即使双方善意且有能力，结算过程本身也可能中断；'
    'DvP／净额结算／CCP 三种缓释；雷曼时因无法确定净敞口而冻结同业拆借）、'
    '`modigliani-miller`（MM 说的是**企业价值**不受融资方式影响，不是股权价值；'
    '其价值在于标出现实偏离理想的条件，并延伸至"提高银行资本要求不必然抬高总资金成本"）。'
    '⑤**R21 保留为 error 不降级**：现有 **33 条待修**（`inequality`／`population`／`rent-seeking`／'
    '`fractional-reserve`／`convergence`／`equity-premium`／`specialization`／`tax-incidence`／'
    '`payment-system`／`investment`／`recession` 已修等），已列入 BACKLOG。'
    '**检查暂时不"全绿"是如实反映问题**，而不是回退标准。'
    '⑥现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    'R21 待修 33 条。其余十道检查全绿 + 自测 18/18。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JW-KC', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 7, 'reviewed': 641, 'fixed': 7,
    'sources_total': len(srcs),
    'check_result': 'PASS(10/11); R21 新增并捕获 39 条，已修 6 条，余 33 条待办',
    'spot_check': '发现 39 个条目以英文摘要充当正文；subordination 深化',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# BACKLOG 记录
bl = 'BACKLOG.md'
b = open(bl, encoding='utf-8').read()
add_bl = '''
## 待办：R21 英文占比超标（33 条，round 110 记录）

**问题**：以下条目的 `overview` 以英文摘要充当正文（英文占比 49—96%），中文站点不应如此。
**已完成**：market-failure／utility／recession／prisoners-dilemma／counterparty-risk／modigliani-miller（6 条）。
**待修 33 条**（按英文占比降序，括号内为占比%）：

'''
for eid, r in left:
    add_bl += '- `%s`（%d%%）\n' % (eid, r)
add_bl += '''
**修法**：读该条目的 `_research/wiki_full/<id>.txt`，用中文重写 overview，
保留原有事实与 sources，不新增无据内容；改完跑 `check.py` 确认 R21 不再报错。
'''
if 'R21 英文占比超标' not in b:
    b = b.rstrip() + '\n' + add_bl
    open(bl, 'w', encoding='utf-8').write(b)
    print('BACKLOG 已记录 33 条待修')

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 91 轮可用（round 110）**。**发现 39 个条目以英文摘要充当正文——已完成 6 条改写，余 33 条记为待办**。
- **发现路径**：先完成最后一条单薄概念 `subordination`（183→567 字）；随后扫描“既无 timeline 也无 key_data”的概念得 **343 条**——但逐一查看后判断**多数为纯抽象概念（机会成本、弹性、边际效用），无时序与数值本属合理**，不强行补。**转而检查“完全没有 schools”的 16 条**，由此打开真正的缺口。
- **关键发现**：那 16 条的 overview **全是英文**，格式为「（据 Wikipedia「X」摘要归纳）+ 英文原文 + 待核实」，系早期批量生成。全库扫描：**39 个条目 overview 英文占比 >45%（多为 94—96%）**。**中文站点的主体内容不应是英文。**
- **加入 R21 检查**（overview 英文占比须 ≤45%），首次运行即捕获 **39 条**。
- **首批改写 6 条为中文**：

  | 条目 | 改写要点 |
  |---|---|
  | `market-failure` | 帕累托效率、**1958 年**首次使用、词源溯至密尔与西季威克；**金融监管的正当性正建立于此** |
  | `utility` | 规范与描述两种含义；**序数效用不可人际比较** |
  | `recession` | 广泛收缩、触发因素、**识别门槛无唯一标准** |
  | `prisoners-dilemma` | **1950 年** Flood 与 Dresher 于兰德公司设计；**与挤兑的关系**——“先跑”对每家都理性，存款保险/最后贷款人/银行假日正是改变支付结构 |
  | `counterparty-risk` | 比“违约”更宽（双方善意且有能力时结算仍可能中断）；DvP／净额结算／CCP；雷曼时因无法确定净敞口而冻结同业拆借 |
  | `modigliani-miller` | MM 说的是**企业价值**而非股权价值；延伸至“提高银行资本要求不必然抬高总资金成本” |

- **R21 保留为 error，不降级**：现有 **33 条待修**，已列入 `BACKLOG.md`（含逐条占比清单与修法）。**检查暂时不“全绿”是如实反映问题，而不是回退标准。**
- 其余十道检查全绿 + 自测 18/18。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JU-JV｜2026-11-24｜状态：641条；深化债务陷阱外交（两派并列）与全球债务**',
              '**续作JW-KC｜2026-11-24｜状态：641条；发现39条英文本充当正文，已修6条余33条**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R21 剩余', len(left))
