# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
tk = sum(len(e.get('key_data', [])) for e in es)
tl = sum(len(e.get('timeline', [])) for e in es)
from kdclass import counts
c = counts(es)
# 单薄条目统计
sup = [e for e in es if e['tier'] == '补充']
thin = [e for e in sup if len(e.get('overview') or '') < 150]

note = (
    '维基第88轮可用。JP-JQ：**发现"标签与深度"倒挂，并深化两个核心概念**。'
    '①**审计发现**：`tier × level` 映射完全正确（核心 34→L3、重要 502→L2、补充 105→L2，无错配），'
    '但**深度与标签倒挂**——"补充"类 overview 均长 **236 字**、timeline 均 1.7 条、key_data 均 0.9 条，'
    '反而**高于**"重要"类的 172 字／0.7／0.5。原因是补充类多为后期所写，成文更细。'
    '②**更要紧的是**：最单薄的 6 个"补充"条目里有 **`too-big-to-fail`（90 字）与 '
    '`impossible-trinity`（92 字）**——这两个都是**核心概念**，却全文最短且无 timeline／key_data。'
    '③**已深化 `too-big-to-fail`**（据专属页全文 36,058 字符）：补**伯南克 2010 年权威定义**'
    '（四要素：规模／复杂性／互联性／关键功能）与其"**并非出于偏袒**"的说明；'
    '补**处置工具的演进**——1950 年前美国只有关闭清算与购买承接**两种**选项，'
    '1950 年《联邦存款保险法》增加第三种"**提供援助**"；overview 90→**563 字**，新增 timeline 4、key_data 2。'
    '④**已深化 `impossible-trinity`**（据专属页全文 10,718 字符）：补"**为什么**"——'
    '世界利率 5%、本国想压到 2% 则资本外流、本币贬值，要守汇率就得放弃利率自主；'
    '补**1980 年代从"理论好奇"变为开放经济宏观经济学基础**的历史；'
    '补**与危机的关联**——固定汇率+资本自由流动+独立货币政策"已知会引发危机"，'
    '文献举墨西哥 1994–95／亚洲 1997–98／阿根廷 2001–02；overview 92→**554 字**。'
    '⑤**R19 在真实编辑中两次拦下我**：两次新增 timeline 都忘填 `sources`，'
    '均被 check.py 立即报错——这是 round 98 新增该规则后的**首次实战捕获**，'
    '证明它不只是自测里能过，实际写作时也真管用。'
    '⑥现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    'timeline ' + str(tl) + '、key_data ' + str(tk) + '；单薄补充条目已由 6 个降至 4 个'
    '（余 global-debt／aiib／afdb／sterling-area）。'
    '**十一道检查全绿 + 自测 18/18**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JP-JQ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 105, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + 自测 18/18',
    'spot_check': '深化 too-big-to-fail 与 impossible-trinity；R19 两次实战拦截',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 88 轮可用（round 107）**。**发现“标签与深度”倒挂，并深化两个核心概念**。
- **审计发现**：`tier × level` 映射完全正确（核心 34→L3、重要 502→L2、补充 105→L2，无错配），但**深度与标签倒挂**：

  | 组别 | overview 均长 | timeline 均 | key_data 均 |
  |---|---|---|---|
  | 重要 L2（502） | 172 字 | 0.7 | 0.5 |
  | **补充 L2（105）** | **236 字** | **1.7** | **0.9** |

  原因：补充类多为后期所写，成文更细。
- **更要紧的**：最单薄的 6 个“补充”条目里有 **`too-big-to-fail`（90 字）** 与 **`impossible-trinity`（92 字）**——两个都是**核心概念**，却全文最短且无 timeline／key_data。
- **已深化 `too-big-to-fail`**（据专属页 36,058 字符）：
  - 补**伯南克 2010 年权威定义**（四要素：**规模／复杂性／互联性／关键功能**）及其“**并非出于偏袒**”的说明
  - 补**处置工具的演进**：1950 年前美国只有关闭清算与购买承接**两种**选项，**1950 年《联邦存款保险法》**增加第三种“**提供援助**”
  - overview 90→**563 字**，新增 timeline 4、key_data 2
- **已深化 `impossible-trinity`**（据专属页 10,718 字符）：
  - 补“**为什么**”——世界利率 **5%**、本国想压到 **2%** 则资本外流、本币贬值，要守汇率就得放弃利率自主
  - 补**1980 年代**从“理论好奇”变为开放经济宏观经济学基础
  - 补**与危机的关联**——该组合“已知会引发危机”，文献举**墨西哥 1994–95／亚洲 1997–98／阿根廷 2001–02**
  - overview 92→**554 字**
- **R19 在真实编辑中两次拦下我**：两次新增 timeline 都忘填 `sources`，均被 `check.py` 立即报错——这是 round 98 新增该规则后的**首次实战捕获**。
- 单薄补充条目由 6 个降至 4 个（余 `global-debt`／`aiib`／`afdb`／`sterling-area`）。十一道检查全绿 + 自测 18/18。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JM-JO｜2026-11-24｜状态：641条；区域覆盖审计，修正crisis-33ce标注并加R20**',
              '**续作JP-JQ｜2026-11-24｜状态：641条；深化TBTF与三元悖论，R19首次实战拦截**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
