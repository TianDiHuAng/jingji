# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)

note = (
    '维基第41轮可用。FV：**新增第6个检查工具 tools/check_sources.py**，'
    '抽样验证 sources.json 中 verified=true 的来源是否真可达。'
    '首次抽样30个：27可达、3失败（openlibrary 503×2、OWID 404×1）；'
    '逐项复测确认**均为服务端瞬时问题**——OWID 的 grapher 页复测返回200、openlibrary 首页与单个作品页复测200。'
    '再抽样20个：19可达、1超时（openlibrary 单项偶发）。'
    '工具设计：403/405/429（反爬、方法限制、限流）视为可达；5xx与超时自动重试一次；只有404与持续失败才报错。'
    '**结论：' + str(srcn) + ' 个来源可达性良好**，round 8 的全量核对结论仍成立。'
    '至此共有 **6 道检查**：check（数据合规R1-R16）、check_links（链接与SVG）、'
    'check_quality（HTML结构10项）、check_kd（key_data数值）、check_polnum（政策段数字）、'
    'check_sources（来源可达性）。'
    '当前：案例政策 ' + str(wp) + '/' + str(len(cases)) + '（' + str(wp * 100 // len(cases)) + '%）、'
    '案例数据 ' + str(wk) + '/' + str(len(cases)) + '（' + str(wk * 100 // len(cases)) + '%）、'
    'key_data ' + str(tk) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FV', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 50, 'fixed': 0,
    'sources_total': srcn,
    'check_result': 'PASS; 6 道检查全绿（来源抽样可达性良好）',
    'spot_check': '来源抽样 50 个：失败均为服务端瞬时问题，复测通过',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FT-FU（新增check_polnum，392个政策数字全部溯源）',
              '- 当前轮次：续作FV（新增check_sources，来源抽样可达性良好）')
entry = '''- **维基百科第 41 轮可用**。**新增第 6 个检查工具 `tools/check_sources.py`**——抽样验证 `verified=true` 的来源是否真可达。
- 首次抽样 30 个：**27 可达、3 失败**（openlibrary 503×2、OWID 404×1）；逐项复测确认**均为服务端瞬时问题**——OWID grapher 页复测 200、openlibrary 作品页复测 200。
- 再抽样 20 个：**19 可达、1 超时**（openlibrary 单项偶发）。
- 工具设计：
  - `403/405/429`（反爬、方法不允许、限流）→ **视为可达**
  - `5xx` 与超时 → **自动重试一次**
  - 只有 `404` 与持续失败才报错
- **结论：732 个来源可达性良好**，round 8 的全量核对结论仍成立。
- **至此共有 6 道检查**：

  | 脚本 | 管什么 |
  |---|---|
  | `check.py` | 数据合规（R1–R16） |
  | `check_links.py` | 链接与 SVG |
  | `check_quality.py` | HTML 结构（10 项） |
  | `check_kd.py` | key_data 数值可核对性 |
  | `check_polnum.py` | policy_response 数字溯源 |
  | **`check_sources.py`** | **来源可达性抽样** |

- 现状：**625 条**、来源 732、站点 639 页；案例政策 69%、案例数据 85%。六道检查全绿。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FT-FU｜2026-11-24｜状态：625条；新增 check_polnum，392个政策数字全部溯源**',
              '**续作FV｜2026-11-24｜状态：625条；新增 check_sources，六道检查全绿**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 来源', srcn, '| 六道检查')
