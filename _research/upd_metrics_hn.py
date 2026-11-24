# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
comp = sum(1 for e in es if e.get('comparison'))
pages = len(glob.glob('site/*.html'))

note = (
    '维基第60轮可用。HM-HN：**校验并重写两份诊断文档，新建 2 个衰退条目**。'
    '①**核查 READER_QUESTIONS.md（round 17）所列缺口**——3 个全部已解决：'
    'FTX（`bankruptcy-ftx`）、动物精神（`animal-spirits`）、铁路狂热（`railway-mania`）；'
    '附录候选中的 1920—21 衰退（`recession-1920-1921`）与 2020 崩盘（`covid-crash-2020`）亦已建。'
    '②**核查 GAP_REPORT.md（round 22）**——其列的两个"真实缺口"（闪崩、2020 崩盘）均已关闭。'
    '③按核查结果**新建 2 条**：`recession-1960-1961`（10 个月、GDP −1.4%、'
    '衰退结束后失业率仍升三个月至 1961.5 见顶）与 `recession-1969-1970`'
    '（11 个月、GDP −0.6%、与越战赤字收紧及加息同时、通胀已在上行）。'
    '`panic-1785` 因维基仅重定向到「美国衰退列表」（通用页），不作专属来源，记入真实缺口表。'
    '④**重写两份文档**：把"已解决"逐项标注，并在开头写明"待办清单本身也需要定期校验——'
    'round 77 曾因依据过时清单而建了已存在的条目"。'
    '⑤两条新条目的 key_data label 加了年份区分（避免与既有条目的同名指标混淆）。'
    '现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、key_data ' + str(tk) + '、'
    'comparison ' + str(comp) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HM-HN', 'date': '2026-11-24', 'new_entries': 2, 'upgraded': 2, 'reviewed': 8, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（632 条、708 来源、646 页）',
    'spot_check': '重写 2 份诊断文档；新建 2 个衰退条目',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：630**（案例 205 / 概念 425）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：706**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：644**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 60 轮可用（round 79）**。**校验并重写两份诊断文档，新建 2 个衰退条目**。
- **① 核查 `READER_QUESTIONS.md`（round 17）所列缺口**——3 个**全部已解决**：

  | 原缺口 | 现状 |
  |---|---|
  | 加密货币崩盘（FTX） | ✅ `bankruptcy-ftx` |
  | 动物精神 | ✅ `animal-spirits` |
  | 铁路狂热 | ✅ `railway-mania` |

  附录候选中的 `1920—21 衰退`（`recession-1920-1921`）与 `2020 崩盘`（`covid-crash-2020`）亦已建。

- **② 核查 `GAP_REPORT.md`（round 22）**——其列的两个"真实缺口"（闪崩、2020 崩盘）均已关闭。
- **③ 新建 2 条**：

  | 条目 | 数据 |
  |---|---|
  | **1960—61 衰退** | **10 个月**、GDP **−1.4%**；衰退 1961.2 结束后**失业率仍升三个月**至 1961.5 见顶；随后是美国史上第三长扩张 |
  | **1969—70 衰退** | **11 个月**、GDP **−0.6%**；与**越战赤字收紧＋加息**同时；衰退前通胀已在上行 |

- `panic-1785` 因维基仅重定向到「美国衰退列表」（通用页），不作专属来源，记入真实缺口表。
- **④ 重写两份文档**，逐项标注"已解决"，并写明"待办清单本身也需要定期校验——round 77 曾因依据过时清单而建了已存在的条目"。
- 现状：**632 条**（案例 205／概念 427）、来源 **708**、页面 **646**。十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HJ-HL｜2026-11-24｜状态：630条；新建4概念，重写BACKLOG待建清单**',
              '**续作HM-HN｜2026-11-24｜状态：632条；重写2份诊断文档，新建2个衰退条目**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 来源', len(srcs), '| 页面', pages)
