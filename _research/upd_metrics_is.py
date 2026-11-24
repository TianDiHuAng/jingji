# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
from kdclass import counts
c = counts(es)

note = (
    '维基第76轮可用。IS：**穷举"文案与导航脱节"的根因，结论是自动化到此为止；另统一一处 schema 冗余**。'
    '①**穷举尝试**：上一轮修了 id 级引用（comparison 76 处 + 见xxx 20 处）。'
    '本轮检查第三种形式——正文用**中文标题**提及其他条目：粗匹配得到 **550 处**，'
    '加指示词（与／见／相比／区别于…）过滤后仍有 **154 处**。'
    '②**判断：不可自动接线**。这些绝大多数是**普通词汇用法**——'
    '"金融危机""债务危机""风险管理"本身就是常用经济词，而条目标题恰好也是这些词。'
    '自动转链接会造成严重过度链接、降低可读性。'
    '**约定**：只对英文 id 级引用自动接线；中文标题级提及不自动加链接（已写入 DECISIONS）。'
    '这是"穷举根因"的诚实结论：**能自动修的修完了，剩下的需要人工判断**。'
    '③**另查三处数据约定**：'
    '（a）`key_data.year` 无异常（无未来年份、无过早年份）；'
    '（b）**4 条 `year=0`** 是"无年份"的约定表示（门槛值等定义性数值），页面渲染为**空白**，非错误；'
    '（c）`sources.url2` 字段 **0/741** 从未使用（备选链接），保留但不要假设有值。'
    '④**统一 schema 冗余**：`schools` 此前 27 条用单值 `src`、1,222 条用 `sources` 列表，'
    '已全部统一为 `sources`（`src` 字段废弃），并确认无工具仍引用它。'
    '⑤四条约定已写入 `DECISIONS.md`，供后续轮次遵循。'
    '现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、'
    'key_data ' + str(tk) + '。**十一道检查全绿**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IS', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 27, 'reviewed': 641, 'fixed': 27,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿',
    'spot_check': '穷举接线根因（中文标题不可自动修）；schools 字段统一为 sources',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 76 轮可用（round 95）**。**穷举"文案与导航脱节"的根因——结论是自动化到此为止**；另统一一处 schema 冗余。
- **穷举尝试**（第三种形式：正文用**中文标题**提及其他条目）：

  | 匹配方式 | 命中数 |
  |---|---|
  | 粗匹配（标题出现在正文） | **550 处** |
  | 加指示词过滤（与／见／相比／区别于…） | **154 处** |

- **判断：不可自动接线**。这些绝大多数是**普通词汇用法**——"金融危机""债务危机""风险管理"本身就是常用经济词，而条目标题恰好也是这些词。自动转链接会造成**过度链接**、降低可读性。
  - **约定**：只对**英文 id 级引用**（如"见 bank-run"）自动接线；中文标题级提及**不自动加链接**（已写入 DECISIONS）
  - 这是"穷举根因"的诚实结论：**能自动修的已经修完，剩下的需要人工判断**
- **另查三处数据约定**：
  - `key_data.year` 无异常（无未来年份、无过早年份）
  - **4 条 `year=0`** 是"无年份"的约定表示（门槛值等定义性数值），页面渲染为**空白**，非错误
  - `sources.url2` 字段 **0/741** 从未使用（备选链接），保留但不要假设有值
- **统一 schema 冗余**：`schools` 此前 **27 条用单值 `src`**、**1,222 条用 `sources` 列表**，已全部统一为 `sources`（`src` 废弃），并确认无工具仍引用。
- 四条约定已写入 `DECISIONS.md`。现状：**641 条**、来源 **741**、页面 **655**。**十一道检查全绿**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IR｜2026-11-24｜状态：641条；修复"见xxx"引用未接线，两类接线缺失共96处**',
              '**续作IS｜2026-11-24｜状态：641条；穷举接线根因（自动化到此为止），统一schools字段**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
