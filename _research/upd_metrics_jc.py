# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
from kdclass import counts
c = counts(es)

note = (
    '维基第81轮可用（**round 100 里程碑**）。**验证验证方法本身——发现 check_kd 存在假匹配**。'
    '①按 round 99 的原则"验证覆盖率之前先验证验证方法"，本轮抽查 check_kd 判定"匹配成功"的数据：'
    '随机取 6 条，**3 条是假匹配**——'
    '"3元券储备支撑 = 5" 命中原文 "50 cents" 的 "5"；'
    '"金融部门占比 = 3" 命中 "$3 billion" 的 "3"；'
    '"人口降幅 = -62" 命中 "249 to 262" 的 "62"。'
    '②**根因**：原判据只检查"数字字符串是否出现在全文中"，不与单位或上下文绑定，'
    '因此任何包含该数字的片段都会被判为匹配。'
    '③**改进尝试与二次发现**：改用"数字+单位/关键词"的严格判据后，'
    '强匹配降到 319，但查看未通过项发现**大量假阴性**——'
    '原文用**英文数字**（eight-day、twelve Key Attributes）、**文字表述**（more than half）、'
    '或**不同单位**（400 million livres vs 0.4 百万里弗）。'
    '④**结论：任何纯字符串匹配都无法同时避免假阳性与假阴性**。'
    '故改为**两级报告**：★强匹配（数字+单位/关键词/英文数字）**328 条（78%）**、'
    '○弱匹配（仅数字出现，需人工判断）**40 条（10%）**、×未匹配 **51 条**。'
    '工具明确声明"**只把强匹配作为可核对依据，弱匹配不视为通过**"，'
    '不再宣称"392/419 条全部可核对"。'
    '⑤这是**第 7 次工具缺陷**，也是影响最大的一次——'
    '它此前一直让我以为 400+ 条数据"已核对"。教训：'
    '**"数字出现"与"数据可核对"之间隔着上下文**。'
    '⑥现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JA-JC', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 419, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（check_kd 改为两级判据）',
    'spot_check': '发现 check_kd 假匹配（3/6）；改为两级报告：强匹配 328/419',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 81 轮可用（round 100 里程碑）**。**验证验证方法本身——发现 `check_kd` 存在假匹配**。
- 按 round 99 的原则"验证覆盖率之前先验证验证方法"，抽查 `check_kd` 判定"匹配成功"的数据：**随机取 6 条，3 条是假匹配**：

  | 数据项 | 值 | 误匹配到 |
  |---|---|---|
  | 3元券储备支撑 | 5 | "**5**0 cents" 的 5 |
  | 金融部门占比 | 3 | "**$3** billion" 的 3 |
  | 亚历山大城人口降幅 | −62 | "249 to **262**" 的 62 |

- **根因**：原判据只检查"数字字符串是否出现"，不与单位或上下文绑定。
- **改进尝试与二次发现**：改用"数字+单位/关键词"严格判据后，强匹配降到 319，但未通过项里**大量是假阴性**——原文用**英文数字**（eight-day、twelve Key Attributes）、**文字表述**（more than half）、或**不同单位**（400 million livres vs 0.4 百万里弗）。
- **结论：任何纯字符串匹配都无法同时避免假阳性与假阴性**。故改为**两级报告**：

  | 级别 | 条数 | 占比 |
  |---|---|---|
  | ★ **强匹配**（数字+单位/关键词/英文数字） | **328** | **78%** |
  | ○ 弱匹配（仅数字出现，需人工判断） | 40 | 10% |
  | × 未匹配 | 51 | — |

  工具明确声明"**只把强匹配作为可核对依据，弱匹配不视为通过**"。
- **这是第 7 次工具缺陷，也是影响最大的一次**——它此前一直让我以为 400+ 条数据"已核对"。教训：**"数字出现"与"数据可核对"之间隔着上下文**。
- 十一道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IY-IZ｜2026-11-24｜状态：641条；修复72处无效来源引用，R4扩展到嵌套字段**',
              '**续作JA-JC｜2026-11-24｜状态：641条；发现check_kd假匹配，改为两级判据（强匹配328/419）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
