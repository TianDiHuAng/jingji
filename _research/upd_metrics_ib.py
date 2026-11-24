# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)
sc = sum(len(e.get('schools', [])) for e in es)

note = (
    '维基第67轮可用。IB：**审计概念维度的类别覆盖，发现监管类偏少，新建 2 条**。'
    '①按语义分组统计 426 个概念：宏观 49／货币 60／金融 54／国际 14／理论 20／危机 14／'
    '**监管仅 7**——监管是危机分析的核心维度，明显偏少。'
    '②逐项核查 26 个关键监管概念，已覆盖 14 项（basel-accords／basel-iii／macroprudential／'
    'stress-test／capital-requirement／deposit-insurance／lender-of-last-resort／too-big-to-fail／'
    'moral-hazard／volcker-rule／dodd-frank／shadow-banking／capital-control／bank-regulation），'
    '**缺 12 项**。'
    '③测试剩余概念的维基页面可用性：`countercyclical-capital-buffer` 无页面；'
    '`ring-fencing` 重定向到「指定用途税」（**完全不相干**）；`regulatory-arbitrage` 重定向到 Arbitrage（通用页）；'
    '`leverage-ratio` 重定向到「杠杆(金融)」（非监管指标页）——均不宜作专属来源，记入缺口。'
    '④**新建 2 条**：'
    '**资本充足率**（Basel I 1988 的 8% 最低要求／Basel II 内部评级／Basel III 提高核心一级资本；'
    '两派观点：缓冲视角 vs 成本与规避视角；关键局限是风险权重可被模型调低）；'
    '**流动性覆盖率 LCR**（Basel III 要求 HQLA 覆盖压力情景 **30 天**净流出；'
    '引入理由正是"一些资本充足的银行因流动性管理不善陷入困境"；与 NSFR、准备金要求的区别）。'
    '⑤两处技术细节：`ring-fencing` 与 `leverage-ratio` 的**重定向陷阱**再次出现（抓到的页面不相干或非专属），'
    '按标准不作来源。'
    '现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、timeline ' + str(tl) + '、'
    'schools ' + str(sc) + '、key_data ' + str(tk) + '。**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IB', 'date': '2026-11-24', 'new_entries': 2, 'upgraded': 2, 'reviewed': 26, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（635 条、649 页）',
    'spot_check': '概念类别审计：监管类 7→9 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：633**（案例 207 / 概念 426）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：731**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：647**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 67 轮可用（round 86）**。**审计概念维度的类别覆盖，发现监管类偏少，新建 2 条**。
- **类别分布审计**（426 个概念）：宏观 49／货币 60／金融 54／国际 14／理论 20／危机 14／**监管仅 7**。
- **逐项核查 26 个关键监管概念**：已覆盖 14 项，**缺 12 项**。测试剩余概念的维基页面后发现：

  | 概念 | 测试结果 |
  |---|---|
  | `countercyclical-capital-buffer` | 无页面 |
  | `ring-fencing` | 重定向到「指定用途税」——**完全不相干** |
  | `regulatory-arbitrage` | 重定向到 Arbitrage（通用页） |
  | `leverage-ratio` | 重定向到「杠杆(金融)」（非监管指标页） |

  均不宜作专属来源，记入缺口。

- **新建 2 条**：

  | 条目 | 关键内容 |
  |---|---|
  | **资本充足率** | Basel I（1988）的 **8%** 最低要求／Basel II 内部评级／Basel III 提高核心一级资本；**缓冲视角 vs 成本与规避视角**；根本局限是**风险权重可被模型调低** |
  | **流动性覆盖率(LCR)** | Basel III 要求 HQLA 覆盖压力情景 **30 天**净流出；引入理由正是"**一些资本充足的银行因流动性管理不善陷入困境**"；与 NSFR、准备金要求的区别 |

- **重定向陷阱再次出现**（`ring-fencing`／`leverage-ratio`），按既定标准不作来源。
- 现状：**635 条**（案例 207／概念 428）、来源 **733**、页面 **649**、监管类 **7→9**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IA｜2026-11-24｜状态：633条；四项覆盖审计通过，新建领先指标**',
              '**续作IB｜2026-11-24｜状态：635条；概念类别审计，新建资本充足率与LCR**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 页面', pages)
