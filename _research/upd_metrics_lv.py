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
short = [e for e in es if e.get('tier') in ('核心', '重要') and len(e.get('overview') or '') < 150]
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))

note = (
    "维基第105轮可用。LP-LV：**扩写 16 条案例（WARNINGS 32 → 16），全部基于来源全文撰写**。"
    "①**方法的改变（重要）**：此前扩写概念可凭机制知识；"
    "本轮起处理案例，**必须先读 `_research/wiki_full/<id>.txt`**，"
    "只写来源中确实存在的事实，"
    "数字必须能在来源中找到（用 check_body_num 检验）。"
    "②第一批 6 条：turkey-2001／bond-crisis-1994／edict-maximum-prices／"
    "norwegian-banking-1988／tripartite-1936／gold-bloc。"
    "③第二批 5 条：nixon-shock／emergency-banking-act-1933／gold-reserve-act-1934／"
    "argentina-2018／dawes-plan-1924。"
    "④第三批 5 条：aig／enron／drexel／worldcom／barings-1995。"
    "⑤**几处从来源读到的关键事实**："
    "**AIG** 从美联储获 **1800 亿美元**救助，FCIC 把失败归因于"
    "「**大规模销售未对冲的保险**」，到 2012 年已偿还 **2050 亿美元**；"
    "**安然**股价从 2000 年 8 月的 **90.75 美元/股**跌至 2001 年 11 月底的**不足 1 美元**，"
    "**634 亿美元资产**使其成为当时最大企业破产；"
    "**世通**虚增资产超 **110 亿美元**，内部审计发现 **38 亿美元**虚假分录，"
    "并记录了**举报者被训斥、被裁员**的细节；"
    "**巴林银行**因 Nick Leeson 期货欺诈损失 **8.27 亿英镑**，"
    "是「单人操作 + 内控失效」导致百年银行覆灭的极端案例；"
    "**德崇证券**1986 财年净利 **5.455 亿美元**为当时华尔街纪录，"
    "米尔肯薪酬 **2.95 亿美元**，1990 年破产是自大萧条来首家。"
    "⑥数字核验：check_body_num 显示新写案例的数字均可在来源中找到"
    "（`gold-bloc` 的「10 月／12 月」为原文事实）。"
    "⑦现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（全部为案例，均有来源全文）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LP-LV', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 16, 'reviewed': 32, 'fixed': 16,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 16（案例）+ 自测 18/18',
    'spot_check': '扩写 16 条案例，全部先读来源全文；数字经 check_body_num 核验',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 105 轮可用（round 125）**。**扩写 16 条案例（WARNINGS 32 → 16），全部基于来源全文撰写**。
- **方法的改变（重要）**：此前扩写概念可凭机制知识；本轮起处理案例，**必须先读 `_research/wiki_full/<id>.txt`**，只写来源中确实存在的事实，数字必须能在来源中找到（用 `check_body_num` 检验）。
- **第一批 6 条**：turkey-2001／bond-crisis-1994／edict-maximum-prices／norwegian-banking-1988／tripartite-1936／gold-bloc。
- **第二批 5 条**：nixon-shock／emergency-banking-act-1933／gold-reserve-act-1934／argentina-2018／dawes-plan-1924。
- **第三批 5 条**：aig／enron／drexel／worldcom／barings-1995。
- **几处从来源读到的关键事实**：

  | 案例 | 来源中的关键事实 |
  |---|---|
  | `aig` | 从美联储获 **1800 亿美元**救助；FCIC 归因于「**大规模销售未对冲的保险**」；到 2012 年已偿还 **2050 亿美元** |
  | `enron` | 股价从 **90.75 美元/股**（2000.8）跌至**不足 1 美元**（2001.11）；**634 亿美元资产**为当时最大企业破产 |
  | `worldcom` | 虚增资产超 **110 亿美元**；内部审计发现 **38 亿美元**虚假分录；**举报者被训斥、被裁员** |
  | `barings-1995` | Nick Leeson 期货欺诈损失 **8.27 亿英镑**；「单人操作 + 内控失效」导致百年银行覆灭 |
  | `drexel` | 1986 财年净利 **5.455 亿美元**（当时华尔街纪录）；米尔肯薪酬 **2.95 亿美元**；1990 年破产为自大萧条来首家 |

- 数字核验：`check_body_num` 显示新写案例的数字均可在来源中找到（如 `gold-bloc` 的「10 月／12 月」为原文事实）。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 900 字**；**ERRORS 0**、WARNINGS **16（全部为案例，均有来源全文）**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LN-LO｜2026-11-24｜状态：641条；扩写27条概念，概念类全部完成（R22 59→32）**',
              '**续作LP-LV｜2026-11-24｜状态：641条；扩写16条案例，全部基于来源全文（R22 32→16）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22', len(short), '| avg', avg)
