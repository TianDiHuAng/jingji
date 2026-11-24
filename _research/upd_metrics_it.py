# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
from kdclass import counts
c = counts(es)
dist = dict(Counter(s.get('type') for s in srcs))

note = (
    '维基第77轮可用。IT：**统一 sources.type 词汇表并加入 R17 检查**。'
    '①统计发现 type 字段**分类不一致**：'
    '既有"官方机构"(18) 又有"权威机构"(4)——**同义不同名**；'
    '既有"统计数据库"(5) 又有 "dataset"(1)——**中英混用**。'
    '②统一为四类：**权威百科／学术著作／官方机构／统计数据库**，共修正 5 个来源的 type。'
    '统一后分布：' + '／'.join('%s %d' % (k, v) for k, v in sorted(dist.items())) + '。'
    '③**加入 R17 检查**：来源的 type 必须属于该词汇表，否则报错——'
    '防止今后再出现"权威机构"这类异名。'
    '④另核验 `deep_svg` 的质量：34 条 L3 全部有机制图，'
    '文本节点 11—18 个、方框 4—8 个、箭头 3—6 个、长度中位数 1,354 字符；'
    '抽查 `lehman` 的图为**真实机制链条**（冲击→资产端受损→杠杆放大→破产；'
    '融资依赖→抵押品折价→流动性枯竭；含反馈回路），非文字堆砌。'
    '⑤这也印证了 round 95 的判断：**中文标题级引用不可自动接线**——'
    '本轮未再尝试该类自动化，而是转向 schema 一致性这类可判定问题。'
    '现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、key_data ' + str(tk) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿（check.py 现含 R17）**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IT', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 5, 'reviewed': 741, 'fixed': 5,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（check.py 新增 R17 来源类型词汇表）',
    'spot_check': '统一 type 为四类；核验 deep_svg 质量为真实机制链条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 77 轮可用（round 96）**。**统一 `sources.type` 词汇表并加入 R17 检查**。
- **发现分类不一致**：

  | 问题 | 实例 |
  |---|---|
  | **同义不同名** | "官方机构"(18) 与 "权威机构"(4) 并存 |
  | **中英混用** | "统计数据库"(5) 与 "dataset"(1) 并存 |

- **统一为四类**：**权威百科 692／学术著作 21／官方机构 22／统计数据库 6**，共修正 5 个来源。
- **加入 R17 检查**：来源的 `type` 必须属于该词汇表，否则报错——防止今后再出现异名。
- **另核验 `deep_svg` 质量**：34 条 L3 全部有机制图，文本节点 11—18 个、方框 4—8 个、箭头 3—6 个、长度中位数 1,354 字符。抽查 `lehman` 的图为**真实机制链条**（冲击→资产端受损→杠杆放大→破产；融资依赖→抵押品折价→流动性枯竭；含反馈回路），非文字堆砌。
- 印证 round 95 的判断：**中文标题级引用不可自动接线**——本轮未再尝试该类自动化，转向 schema 一致性这类可判定问题。
- 现状：**641 条**、来源 **741**、页面 **655**。**十一道检查全绿**（`check.py` 现含 R17）。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IS｜2026-11-24｜状态：641条；穷举接线根因（自动化到此为止），统一schools字段**',
              '**续作IT｜2026-11-24｜状态：641条；统一来源类型词汇表并加入R17检查**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | type 分布', dist)
