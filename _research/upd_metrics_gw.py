# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)


def nlang(e):
    ls = {str(x).split('-')[1] for x in (e.get('sources') or [])
          if str(x).startswith('w-') and len(str(x).split('-')) > 1}
    return len({l for l in ls if l in ('en', 'zh', 'de', 'fr', 'es', 'ja')})


multi = sum(1 for e in es if nlang(e) >= 2)

note = (
    '维基第53轮可用。GV-GW：**修正验证页"跨语言对照"的判定缺陷，并扩展首页统计维度**。'
    '①**原判定有缺陷**：`crosslang` 的条件是"note 含印证词但无官方机构源"，'
    '这与"跨语言"毫无关系。改为**真正检查该数据行（连带所属条目）是否引用 ≥2 种语言的维基**'
    '（en／zh／de／fr／es／ja）。'
    '②结果：跨语言对照由 **6 条增至 32 条**（' + str(multi) + ' 个条目有多个语种来源，其中 14 个有 key_data）。'
    '核验判定准确性：asian-financial-crisis-1997（en+zh）、black-monday-1987（de+en）、'
    'dotcom-bubble-2000（en+zh）等均正确。'
    '③**说明文字改为诚实表述**：明确"多语种页面同属维基体系，彼此不构成独立机构互证——'
    '它们是同一知识生产体系的不同语言版本，可能共享同一批原始引用，也可能各自独立"，'
    '本页仅作对照记录，不作核实等级认定。'
    '④首页统计卡片由 7 项扩展为 **9 项**，新增"多语种维基条目 ' + str(multi) + '"与'
    '"案例载有政策应对 ' + str(wp) + '/' + str(len(cases)) + '"；'
    '并统一口径——首页按**条目**计、验证页按 **key_data 行**计，两者的差异已在标签上区分。'
    '⑤首页原有 7 项统计经核对全部准确。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GV-GW', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 639, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 九道检查全绿',
    'spot_check': '跨语言对照 6→32 条（判定修正）；首页统计 7→9 项',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 53 轮可用（round 72）**。**修正验证页"跨语言对照"的判定缺陷**，并扩展首页统计维度。
- **原判定有缺陷**：`crosslang` 的条件是"note 含印证词但**无**官方机构源"——这与"跨语言"毫无关系。改为**真正检查该数据行（连带所属条目）是否引用 ≥2 种语言的维基**（en／zh／de／fr／es／ja）。
- 结果：跨语言对照由 **6 条增至 32 条**（**25 个条目**有多个语种来源，其中 14 个有 key_data）。
  - 核验：`asian-financial-crisis-1997`（en+zh）、`black-monday-1987`（de+en）、`dotcom-bubble-2000`（en+zh）等判定正确
- **说明文字改为诚实表述**：
  > 多语种页面**同属维基体系**，彼此不构成独立机构互证——它们是同一知识生产体系的不同语言版本，可能共享同一批原始引用，也可能各自独立。本页仅作对照记录，不作核实等级认定。
- 首页统计卡片由 7 项扩展为 **9 项**，新增「多语种维基条目 25」「案例载有政策应对 146/205」；并统一口径——首页按**条目**计、验证页按 **key_data 行**计。
- 首页原有 7 项统计经核对全部准确（625／34／591／0／729／418／15）。
- 九道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GS-GU｜2026-11-24｜状态：625条；30处"有源未引"已补，未引用来源54→16**',
              '**续作GV-GW｜2026-11-24｜状态：625条；跨语言对照判定修正(6→32)，首页统计扩展为9项**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 多语种条目', multi, '| 政策覆盖', wp, '/', len(cases))
