# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
tk = sum(len(e.get('key_data', [])) for e in es)
tl = sum(len(e.get('timeline', [])) for e in es)
from kdclass import counts
c = counts(es)
thin = [e for e in es if e['unit'].startswith('U6') and e['tier'] == '补充' and len(e['overview']) < 200]

note = (
    '维基第90轮可用。JU-JV：**深化两条理论概念，其中一条逐条并列两派证据**。'
    '①**`debt-trap-diplomacy`（债务陷阱外交，102 → 721 字）**，据专属页 51,436 字符：'
    '补**词源**——该词由**印度学者 Brahma Chellaney 于 2017 年**首创；'
    '补**背景**——2008 后美欧长期低利率使资金追逐新兴市场收益，叠加 **2013 年**"一带一路"启动；'
    '补**两派证据并列**：'
    '（a）**2018 年 3 月**全球发展中心(CGD)报告称 **2001—2017 年中国对 51 个债务国重组或豁免偿付、'
    '未扣押国家资产**；（b）W. Gyude Moore（前利比里亚公共工程部长）**2018 年 9 月**批评'
    '该话语"**根源是对中国崛起的焦虑，而非非洲的现实**"。'
    '条目明确写"**本库不对此下结论**"，并把两派写入 `schools` 并列呈现——'
    '符合项目"争议立场并列、不代读者结论"的规则。'
    '②**`global-debt`（全球债务，94 → 515 字）**，据专属页 8,940 字符：'
    '补**三种口径的区分**（公共债务/GDP、私人债务/GDP、对**外国债权人**的外债），强调三者不可混用；'
    '补**"债务多于货币"**这一常被忽略的事实——总债务/货币供应量在日、瑞为 1.7，丹麦、冰岛达 **4.7**，'
    '**世界总计 1.8**；债务/GDP 从拉脱维亚 1.5 到卢森堡 5.0，**世界总计 3.5（据 IIF）**；'
    '新增 key_data 3 条，均标注"统计年份待核实"。'
    '③**检查随数据增长而跟进**：key_data 可核对数由 419 增至 **428**，'
    '强匹配 333（78%）——新增数据未拉低强匹配比例。'
    '④现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    'timeline ' + str(tl) + '、key_data ' + str(tk) + '；单薄概念条目由 3 降至 1（余 `subordination`）。'
    '**十一道检查全绿 + 自测 18/18**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JU-JV', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 2, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + 自测 18/18',
    'spot_check': '深化 debt-trap-diplomacy（两派并列）与 global-debt（三口径）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 90 轮可用（round 109）**。**深化两条理论概念，其中一条逐条并列两派证据**。
- **`debt-trap-diplomacy`（债务陷阱外交，102 → 721 字）**，据专属页 51,436 字符：
  - **词源**：由**印度学者 Brahma Chellaney 于 2017 年**首创
  - **背景**：2008 后美欧长期低利率使资金追逐新兴市场收益，叠加 **2013 年**“一带一路”启动
  - **两派证据并列**：

    | 立场 | 证据 |
    |---|---|
    | 质疑方 | **2018 年 3 月** CGD 报告称 **2001—2017 年中国对 51 个债务国重组或豁免偿付、未扣押国家资产** |
    | 质疑方 | W. Gyude Moore（前利比里亚公共工程部长）**2018 年 9 月**批评该话语“**根源是对中国崛起的焦虑，而非非洲的现实**” |
    | 支持方 | 强调贷款条款不透明、资金回流本国承包商、部分项目位于战略要地 |

  - 条目明确写“**本库不对此下结论**”，两派写入 `schools` 并列呈现——符合项目“争议立场并列、不代读者结论”的规则
- **`global-debt`（全球债务，94 → 515 字）**，据专属页 8,940 字符：
  - 补**三种口径的区分**（公共债务/GDP、私人债务/GDP、对**外国债权人**的外债），强调三者不可混用
  - 补**“债务多于货币”**——总债务/货币供应量：日、瑞 **1.7**，丹麦、冰岛 **4.7**，**世界总计 1.8**；债务/GDP：拉脱维亚 1.5 → 卢森堡 5.0，**世界总计 3.5（据 IIF）**
  - 新增 key_data 3 条，均标注“统计年份待核实”
- **检查随数据增长而跟进**：key_data 可核对数 419 → **428**，强匹配 **333（78%）**——新增数据未拉低强匹配比例。
- 单薄概念条目由 **3 降至 1**（余 `subordination`）。十一道检查全绿 + 自测 18/18。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JR-JT｜2026-11-24｜状态：641条；深化道德风险与动物精神，R4b首次实战捕获**',
              '**续作JU-JV｜2026-11-24｜状态：641条；深化债务陷阱外交（两派并列）与全球债务**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
