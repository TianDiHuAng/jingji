# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts

c = counts(es)
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))
nsch = sum(1 for e in es if e.get('schools'))
ncmp = sum(1 for e in es if e.get('comparison'))
thin = [e for e in es if len(e.get('overview') or '') < 150]

note = (
    "维基第107轮可用。ME-MG：**全面质量审计 + 为 11 条概念补 schools**。"
    "①**审计结果（不依赖网络）**："
    "overview 长度分布 — <150: 19（全为补充类机构条目，按既定政策可接受）、"
    "150-249: 106、250-399: 144、400-599: 295、≥600: 77；"
    "comparison 覆盖 578/641（90%）、related 641/641（平均 7.3 条）、"
    "schools 625/641、timeline 288/641、key_data 211/641；"
    "**案例中 key_data 与 timeline 双缺的为 0**、**核心/重要案例缺 timeline 的为 0**。"
    "②**发现两个结构性缺口**：缺 comparison 63 条（多为案例）、缺 schools 16 条。"
    "③**本轮补 schools 11 条**——选择**确有学术分歧**的概念，"
    "每条给出两派观点并标注到该条目已有来源："
    "market-failure（新古典干预 vs 公共选择／奥地利）、utility（规范 vs 描述）、"
    "recession（量化门槛 vs 机构判定）、growth（增长优先 vs 限度代价）、"
    "prisoners-dilemma（一次性 vs 重复博弈）、convergence（无条件 vs 条件收敛）、"
    "specialization（效率 vs 脆弱性）、investment（实物资本 vs 金融资产）、"
    "toxic-assets（无法定价 vs 价格下跌）、eurodollar（效率 vs 监管风险）、"
    "expectations（适应性 vs 理性预期）。"
    "**未强行为机构类条目（nasdaq／mutual-fund／dividend／buyback／population）编造分歧**——"
    "没有真实争论时，留空优于虚构。schools 覆盖升至 636/641。"
    "④现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；comparison " + str(ncmp) +
    "、schools " + str(nsch) + "；**ERRORS 0、WARNINGS 0**。"
    "⑤**遗留**：3 条案例仍缺维基全文（网络持续不可用），具体细节已在 pending_notes 标注待补。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作ME-MG', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 11, 'reviewed': 641, 'fixed': 11,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18',
    'spot_check': '全面质量审计；为 11 条概念补两派 schools',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 107 轮可用（round 127）**。**全面质量审计 + 为 11 条概念补 schools**。
- **审计结果（不依赖网络）**：

  | 维度 | 结果 |
  |---|---|
  | overview 长度 | <150: 19（全为补充类机构条目，按既定政策可接受）／150-249: 106／250-399: 144／400-599: 295／≥600: 77 |
  | `comparison` | 578/641（90%） |
  | `related` | 641/641（平均 **7.3** 条） |
  | `schools` | 625/641 |
  | `timeline` / `key_data` | 288 / 211 |
  | 案例 key_data 与 timeline 双缺 | **0** |
  | 核心/重要案例缺 timeline | **0** |

- **发现两个结构性缺口**：缺 `comparison` 63 条（多为案例）、缺 `schools` 16 条。
- **本轮补 schools 11 条**——选择**确有学术分歧**的概念，每条给出两派观点并标注到该条目已有来源：

  | 概念 | 两派 |
  |---|---|
  | `market-failure` | 新古典干预 vs 公共选择／奥地利 |
  | `utility` | 规范（目标函数）vs 描述（偏好表示） |
  | `recession` | 量化门槛 vs 机构判定 |
  | `growth` | 增长优先 vs 限度代价 |
  | `prisoners-dilemma` | 一次性 vs 重复博弈 |
  | `convergence` | 无条件 vs 条件收敛 |
  | `specialization` | 效率 vs 脆弱性 |
  | `investment` | 实物资本 vs 金融资产 |
  | `toxic-assets` | 无法定价 vs 价格下跌 |
  | `eurodollar` | 效率 vs 监管风险 |
  | `expectations` | 适应性 vs 理性预期 |

- **未强行为机构类条目（nasdaq／mutual-fund／dividend／buyback／population）编造分歧**——没有真实争论时，留空优于虚构。`schools` 覆盖升至 **636/641**。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。遗留：3 条案例仍缺维基全文（网络持续不可用）。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LW-MD｜2026-11-24｜状态：641条；扩写剩余13条案例，R22归零（全部完成）**',
              '**续作ME-MG｜2026-11-24｜状态：641条；质量审计+补11条schools两派观点**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', ncmp, '| schools', nsch, '| thin', len(thin), '| avg', avg)
