# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
from kdclass import counts
c = counts(es)
reln = [len(e.get('related', [])) for e in es]

note = (
    '维基第75轮可用。IR：**修复第二种"接线"缺失——正文"见 xxx"式引用未接入 related**。'
    '①上一轮修复了 comparison 中提到的条目未入 related；'
    '本轮用正则 `见 xxx` 扫描 overview／comparison／one_line／timeline，'
    '又发现 **20 处**正文明确写"见某条目"却未在 related 中收录——读者同样无法跳转。'
    '②**修复**：把这 20 处引用补入 related，并按约定做同类对称化（10 条）。'
    '复核：**仍缺接线的"见 xxx"引用归零**。'
    '③**扩展检查规则**：`check_pages.py` 的「文案与导航一致性」检查现同时覆盖'
    '（a）comparison 中提到的 id 与（b）正文"见 xxx"式引用，两者都必须在 related 中。'
    '④这是同一根因的两种表现：**文案里写下的交叉引用，未必都变成了可点击的链接**。'
    '两类合计修复 **96 处**（comparison 76 + 见xxx 20），并都已纳入自动检查。'
    '⑤现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、'
    'key_data ' + str(tk) + '；related 平均 %.1f 条；' % (sum(reln) / len(reln)) +
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IR', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 20, 'reviewed': 641, 'fixed': 30,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（检查规则已扩展到正文引用）',
    'spot_check': '20 处"见 xxx"补入 related；两类接线缺失合计修复 96 处',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 75 轮可用（round 94）**。**修复第二种"接线"缺失——正文"见 xxx"式引用未接入 `related`**。
- 上一轮修的是 comparison 中提到的条目未入 `related`；本轮用正则 `见 xxx` 扫描 overview／comparison／one_line／timeline，**又发现 20 处**正文明确写"见某条目"却未收录——读者同样无法跳转。

  | 例 | 正文引用 |
  |---|---|
  | `fixed-exchange-rate` | 见 `black-wednesday-1992`／`mexican-peso-1994`／`asian-financial-crisis-1997` |
  | `lemons-market` | 见 `subprime-lending`／`bank-run` |
  | `kipper-wipper-1618` | 见 `debasement` |

- **修复**：20 处引用补入 `related`，并做同类对称化（10 条）。复核：**归零**。
- **扩展检查规则**：`check_pages.py` 的「文案与导航一致性」现同时覆盖（a）comparison 提到的 id 与（b）正文"见 xxx"式引用。
- **两类合计修复 96 处**（comparison 76 + 见xxx 20），均已纳入自动检查。
- 现状：**641 条**、来源 **741**、页面 **655**；`related` 平均 **%.1f 条**。**十一道检查全绿**。
''' % (sum(reln) / len(reln))
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IP-IQ｜2026-11-24｜状态：641条；修复文案与导航不一致并固化为检查**',
              '**续作IR｜2026-11-24｜状态：641条；修复"见xxx"引用未接线，两类接线缺失共96处**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | related 平均 %.1f' % (sum(reln) / len(reln)))
