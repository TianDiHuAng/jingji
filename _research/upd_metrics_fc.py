# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
pct = wp * 100 // len(cases)

note = (
    '维基第28轮可用。策略转向：补齐案例政策的来源天花板已破除，改用维基**全文**而非摘要。'
    '①抓取40个案例全文（平均1.5万字符，最大7万）；'
    '②提取方法两次迭代：先按章节标题匹配（Policy response/Rescue/Aftermath等），仅找到18个有政策类章节；'
    '再改为"含政策主体句"提取（FDIC/Fed/ECB/IMF/government/central bank等），覆盖升至38/40——'
    '但**噪声极大**（如"安哥拉政府优先修复基础设施"、"巴林银行曾为1812年战争融资美国政府"被误判），'
    '正是round 25的教训重现；'
    '③最终**放弃自动提取，改为人工核验**：逐个阅读政策章节原文后补写8条，'
    '包括阿姆斯特丹1763(央行提供流动性)、智利1982(救助+两家国有化+1983年大规模干预)、'
    '中国2015(国家队1.6万亿入市+限卖空+6个月禁减持)、中国房地产2020(预售资金政府监管+房贷利率下限取消+开发商破产表态)、'
    '巴西2014(95号宪法修正案20年支出上限+2017劳动改革)、巴林1995(ING以1英镑收购并承担全部负债)、'
    '第一共和2023(11家银行存款300亿美元+FDIC接管竞拍)、富兰克林1974(美联储借超10亿美元仍宣告无偿付能力)。'
    '案例政策覆盖 41%→' + str(pct) + '%（' + str(wp) + '/' + str(len(cases)) + '）。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EY-FC', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 8, 'reviewed': 40, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '案例政策覆盖 41%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EW-EX（第二批补建15个基础概念）',
              '- 当前轮次：续作EY-FC（维基全文补案例政策应对，覆盖45%）')
entry = '''- **维基百科第 28 轮可用**。策略转向：`policy_response` 的来源天花板（round 30 记录）**已破除**——改用维基**全文**而非摘要。
- 步骤：抓取 40 个案例全文（平均 1.5 万字符，最大 7 万）→ 两种提取方法对比 → 人工核验后补写。
- **提取方法的两次迭代（重要）**：
  1. 按**章节标题**匹配（Policy response / Rescue / Aftermath 等）→ 仅 18 个案例有政策类章节
  2. 改为**含政策主体句**提取（FDIC / Fed / ECB / IMF / government / central bank 等）→ 覆盖升至 38/40，但**噪声极大**："安哥拉政府优先修复基础设施"、"巴林银行曾为 1812 年战争融资美国政府"都被误判为政策应对
  - **这正是 round 25 的教训重现**。最终放弃自动提取，**改为人工核验**。
- 人工核验后补写 **8 条**：

  | 案例 | 政策应对 |
  |---|---|
  | 阿姆斯特丹 1763 | 阿姆斯特丹银行（央行）提供额外流动性 |
  | 智利 1982 | 救助多家银行 + 两家**国有化** + 1983.1.13 大规模干预（救助5家、解散3家） |
  | 中国 2015 | "国家队"投入 **1.6万亿元**入市 + 限制卖空 + 6个月禁减持 |
  | 中国房地产 2020 | 预售资金纳入政府监管账户 + 取消首套房贷利率下限 + 开发商应破产表态 |
  | 巴西 2014 | 95号宪法修正案（**20年支出上限**）+ 2017劳动改革 |
  | 巴林 1995 | ING 以**1英镑**收购并承担全部负债（市场化处置） |
  | 第一共和 2023 | 11家银行联合存入 **300亿美元** + FDIC 接管、摩根大通竞拍收购 |
  | 富兰克林 1974 | 美联储借出**超10亿美元**，仍于1974.10.8宣告无偿付能力 |

- 案例政策覆盖 **41% → 45%（93/205）**。三道检查全绿。
- 现状：**625 条**（案例 205 / 概念 420）、来源 727、站点 639 页；comparison 与 related 双 100%。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EW-EX｜2026-11-24｜状态：625条（+15 基础概念）**',
              '**续作EY-FC｜2026-11-24｜状态：625条；案例政策覆盖45%（维基全文）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 案例政策', wp, '/', len(cases), '=', pct, '%')
