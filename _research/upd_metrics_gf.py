# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
wk = sum(1 for e in cases if e.get('key_data'))
l3 = [e for e in es if e.get('level') == 'L3']
l3full = sum(1 for e in l3 if all(e.get(x) for x in ('deep_svg', 'l3_detail', 'key_data', 'timeline', 'policy_response')))
core = [e for e in es if e.get('tier') == '核心']
tk = sum(len(e.get('key_data', [])) for e in es)

note = (
    '维基第45轮可用。GC-GF 三件事：'
    '①**核心 34 条全部升级 L3**——此前 growth/recession/utility/market-failure 四个基础概念'
    '标为 tier=核心 却只有 L2，违反"核心→L3"规则。已补齐 deep_svg 机制图、'
    'l3_detail（content＋data_caveat＋controversy_summary）、key_data'
    '（索洛"技术80%/资本20%"、2013年60%消费支出用于1869年不存在的商品、'
    '衰退判定三套门槛 1.5%／15%／75%／10%）、timeline 思想演化、policy_response。'
    '②发现 gen_site.py 只渲染 l3_detail 的 data_caveat 与 controversy_summary，'
    '新增的 content 字段未被渲染，已支持。'
    '③**本轮最重要的发现：全站 125 个页面的 Markdown 粗体 ** 从未渲染**——'
    'round 39 只修了单元导语，条目页的 overview／timeline／schools／policy_response／'
    'key_data／pending_notes 一直显示字面 **。'
    '新增 mdesc() 辅助函数（转义后把 **x** 转 <strong>）并替换全部长文本渲染点，'
    '修复后 **0 页面残留**；check_quality.py 加入第 11 项检查（未渲染 Markdown）。'
    '当前：L3 ' + str(len(l3)) + ' 条（五项全备 ' + str(l3full) + '）、核心 ' + str(len(core)) + ' 条全为 L3、'
    '案例政策 ' + str(wp * 100 // len(cases)) + '%、案例数据 ' + str(wk * 100 // len(cases)) + '%、key_data ' + str(tk) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GC-GF', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 639, 'fixed': 125,
    'sources_total': srcn,
    'check_result': 'PASS; 八道检查全绿（check_quality 新增Markdown渲染检查）',
    'spot_check': '核心34条全为L3；修复125页Markdown粗体未渲染',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作GA-GB（发现L3结构缺口，案例政策71%）',
              '- 当前轮次：续作GC-GF（核心全升L3，修复125页Markdown渲染缺陷）')
entry = '''- **维基百科第 45 轮可用**。三件事，第三件最重要。
- **① 核心 34 条全部升级 L3**：此前 `growth`／`recession`／`utility`／`market-failure` 四个基础概念标为 `tier=核心` 却只有 L2，违反"核心→L3"规则。已补齐：
  - `deep_svg` 机制图
  - `l3_detail`（content ＋ data_caveat ＋ controversy_summary）
  - `key_data`：索洛"**技术 80%／资本 20%**"、2013 年 **60%** 消费支出用于 1869 年不存在的商品、衰退判定三套门槛（1.5%／15%／75%／10%）
  - `timeline` 思想演化、`policy_response` 政策含义
- **② 修 gen_site.py**：此前只渲染 `l3_detail` 的 `data_caveat` 与 `controversy_summary`，新增的 `content` 字段未被渲染。
- **③ 本轮最重要的发现：全站 125 个页面的 Markdown 粗体 `**` 从未渲染**
  - round 39 只修了**单元导语**，条目页的 `overview`／`timeline`／`schools`／`policy_response`／`key_data`／`pending_notes` **一直显示字面 `**`**
  - 新增 `mdesc()` 辅助函数（转义后把 `**x**` 转 `<strong>`），替换**全部**长文本渲染点
  - 修复后 **0 页面残留**
  - `check_quality.py` 加入第 **11** 项检查（未渲染 Markdown）
- 当前：L3 **34 条**（五项全备 26）、**核心 34 条全为 L3**、案例政策 71%、案例数据 85%、`key_data` 403 条。八道检查全绿。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GA-GB｜2026-11-24｜状态：625条；发现L3结构缺口，案例政策71%**',
              '**续作GC-GF｜2026-11-24｜状态：625条；核心全升L3，修复125页Markdown渲染**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | L3', len(l3), '| 核心全L3 | key_data', tk)
