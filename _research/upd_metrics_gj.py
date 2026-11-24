# -*- coding: utf-8 -*-
import json, glob, re, os

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
tl = sum(len(e.get('timeline', [])) for e in es)
sc = sum(len(e.get('schools', [])) for e in es)
thin = sum(1 for e in es if not (e.get('timeline') or e.get('schools')))

note = (
    '维基第46轮可用。GG-GJ：**为 13 个"内容薄弱"的概念条目补充实质内容**。'
    '①先抓取 29 个"仅 5 个区块"条目的维基全文（均 5千—7万字符），'
    '说明来源充足，此前只是建条目时仅取了 REST 摘要（几百字符）。'
    '②为 7 个补充：counterparty-risk（赫斯塔特银行 1974.6.26 牌照吊销、德崇 1990 未引发同类问题、'
    '英央行专设安排）、dividend（VOC 1602—1800 年付约 **18%** 股息、1902 年"不干预"原则判例）、'
    'convergence（Sachs-Warner 111国 1970—89 研究、绝对 vs 条件收敛）、'
    'buyback（1934 证券交易法 10b-18 安全港、1981 年前均为固定价格要约）、'
    'savings／demand／effective-demand（学术分歧条目化）。'
    '③再为 6 个补充：toxic-assets（2006 年 Mozilo 邮件首创该词、2009.3.23 盖特纳 **PPIP**、'
    '当日股指涨超 **6%**）、rent-seeking（1817 李嘉图地租→1967 塔洛克→1980s 批评、塔洛克悖论）、'
    'transaction-cost（1931 Commons→1996 Williamson 分歧）、tax-incidence（弹性决定归宿）、'
    'junk-bond（再打包成 CDO 提升优先级评级）、prisoners-dilemma（1950 提出→1984 Axelrod 锦标赛）。'
    '效果：timeline 事件 ' + str(tl) + ' 条、schools ' + str(sc) + ' 条、key_data ' + str(tk) + ' 条；'
    '仍缺 timeline/schools 的条目由 29 降至 ' + str(thin) + '。'
    '案例政策 ' + str(wp * 100 // len(cases)) + '%。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GG-GJ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 13, 'reviewed': 29, 'fixed': 0,
    'sources_total': srcn,
    'check_result': 'PASS (' + str(len(es)) + '); 八道检查全绿',
    'spot_check': '13个薄弱条目已补充；timeline ' + str(tl) + ' 条、schools ' + str(sc) + ' 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作GC-GF（核心全升L3，修复125页Markdown渲染缺陷）',
              '- 当前轮次：续作GG-GJ（13个薄弱条目补内容）')
entry = '''- **维基百科第 46 轮可用**。**为 13 个"内容薄弱"的概念条目补充实质内容**。
- **根因诊断**：29 个条目只有 5 个区块（概述／对照／待核实／来源／相关）。抓取它们的维基全文后发现**均有 5 千—7 万字符**——来源充足，问题在于 round 45 建条目时只取了 REST **摘要**（几百字符）。
- 补充内容举例：

  | 条目 | 新增 |
  |---|---|
  | **counterparty-risk** | 赫斯塔特银行 **1974.6.26** 牌照吊销（结算风险起源）；德崇 1990 未引发同类问题（英央行专设安排） |
  | **dividend** | VOC **1602—1800** 年付约 **18%** 股息；1902 年"不干预"原则判例 |
  | **toxic-assets** | 2006 年 Mozilo 邮件首创该词；**2009.3.23 盖特纳 PPIP**，当日股指涨超 **6%** |
  | **rent-seeking** | 1817 李嘉图地租 → **1967 塔洛克** → 1980s 批评；**塔洛克悖论** |
  | **transaction-cost** | 1931 Commons 提出 → 1996 Williamson 列出 TCE 与新古典的分歧 |
  | **prisoners-dilemma** | 1950 提出 → **1984 Axelrod 锦标赛** |
  | convergence／buyback／tax-incidence／junk-bond | Sachs-Warner 研究、10b-18 安全港、弹性决定归宿、CDO 再打包提升评级 |

- 效果：`timeline` 事件 **584 条**、`schools` **153 条**、`key_data` **409 条**；仍缺 timeline/schools 的条目由 **29 降至 16**。
- 现状：**625 条**、来源 732、站点 639 页；案例政策 71%、案例数据 85%。八道检查全绿。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GC-GF｜2026-11-24｜状态：625条；核心全升L3，修复125页Markdown渲染**',
              '**续作GG-GJ｜2026-11-24｜状态：625条；13个薄弱条目已补内容**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | timeline', tl, '| schools', sc, '| key_data', tk, '| 仍薄弱', thin)
