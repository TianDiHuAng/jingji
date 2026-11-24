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
    '维基第89轮可用。JR-JT：**系统找出"被误标为补充的核心概念"，深化 2 条**。'
    '①**系统扫描**：U6 概念中 tier=补充 且 overview<200 字者共 **15 条**。'
    '其中 10 条是机构条目（AIIB／AfDB／IDB／ADB／EBRD／IAIS／英格兰银行／瑞典央行／'
    '安达信／房地美），简短本属合理；但 **5 条是理论/机制概念**——'
    '**`moral-hazard`（道德风险，102 字）**、**`animal-spirits`（动物精神，128 字）**、'
    '`debt-trap-diplomacy`（102 字）、`global-debt`（94 字）、`subordination`（183 字）。'
    '②**深化 `moral-hazard`（102 → 677 字）**：据专属页 26,026 字符——'
    '补**词源澄清**（17 世纪起源、19 世纪末被英国保险业广泛使用；但 18 世纪数学家把 '
    '"moral" 用作"**主观的**"，与伦理无关）；'
    '补**1998 年 LTCM 经典案例**（纽约联储主席 McDonough 的安排被沃尔克批评为加重道德风险；'
    'Tyler Cowen 概括为"债权人相信只要崩溃会威胁全球信贷体系、美联储就会偿付他们的贷款"）；'
    '补**2008 年三条渠道**（已录第一条：报酬按利润百分比计提的资产管理人）。'
    '③**深化 `animal-spirits`（128 → 569 字）**：据专属页 7,590 字符——'
    '补**凯恩斯原文**（"积极活动依赖**自发的乐观**而非数学期望……只能归因于动物精神——'
    '一种要行动而非不行动的自发冲动"）；'
    '补**1905 年心理学来源**（凯恩斯研读过的心理学家已用该词）；'
    '补 **2009 年 Akerlof 与 Shiller** 的政府角色论述（"政府如同育儿手册中的父母，'
    '要**搭好舞台**，并抵消动物精神导致的过度"）。'
    '④**两个新规则在真实写作中首次被触发**：'
    '（a）**R4b** 抓出 `w-en-animal-spirits` 未在 sources.json 注册——'
    '这是 round 103 修好 R4b（原只检查 1 个条目）后的**首次实战捕获**；'
    '（b）round 107 的 **R19** 也已两次拦下忘填 sources 的 timeline。'
    '⑤现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '（+1）、页面 ' + str(pages) + '；'
    'timeline ' + str(tl) + '、key_data ' + str(tk) + '；单薄概念条目由 5 降至 3'
    '（余 debt-trap-diplomacy／global-debt／subordination）。'
    '**十一道检查全绿 + 自测 18/18**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JR-JT', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 15, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + 自测 18/18',
    'spot_check': '深化 moral-hazard 与 animal-spirits；R4b 首次实战捕获',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **来源：741**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
add = '''- **维基百科第 89 轮可用（round 108）**。**系统找出“被误标为补充的核心概念”，深化 2 条**。
- **系统扫描**：U6 概念中 `tier=补充` 且 `overview<200` 字者共 **15 条**。其中 **10 条是机构条目**（AIIB／AfDB／IDB／ADB／EBRD／IAIS／英格兰银行／瑞典央行／安达信／房地美），简短本属合理；但 **5 条是理论/机制概念**：

  | 条目 | 字数 |
  |---|---|
  | **`moral-hazard`（道德风险）** | **102** |
  | **`animal-spirits`（动物精神）** | **128** |
  | `debt-trap-diplomacy` | 102 |
  | `global-debt` | 94 |
  | `subordination` | 183 |

- **深化 `moral-hazard`（102 → 677 字）**，据专属页 26,026 字符：
  - **词源澄清**：17 世纪起源、19 世纪末被英国保险业广泛使用；但 18 世纪数学家把 "moral" 用作“**主观的**”，**与伦理无关**
  - **1998 年 LTCM 经典案例**：纽约联储主席 McDonough 的安排被**沃尔克**批评为加重道德风险；Tyler Cowen 概括为“债权人相信只要崩溃会威胁全球信贷体系、美联储就会偿付他们的贷款”
  - **2008 年三条渠道**（已录第一条：报酬按利润百分比计提的资产管理人）
- **深化 `animal-spirits`（128 → 569 字）**，据专属页 7,590 字符：
  - **凯恩斯原文**：“积极活动依赖**自发的乐观**而非数学期望……只能归因于动物精神——一种**要行动而非不行动的自发冲动**”
  - **1905 年心理学来源**：凯恩斯研读过的心理学家已用该词
  - **2009 年 Akerlof 与 Shiller**：“政府如同育儿手册中的父母，要**搭好舞台**，并抵消动物精神导致的过度”
- **两个新规则在真实写作中首次被触发**：
  - **R4b** 抓出 `w-en-animal-spirits` 未在 `sources.json` 注册——这是 round 103 修好 R4b（原只检查 1 个条目）后的**首次实战捕获**
  - round 107 的 **R19** 也已两次拦下忘填 sources 的 timeline
- 来源 **741 → 742**；单薄概念条目由 **5 降至 3**（余 `debt-trap-diplomacy`／`global-debt`／`subordination`）。十一道检查全绿 + 自测 18/18。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JP-JQ｜2026-11-24｜状态：641条；深化TBTF与三元悖论，R19首次实战拦截**',
              '**续作JR-JT｜2026-11-24｜状态：641条；深化道德风险与动物精神，R4b首次实战捕获**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 来源', len(srcs))
