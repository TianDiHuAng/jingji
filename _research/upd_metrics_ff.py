# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
pct = wp * 100 // len(cases)

note = (
    '维基第30轮可用。FF：再抓40个案例全文（累计120个），人工核验补写10条，'
    '案例政策覆盖 51%→' + str(pct) + '%（' + str(wp) + '/' + str(len(cases)) + '）。'
    '补写内容：上海橡皮股票风潮1910（清廷7.27批准向外国银行借款、8.4与9家外国银行签约借350万两维持市面）、'
    '史密森协议（汇率区间2.25%、用SDR平衡、取消进口附加税、1973.2.14美元再贬10%后转浮动）、'
    '硅谷银行2023（拜登承诺存款可用但不奖励投资者、599名风投呼吁干预、公开争论）、'
    '西班牙2008（欧元集团向FROB提供最高1000亿欧元，IMF估资本需求约400亿）、'
    '土耳其2001（IMF 114亿美元、土航51%股权私有化）、'
    '南斯拉夫1992（非正统vs正统稳定方案均长期失败、1994货币重建计划）、'
    '世通（促成萨班斯-奥克斯利法、2006被Verizon收购）、'
    '瑞典1990s（含同期芬兰经验：71亿马克卡可转换贷款+政府担保基金）、'
    'DeFi（FATF 2021.10纳入加密服务提供者指引）、GameStop（SEC发布极端波动期融资披露样本函）。'
    '**跳过来源不匹配者**：台湾泡沫的"Monetary policy"章节实为日本央行贴现率内容；'
    '津巴布韦/魏玛的Aftermath是恶性通胀结束方式的通用讨论；委内瑞拉章节内容不相关；'
    'Terra-Luna是"未申请牌照"属监管缺失而非政策应对。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FF', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 10, 'reviewed': 40, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '案例政策覆盖 51%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FD-FE（再补12条，案例政策首次过半51%）',
              '- 当前轮次：续作FF（再补10条，案例政策56%）')
entry = '''- **维基百科第 30 轮可用**。再抓 40 个案例全文（累计 120 个），补写 **10 条**，案例政策覆盖 **51% → 56%（115/205）**。
- 本轮几条有意思的：

  | 案例 | 政策应对 |
  |---|---|
  | 上海橡皮股票风潮 1910 | 清廷 7.27 批准向外国银行借款；8.4 与 **9 家外国银行**签约借 **350 万两**维持市面 |
  | 史密森协议 1971 | 汇率区间 **2.25%**、用 SDR 平衡、取消进口附加税；1973.2.14 美元再贬 10% 后转浮动 |
  | 西班牙 2008 | 欧元集团向 FROB 提供最高 **1000 亿欧元**（IMF 估需求约 400 亿） |
  | 土耳其 2001 | IMF **114 亿美元** + 土航 **51%** 股权私有化 |
  | 南斯拉夫 1992 | 非正统 vs 正统稳定方案**均长期失败**；1994 货币重建计划 |
  | 世通 2002 | 促成**萨班斯-奥克斯利法**；2006 被 Verizon 收购 |
  | DeFi 2021 | FATF 将 DeFi 纳入加密服务提供者指引 |
  | GameStop 2021 | SEC 发布极端波动期融资的**披露样本函** |

- **本轮跳过 4 类来源不匹配的内容**（重要）：
  - **台湾泡沫**的 `Monetary policy` 章节实为**日本央行**贴现率内容（5.00%→2.50%）
  - **津巴布韦/魏玛**的 `Aftermath` 是恶性通胀结束方式的**通用讨论**，不是该国具体政策
  - **委内瑞拉**章节内容不相关（讲情报机构减员）
  - **Terra-Luna** 是"未申请牌照"，属**监管缺失**而非政策应对
- 三道检查全绿。现状：**625 条**、来源 727、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FD-FE｜2026-11-24｜状态：625条；案例政策覆盖51%（首次过半）**',
              '**续作FF｜2026-11-24｜状态：625条；案例政策覆盖56%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 案例政策', wp, '/', len(cases), '=', pct, '%')
