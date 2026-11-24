# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
used = set()
for e in es:
    used.update(e.get('sources', []))
    for k in e.get('key_data', []):
        used.update(k.get('sources', []))
    for p in e.get('policy_response', []):
        used.update(p.get('sources', []))
    for s in e.get('schools', []):
        if s.get('src'):
            used.add(s['src'])
src_ids = {s['id'] for s in srcs}
unused = sorted(src_ids - used)
zh = [s['id'] for s in srcs if s['id'].startswith('w-zh')]

note = (
    '维基第52轮可用。GS-GU：**补上 30 处"有源未引"，并发现第 5 次工具缺陷**。'
    '①第二批补 21 个条目：英文维基（panic-1796／panic-1910／greek-hyper-1941／bernie-madoff／sdr）；'
    '中文维基**跨语言对照源** 12 条（大萧条／通货膨胀／金本位／失业／货币政策／日本泡沫／'
    '互联网泡沫／恶性通胀／金融危机／景气循环／次贷危机／财政政策）；'
    '德/法/西语维基（`w-de-schwarzer-montag`→black-monday-1987、`w-fr-krach-1929`→wall-street-1929）。'
    '②第三批补 9 个条目：The Big Short→次贷危机、Das Kapital→马克思主义、NBER→商业周期、'
    'Fed+BIS→央行、ECB→欧洲央行、The Great Crash/Crash of 1929→wall-street-1929 等。'
    '③删除 3 个确实无用的来源。'
    '④**误删 `owid-dataset` 导致 12 处 R4 错误**——根因：统计"来源是否被引用"时只扫 '
    '`entries[].sources`，**漏了 `key_data[].sources`**（owid-dataset 正被 12 处 key_data 引用）。'
    '已恢复并修正统计口径（含 sources／key_data／policy_response／schools 四类字段）。'
    '⑤补齐 `owid-dataset` 缺失的 title 等字段与 13 个机构源的 year 字段。'
    '⑥第 5 次工具缺陷记入 BLOCKERS。'
    '现状：来源库 **' + str(len(srcs)) + '** 条，其中 **' + str(len(src_ids & used)) + '** 被引用、**'
    + str(len(unused)) + '** 未引用（9 本书 + 7 个机构，留作参考资源）。'
    '中文维基来源 ' + str(len(zh)) + ' 条现已全部被引用，构成跨语言对照。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GS-GU', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 30, 'reviewed': 54, 'fixed': 31,
    'sources_total': len(srcs),
    'check_result': 'PASS; 九道检查全绿',
    'spot_check': '30 处"有源未引"已补；未引用来源 54→16；第5次工具缺陷已记录',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 52 轮可用（round 71）**。**补上 30 处"有源未引"，并发现第 5 次工具缺陷**。
- 第二批补 21 个条目：

  | 类型 | 来源 → 条目 |
  |---|---|
  | 英文维基 | panic-1796／panic-1910／greek-hyper-1941／bernie-madoff／sdr |
  | **中文维基（跨语言对照）** | 大萧条／通货膨胀／金本位／失业／货币政策／日本泡沫／互联网泡沫／恶性通胀／金融危机／景气循环／次贷危机／财政政策 |
  | 德/法/西语维基 | `w-de-schwarzer-montag`→black-monday-1987；`w-fr-krach-1929`→wall-street-1929 |

- 第三批补 9 个条目：The Big Short→次贷危机、Das Kapital→马克思主义、NBER→商业周期、Fed+BIS→央行、ECB→欧洲央行等。
- **误删 `owid-dataset` 导致 12 处 R4 错误**——根因：统计"来源是否被引用"时只扫 `entries[].sources`，**漏了 `key_data[].sources`**。已恢复并修正口径（含 sources／key_data／policy_response／schools 四类字段）。
- 补齐 `owid-dataset` 缺失的 title 等字段与 13 个机构源的 year 字段。
- **第 5 次工具缺陷**记入 `BLOCKERS.md`。
- 现状：来源库 **729** 条，**713 被引用、16 未引用**（9 本书 + 7 个机构，留作参考资源）。中文维基来源现已**全部被引用**，构成跨语言对照。
- 九道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GR｜2026-11-24｜状态：625条；修复11处"有源未引"，第4次工具缺陷已记录**',
              '**续作GS-GU｜2026-11-24｜状态：625条；30处"有源未引"已补，未引用来源54→16**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 未引用', len(unused), '| 中文维基', len(zh))
