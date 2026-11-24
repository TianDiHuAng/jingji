# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts
c = counts(es)

note = (
    '维基第82轮可用。JD：**用同一方法验证 check_polnum，发现同类假匹配并修复一个实现 bug**。'
    '①抽查 check_polnum 判定通过的样本：随机 6 条中**约 4 条错位**——'
    '"8月1日"命中原文 "7 August 2018" 的 8、"12月29日"命中 "1941年12月" 的 12、'
    '"6%"命中 "6.9%" 的 6。与 round 100 发现的 check_kd 缺陷**同源**。'
    '②改造为两级判据时**发现一个实现 bug**：初版只在"数字第一次出现的位置"判断上下文，'
    '导致大量**真匹配被误判为弱**（如"1825 年危机"的 1825 首次出现在别处）。'
    '修复为**遍历该数字的所有出现位置，任一位置满足上下文即判强**。'
    '③修复后结果：**强匹配 413/558（74%）**、弱匹配 145（26%）、完全找不到 0。'
    '④抽查剩余 145 个弱匹配，发现多为**中文单位与英文原文表述差异**'
    '（如"1999—2000 年"的"年"在数字后更远处、中文"万元"对应原文 "thousand yuan"）——'
    '这再次印证 round 100 的结论：**纯字符串匹配无法同时消除假阳性与假阴性**。'
    '⑤工具输出已改为"未发现「完全找不到」的数字；但**弱匹配不视为通过**，仍需人工抽查"。'
    '⑥**两周连续发现两个核心检查工具存在系统性假阳性**，说明此前的"检查全绿"里，'
    '至少 check_kd 与 check_polnum 两项的"通过"仅代表"数字能在某处找到"，'
    '不代表"数字与来源对应"。已在工具内声明该局限。'
    '⑦现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JD', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 558, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; check_polnum 改为两级判据（强匹配 413/558）',
    'spot_check': '发现 check_polnum 同类假匹配；修复"只看首个匹配位置"的实现 bug',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 82 轮可用（round 101）**。**用同一方法验证 `check_polnum`，发现同类假匹配并修复一个实现 bug**。
- 抽查判定通过的样本：随机 6 条中**约 4 条错位**——「8月1日」命中原文 "7 August **2018**" 的 8、「12月29日」命中 "1941 年 12 月" 的 12、「6%」命中 "**6**.9%" 的 6。与 round 100 的 `check_kd` 缺陷**同源**。
- 改造为两级判据时**发现一个实现 bug**：初版只在“数字**第一次出现**的位置”判断上下文，导致大量**真匹配被误判为弱**（如「1825 年危机」的 1825 首次出现在别处）。修复为**遍历所有出现位置，任一满足上下文即判强**。
- 修复后：

  | 级别 | 条数 | 占比 |
  |---|---|---|
  | ★ **强匹配** | **413** | **74%** |
  | ○ 弱匹配（需人工判断） | 145 | 26% |
  | × 完全找不到 | 0 | — |

- 抽查剩余 145 个弱匹配，多为**中文单位与英文原文表述差异**（「1999—2000 年」的“年”在数字后更远处、中文“万元”对应原文 "thousand yuan"）——再次印证：**纯字符串匹配无法同时消除假阳性与假阴性**。
- **连续两轮发现两个核心检查工具存在系统性假阳性**：此前的“检查全绿”里，`check_kd` 与 `check_polnum` 的“通过”仅代表“数字能在某处找到”，**不代表“数字与来源对应”**。已在工具内声明该局限。
- 十一道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JA-JC｜2026-11-24｜状态：641条；发现check_kd假匹配，改为两级判据（强匹配328/419）**',
              '**续作JD｜2026-11-24｜状态：641条；check_polnum同类缺陷，改两级（强匹配413/558）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
