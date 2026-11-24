# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
tl = sum(len(e.get('timeline', [])) for e in es)

from kdclass import counts
c = counts(es)

note = (
    '维基第69轮可用。IE-II：**突破"仅依赖维基"的来源边界，并根治"两处代码算同一指标"的结构问题**。'
    '①**来源边界突破**：测试发现 **IMF／BIS／FSB** 的官方页面均可访问，'
    '其中 **IMF Glossary**（9,535 字符）含监督、全球失衡、储备、SDR 的一手定义。'
    '这打破了 round 86/87 遇到的"无专属维基页面即无法建条目"的限制。'
    '②**首次使用国际机构一手文献**：注册 `org-imf-glossary` 并补 `sdr` 条目——'
    '篮子由**人民币／欧元／日元／英镑／美元**五种货币构成；最近一次审查 **2015 年 11 月**完成、'
    '新权重 **2016 年 10 月 1 日**生效；SDR 利率为篮子市场短期利率的**每周加权平均**、下限 **0.050%**。'
    '并新增 key_data 2 条、timeline 2 条。'
    '③**判据细化**：原判据简单按前缀（fed-* 独立、owid-*/org-* 统计汇总），'
    '但 `org-imf-glossary`／`org-bis`／`org-fsb` 是**机构独立撰写的文献**，不应归入"统计汇总"。'
    '已建立两份白名单分别标注。'
    '④**发现并修复回归 bug**：细化判据时把 `org-nber` 加入独立文献白名单，'
    '导致两条衰退条目（其 note 早已写明"**NBER 为原始出处、维基为转引，不构成独立双源**"）'
    '被重新算进"独立印证"（2→4 条）。已从白名单移除，并在判据中加入**否定词排除**'
    '（note 含"不构成独立/原始出处/系转引"者一律不计入印证类）。'
    '⑤**结构性根治**：把核实等级判据抽为共享模块 **`tools/kdclass.py`**，'
    '由 `gen_site.py` 与 `check_pages.py` **import 同一函数**——'
    '这才是 round 83 教训（两处代码算同一指标必然矛盾）的彻底解法。'
    '当前：独立机构印证 **' + str(c['confirmed']) + '** 条、统计口径对照 **' + str(c['statview']) + '** 条、'
    '差异并列 **' + str(c['discrepant']) + '** 条，三处（首页/验证页/检查脚本）完全一致。'
    '⑥现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、timeline ' + str(tl) + '、key_data ' + str(tk) + '。'
    '**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IE-II', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 635, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（判据统一为共享模块）',
    'spot_check': '首次用 IMF 一手文献补 sdr；修复 NBER 回归；抽取 kdclass 共享判据',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **来源：733**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
add = '''- **维基百科第 69 轮可用（round 88）**。**突破"仅依赖维基"的来源边界，并根治"两处代码算同一指标"的结构问题**。
- **① 来源边界突破**：测试发现 **IMF／BIS／FSB** 官方页面均可访问，其中 **IMF Glossary**（9,535 字符）含监督、全球失衡、储备、**SDR** 的一手定义。这打破了 round 86/87 遇到的"无专属维基页面即无法建条目"的限制。
- **② 首次使用国际机构一手文献**：注册 `org-imf-glossary` 并补 `sdr`：

  | 项 | 内容 |
  |---|---|
  | 篮子构成 | **人民币／欧元／日元／英镑／美元**（5 种） |
  | 最近审查 | **2015 年 11 月**完成，新权重 **2016 年 10 月 1 日**生效 |
  | SDR 利率 | 篮子市场短期利率的**每周加权平均**，下限 **0.050%** |

- **③ 判据细化**：原判据按前缀划分，但 `org-imf-glossary`／`org-bis`／`org-fsb` 是**机构独立撰写的文献**，不应归入"统计汇总"。已建立两份白名单。
- **④ 发现并修复回归 bug**：细化判据时把 `org-nber` 加入独立文献白名单，导致两条衰退条目（note 早已写明"**NBER 为原始出处、维基为转引，不构成独立双源**"）被重新算进"独立印证"（2→4）。已移除，并在判据中加入**否定词排除**（含"不构成独立/原始出处/系转引"者不计入）。
- **⑤ 结构性根治**：把判据抽为共享模块 **`tools/kdclass.py`**，由 `gen_site.py` 与 `check_pages.py` **import 同一函数**——这是 round 83 教训的彻底解法。
- 当前：独立印证 **2** 条、统计口径对照 **13** 条、差异并列 **12** 条，三处完全一致。
- 现状：**635 条**、来源 **734**、页面 **649**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IC-ID｜2026-11-24｜状态：635条；危机理论核查，original-sin补充并纠"定义充数据"**',
              '**续作IE-II｜2026-11-24｜状态：635条；首次用IMF一手文献，抽取共享判据模块**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 印证 %d | 口径 %d' % (c['confirmed'], c['statview']))
