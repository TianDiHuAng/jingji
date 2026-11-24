# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)
from kdclass import counts
c = counts(es)

note = (
    '维基第73轮可用。IN-IO：**再建 2 条（secured-lending／taper-tantrum），并对来源性质做了分级标注**。'
    '①换名重试三个缺口：`taper-tantrum` 的多种名称均无专属页（"2013 bond market selloff" 为空）、'
    '`sacrifice-ratio` 无专属页、`regulatory-arbitrage` 仍重定向到 Arbitrage——三项确无专属维基页。'
    '②**新建 `secured-lending`（担保贷款）**——有专属页（10,780 字符）。'
    '内容含：担保安排的双向目的（债权人降风险／借款人得优惠条件）；'
    '**无追索权贷款**（抵押物为唯一求偿对象，止赎后不得追讨差额）与有追索权的区别；'
    '担保债权的三种产生方式（合同／法定留置权／判决留置权）与 PMSI／NPMSI 之分；'
    '以及 2007 年英国担保贷款市场随危机萎缩的时间线。'
    '③**新建 `taper-tantrum`（2013 年缩减恐慌）**——无可用的专属页，'
    '实质记述在「Quantitative easing」页面。'
    '**处理方式：建条目，但明确标注来源性质为"通用页中的相关章节，非专属页"**'
    '（写入 source 的 note、key_data 的 note 与 pending_notes 三处），以便读者判断可信度等级。'
    '核心事实：2012.12.12 开放式购债增至 **850 亿美元/月**；'
    '**2013.6.19 伯南克**宣布有条件缩减——若数据向好，9 月可降至 **650 亿美元/月**，'
    '并暗示 2014 年中期结束；他强调**未宣布加息**。'
    '条目点明关键：**政策尚未改变、长期利率已上行**，说明前瞻指引本身即政策工具。'
    '市场反应的具体幅度（10 年期收益率升幅、新兴市场货币贬值幅度）未录入，已在 pending_notes 注明待补。'
    '④现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、timeline ' + str(tl) + '、key_data ' + str(tk) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IN-IO', 'date': '2026-11-24', 'new_entries': 2, 'upgraded': 2, 'reviewed': 4, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（641 条、655 页）',
    'spot_check': '新建 secured-lending／taper-tantrum；来源性质分级标注',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：639**（案例 208 / 概念 431）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：740**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：653**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 73 轮可用（round 92）**。**再建 2 条，并对来源性质做分级标注**。
- **换名重试三个缺口**：`taper-tantrum` 多种名称均无专属页（"2013 bond market selloff" 为空）、`sacrifice-ratio` 无专属页、`regulatory-arbitrage` 仍重定向到 Arbitrage——**三项确无专属维基页**。
- **① `secured-lending`（担保贷款）**——有专属页（10,780 字符）：

  | 内容 | 要点 |
  |---|---|
  | 双向目的 | 债权人降风险（可取得抵押物）／借款人得优惠条件 |
  | **无追索权贷款** | 抵押物为**唯一**求偿对象，止赎后**不得追讨差额** |
  | 产生方式 | 合同协议／法定留置权／判决留置权；PMSI 与 NPMSI 之分 |
  | 危机中的顺周期 | 抵押物跌价→抵押不足→追加担保或止赎→抛售→价格再跌 |

- **② `taper-tantrum`（2013 年缩减恐慌）**——**无可用的专属页**，实质记述在「Quantitative easing」页面。
  - **处理方式：建条目，但明确标注来源性质为"通用页中的相关章节，非专属页"**（写入 source note、key_data note、pending_notes 三处）
  - 核心事实：2012.12.12 开放式购债增至 **850 亿美元/月**；**2013.6.19 伯南克**宣布有条件缩减——若数据向好，9 月可降至 **650 亿美元/月**，暗示 2014 年中期结束；他强调**未宣布加息**
  - 条目点明：**政策尚未改变、长期利率已上行** → 前瞻指引本身即政策工具
  - 市场反应的具体幅度未录入，已注明待补
- 现状：**641 条**（案例 208／概念 433）、来源 **741**、页面 **655**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IM｜2026-11-24｜状态：639条；新建1933银行假日与两条风险管理概念**',
              '**续作IN-IO｜2026-11-24｜状态：641条；新建担保贷款与缩减恐慌，来源性质分级标注**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 页面', pages)
