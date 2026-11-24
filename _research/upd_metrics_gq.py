# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
ids = {e['id'] for e in es}
oneway = [(a, r) for a, e in ((x['id'], x) for x in es) for r in e.get('related', [])
          if r in ids and a not in next(y for y in es if y['id'] == r).get('related', [])]
both = sum(1 for e in es for r in e.get('related', [])
           if r in ids and e['id'] in next(y for y in es if y['id'] == r).get('related', [])) // 2
avg = sum(len(e.get('related', [])) for e in es) / len(es)

note = (
    '维基第50轮可用。GQ：**对称化同类关联，双向关联对由 529 增至 1,615**。'
    '①检查发现 **1,343 条单向关联**（概念→概念 838／案例→案例 248／案例→概念 198／概念→案例 59）。'
    '②判断：两个概念互相关联、两个案例互为参照时，读者从任一侧都应能跳转；'
    '跨类关联（案例→概念）保持单向——案例可指向多个概念，概念不必回指所有案例。'
    '③补入 **1,086 条**反向关联，双向对 529 → **1,615**，剩余 257 条单向全部为跨类（有意保留）。'
    '④`related` 平均 ' + ('%.1f' % avg) + ' 条，最多 26 条（monetary-policy），页面显示正常。'
    '当前：' + str(len(es)) + ' 条、来源 ' + str(srcn) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '、key_data ' + str(tk) + ' 条。九道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GQ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 625, 'reviewed': 1343, 'fixed': 1086,
    'sources_total': srcn,
    'check_result': 'PASS; 九道检查全绿',
    'spot_check': '双向关联对 529→1615，剩余单向均为跨类（有意保留）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 50 轮可用（round 69）**。**对称化同类关联，双向关联对由 529 增至 1,615**。
- 检查发现 **1,343 条单向关联**：

  | 类型 | 数量 | 处理 |
  |---|---|---|
  | 概念→概念 | 838 | **对称化** |
  | 案例→案例 | 248 | **对称化** |
  | 案例→概念 | 198 | 保持单向 |
  | 概念→案例 | 59 | 保持单向 |

- **判断依据**：两个概念互相关联、两个案例互为参照时，读者从任一侧都应能跳转；但案例可指向多个概念，概念不必回指所有案例——**跨类单向是合理的结构，不是缺陷**。
- 补入 **1,086 条**反向关联，双向对 529 → **1,615**，剩余 257 条单向全部为跨类（有意保留）。
- `related` 平均 **5.6 条**，最多 26 条（`monetary-policy`），页面显示正常。
- 九道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GN-GP｜2026-11-24｜状态：625条；13个薄弱条目已补，缺timeline/schools降至4**',
              '**续作GQ｜2026-11-24｜状态：625条；双向关联对529→1615**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 双向对', both, '| 单向', len(oneway), '| 平均', round(avg, 1))
