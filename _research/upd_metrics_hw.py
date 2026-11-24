# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
single = [e['id'] for e in es if len(e.get('sources', [])) == 1]

note = (
    '维基第63轮可用。HV-HW：**把 round 81 确立的"独立性"标准应用到现有数据上，'
    '结果是验证页的核心分类被大幅修正**。'
    '①逐条审查原"独立机构双源印证（15 条）"，发现只有 **2 条**真正独立：'
    '`black-monday-1987`（维基 vs 美联储历史站，22.6%）与 `wall-street-1929`（美联储 89% vs 维基 90%）。'
    '其余 **13 条**用的是 OWID／世界银行数据——而这些机构的数字**本身汇总自各国官方统计**，'
    '维基所载数字往往源自**同一批官方统计**，两者属"不同加工口径"（国际可比调整 vs 原始公布），'
    '**不构成严格独立的信息生产链**。'
    '②据此把验证页分类拆为：**独立机构双源印证（2 条）** 与 **不同统计口径对照（15 条）**，'
    '新增板块并写明"本板块单列，不与独立机构印证合并计数"。'
    '③修改过程中遇到两个技术坑：gen_site.py 是 **CRLF 行尾**（`\\n` 匹配失败）→ 改用行号插入；'
    '注释中含同名字样导致"板块已存在"误判 → 改为匹配 `vb.append` 行。'
    '④页面现有五个板块：独立机构印证 2／统计口径对照 15／跨语言对照 41／两源差异并列 12／官方来源 11。'
    '这是一次**数字变小但诚实度上升**的修正——把"看起来有 15 条双源印证"还原为'
    '"2 条真独立 + 15 条口径对照"。'
    '现状：' + str(len(es)) + ' 条、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HV-HW', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 15, 'reviewed': 15, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（验证页分类修正）',
    'spot_check': '独立机构印证 15→2 条；新增统计口径对照 15 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 63 轮可用（round 82）**。**把"独立性"标准应用到现有数据上，验证页核心分类被大幅修正**。
- **① 逐条审查原"独立机构双源印证（15 条）"**——只有 **2 条**真正独立：

  | 条目 | 印证关系 |
  |---|---|
  | `black-monday-1987` | 维基 **vs** 美联储历史站（22.6%） |
  | `wall-street-1929` | 美联储 **vs** 维基（89% / 90%） |

  其余 **13 条**用的是 OWID／世界银行数据——这些机构**本身汇总自各国官方统计**，而维基数字往往源自**同一批官方统计**，两者属"不同加工口径"，**不构成严格独立的信息生产链**。

- **② 验证页分类拆分**：

  | 板块 | 条数 |
  |---|---|
  | 独立机构双源印证 | **2**（原 15） |
  | **不同统计口径对照（新增）** | **15** |
  | 跨语言维基对照 | 41 |
  | 两源存在差异·已并列 | 12 |

  新板块明确写"本板块单列，不与独立机构印证合并计数"。

- **③ 两个技术坑**：`gen_site.py` 是 **CRLF 行尾**（`\\n` 匹配失败）→ 改用行号插入；注释含同名字样导致"板块已存在"误判 → 改为匹配 `vb.append` 行。
- 这是一次**数字变小但诚实度上升**的修正：把"看起来有 15 条双源印证"还原为"**2 条真独立 + 15 条口径对照**"。
- 十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HR-HU｜2026-11-24｜状态：632条；再补10个跨语言来源，并自我修正NBER≠第二来源**',
              '**续作HV-HW｜2026-11-24｜状态：632条；独立印证15→2条，新增统计口径对照15条**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
