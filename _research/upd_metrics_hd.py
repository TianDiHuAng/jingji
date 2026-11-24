# -*- coding: utf-8 -*-
import json, glob, os

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
comp = sum(1 for e in es if e.get('comparison'))
pages = len(glob.glob('site/*.html'))

note = (
    '维基第56轮可用。HB-HD：**合并一处重复条目，并修复"孤儿页面累积"的系统缺陷**。'
    '①**发现重复条目**：`glass-steagall-1933`（U3 20世纪上半）与 `glass-steagall`（U6 理论与制度）'
    '讲的是**同一部 1933 年美国《银行法》**，仅归类不同。'
    '保留内容更完整的 `glass-steagall-1933`（key_data 1／timeline 3／schools 2／policy 1），'
    '并入后者的来源（w-en-bank-regulation）与 2 条学派观点，'
    '并把全站 6 个条目的 related 引用重定向，随后删除旧条目。'
    '条目总数 625 → **624**。'
    '②**发现系统缺陷**：`gen_site.py` 只写新页面、**不清理过时页面**——'
    '删除条目后 `site/glass-steagall.html` 仍残留，成为孤儿文件。'
    '已新增 `_cleanup_stale_pages()`：生成前扫描 site 目录，删除既不属条目、也不属特殊页的旧 .html。'
    '首次执行清理 1 个文件；站点页面数 639 → **638**（624 条目 + 14 特殊页）。'
    '③现状：条目 ' + str(len(es)) + '、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、'
    'key_data ' + str(tk) + ' 条、comparison ' + str(comp) + '/' + str(len(es)) + '、'
    '案例政策 ' + str(wp) + '/' + str(len(cases)) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HB-HD', 'date': '2026-11-24', 'new_entries': -1, 'upgraded': 1, 'reviewed': 625, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（624 条、638 页）',
    'spot_check': '合并 1 处重复条目；修复孤儿页面累积机制',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
# 更新顶部数字
s = s.replace('- **条目：625**（案例 205 / 概念 420）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(es) - len(cases)))
s = s.replace('- **站点页面：639**', '- **站点页面：%d**' % pages)
s = s.replace('- 内容覆盖：`comparison` **562/625（89%）**、`related` **625/625**',
              '- 内容覆盖：`comparison` **%d/%d（%d%%）**、`related` **%d/%d**'
              % (comp, len(es), comp * 100 // len(es), len(es), len(es)))
s = s.replace('- 案例内容：政策应对 **146/205（71%）**、关键数据 **176/205（85%）**',
              '- 案例内容：政策应对 **%d/%d（%d%%）**、关键数据 **%d/%d（%d%%）**'
              % (wp, len(cases), wp * 100 // len(cases),
                 sum(1 for e in cases if e.get('key_data')), len(cases),
                 sum(1 for e in cases if e.get('key_data')) * 100 // len(cases)))
add = '''- **维基百科第 56 轮可用（round 75）**。**合并一处重复条目，并修复"孤儿页面累积"的系统缺陷**。
- **① 发现重复条目**：`glass-steagall-1933`（U3 20世纪上半）与 `glass-steagall`（U6 理论与制度）讲的是**同一部 1933 年美国《银行法》**，仅归类不同。
  - 保留内容更完整的 `glass-steagall-1933`（key_data 1／timeline 3／schools 2／policy 1）
  - 并入后者的来源与 2 条学派观点（分业视角／混业视角）
  - 全站 **6 个条目的 related 引用重定向**，随后删除旧条目
  - 条目总数 625 → **624**
- **② 发现系统缺陷**：`gen_site.py` 只写新页面、**不清理过时页面**——删除条目后 `site/glass-steagall.html` 仍残留为孤儿文件。
  - 新增 `_cleanup_stale_pages()`：生成前扫描 site 目录，删除既不属条目、也不属特殊页的旧 `.html`
  - 首次执行清理 1 个文件；页面数 639 → **638**（624 条目 + 14 特殊页）
- 现状：**624 条**、来源 729、页面 **638**、key_data 416 条、comparison 562/624、案例政策 71%。十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HA｜2026-11-24｜状态：625条；新增 check_filler，共10道检查**',
              '**续作HB-HD｜2026-11-24｜状态：624条；合并重复条目，修复孤儿页面累积**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 页面', pages, '| comparison', comp)
