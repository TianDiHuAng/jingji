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
    '维基第58轮可用。HG-HI：**新建 2 个概念条目，并发现/合并 2 组重复**。'
    '①先测 12 个 BACKLOG 待建概念的维基页面：9 个可抓全文，3 个重定向到通用页'
    '（`regulatory-arbitrage`→Arbitrage、`taper-tantrum`→QE、`sacrifice-ratio`／`term-premium`／`disclosure` 无页面）。'
    '②新建 **`pigouvian-tax`（庇古税）** 与 **`common-pool`（公共池资源）**，'
    '各含 overview／timeline（庇古1920·科斯1960／哈丁1968·奥斯特罗姆1990）／'
    '两派观点／对比辨析／关联条目，来源为各自专属维基页（34k／17k 字符）。'
    '③**发现 2 组重复**：已存在 `externality`（非 `externalities`）与 `value-at-risk`（非 `var`）——'
    'BACKLOG 清单（round 37 编制）已过时，未核对现状。已把新内容（timeline／更完整 overview／来源）'
    '并入已有条目后删除重复文件，并重定向相关引用。**这是"未先检索自己的库"的又一次复发。**'
    '④新建条目时 `schools` 直接赋值为元组导致渲染报错，已修正为 dict 格式（与 round 64 同类错误）。'
    '⑤来源库 704→**702**（合并 `w-en-var`→`w-en-value-at-risk`、`w-en-externalities`→`w-en-externality`）。'
    '现状：**626 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、key_data ' + str(tk) + '、'
    'comparison ' + str(comp) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HG-HI', 'date': '2026-11-24', 'new_entries': 2, 'upgraded': 2, 'reviewed': 12, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（626 条、702 来源、640 页）',
    'spot_check': '新建 2 概念；合并 2 组重复条目；来源 704→702',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：624**（案例 205 / 概念 419）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **条目：624**（案例 205 / 概念 420）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：700**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：638**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 58 轮可用（round 77）**。**新建 2 个概念条目，并发现/合并 2 组重复**。
- 先测 12 个 BACKLOG 待建概念的维基页面：**9 个可抓全文**，3 个重定向到通用页（`regulatory-arbitrage`→Arbitrage、`taper-tantrum`→QE、`sacrifice-ratio`／`term-premium`／`disclosure` 无页面）。
- **新建 2 条**：

  | 条目 | 内容 |
  |---|---|
  | **庇古税** | 税=边际外部成本以内部化；实践难题是成本难计量→多用代理税基；**双重红利假说**的成立条件有争议 |
  | **公共池资源** | 难排他但具竞争性；哈丁"公地悲剧"（1968）vs **奥斯特罗姆自主治理**（1990）；与公共品的区别在竞争性 |

- **发现 2 组重复**：站内已有 `externality`（非 `externalities`）、`value-at-risk`（非 `var`）——**BACKLOG 清单（round 37 编制）已过时**。已把新内容并入已有条目后删除重复，并重定向引用。**这是"未先检索自己的库"的又一次复发。**
- 新建时 `schools` 直接赋值为元组导致渲染报错，已修正为 dict（与 round 64 同类错误）。
- 来源库 704 → **702**（合并 `w-en-var`、`w-en-externalities`）。
- 现状：**626 条**（案例 205／概念 421）、来源 **702**、页面 **640**。十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HE-HF｜2026-11-24｜状态：624条；合并29组重复来源，来源库729→700**',
              '**续作HG-HI｜2026-11-24｜状态：626条；新建庇古税与公共池资源，合并2组重复**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 来源', len(srcs), '| 页面', pages)
