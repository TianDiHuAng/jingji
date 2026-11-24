# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
reln = sum(1 for e in es if e.get('related'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]

note = (
    '**维基百科恢复**（前25轮全部不可达）。ES/ET/EU/EV四步完成首批补建：'
    '①抓取29个BACKLOG概念摘要（26成功+3修正slug），逐一核对内容匹配度，'
    '发现10个维基无独立条目（重定向到宽泛条目：bank-resolution→bank failure、'
    'clearage-ratio→leverage、ring-fencing→hypothecation、taper-tantrum→QE、'
    'term-premium→yield curve、originate-to-distribute→securitization等），**未强建以免用错误来源**；'
    '②为19个内容匹配者中18个新建条目（externality已存在），涵盖长期缺失的**基础概念地基**：'
    '经济增长、衰退、效用、市场失灵、寻租、预期、有效需求、收敛、莫迪利亚尼-米勒定理、'
    '股权溢价之谜、对手方风险、部分准备金银行、次级化、自营交易、共同基金、纳斯达克、欧洲美元、股息。'
    '这直接回应了round 37的判断——本站概念覆盖偏向"金融专门术语"而基础地基不完整；'
    '③每个新条目均含摘要来源、对照辨析、语义关联，comparison与related重回100%；'
    '④新增17个维基来源（695→712）。总条目592→610、站点606→624页。三道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作ES-EV', 'date': '2026-11-24', 'new_entries': 18, 'upgraded': 18, 'reviewed': 29, 'fixed': 2,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '总条目 592→' + str(len(es)) + '；comparison/related 双 100%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EQ-ER（概念缺口检查法 + 新检查工具）',
              '- 当前轮次：续作ES-EV（**维基恢复**，首批补建18个基础概念）')
entry = '''- **维基百科恢复**（前 25 轮全部不可达）。本轮完成首批概念补建，总条目 **592 → 610**。
- 步骤：抓取 29 个 BACKLOG 概念摘要 → 逐一核对内容匹配度 → 建条目 → 补辨析与关联。
- **关键判断：10 个概念维基无独立条目，未强建**。它们都重定向到了宽泛条目：

  | 概念 | 重定向到 |
  |---|---|
  | `bank-resolution` | Bank failure |
  | `leverage-ratio` | Leverage (finance) |
  | `ring-fencing` | Hypothecation (tax) |
  | `taper-tantrum` | Quantitative easing |
  | `term-premium` | Yield curve |
  | `originate-to-distribute` | Securitization |
  | 另 4 个 | 同类 |

  用错误的上位条目做来源，等于让"银行处置"条目引用"银行倒闭"的内容——内容对不上。宁可留空。
- **新建 18 个条目**，正是 round 37 指出的"基础概念地基"：
  经济增长、衰退、效用、市场失灵、寻租、预期、有效需求、收敛、莫迪利亚尼-米勒定理、股权溢价之谜、对手方风险、部分准备金银行、次级化、自营交易、共同基金、纳斯达克、欧洲美元、股息。
- 每个新条目均含：摘要来源、对照辨析（如衰退 vs 萧条、市场失灵 vs 政府失灵、效用 vs 价值、收敛 vs 分化）、语义关联。
- `comparison` 与 `related` 重回 **100%（610/610）**；来源 **695 → 712**；站点 **606 → 624 页**。
- 三道检查（check / check_links / check_quality）**全绿**。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EQ-ER｜2026-11-24｜状态：592条；新增 check_quality.py（三道检查全绿）**',
              '**续作ES-EV｜2026-11-24｜状态：维基恢复，610条（+18 基础概念）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 概念', len(concepts), '| 案例', len(cases), '| 来源', src)
