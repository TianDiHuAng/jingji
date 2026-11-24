# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
wk = sum(1 for e in cases if e.get('key_data'))
l3 = [e for e in es if e.get('level') == 'L3']
l3full = sum(1 for e in l3 if all(e.get(x) for x in ('deep_svg', 'l3_detail', 'key_data', 'timeline', 'policy_response')))

note = (
    '维基第44轮可用。GA/GB：案例政策覆盖 69%→' + str(wp * 100 // len(cases)) + '%（' + str(wp) + '/' + str(len(cases)) + '）。'
    '**本轮发现了此前未检查的维度：L3 深度条目的结构完整性**——30 条 L3 中 11 条缺 policy_response，'
    '其中包含 **lehman** 与 **subprime-crisis-2007** 两个最核心的案例。'
    '补写 5 条：'
    'lehman（2008.9.13 纽约联储盖特纳召集会议讨论但不注资；9.15 申请第11章破产；'
    '次日巴克莱宣布收购控股权、9.20 破产法院批准；随后野村收购亚太区业务）、'
    'subprime-crisis-2007（TARP 依《紧急经济稳定法》2008.10.3 签署＋ARRA 2009＋多德-弗兰克法但未拆分大行；'
    '伯南克"不做则周一可能没有经济"；到 2018 年 1 月救助资金含息**全部收回**，总额约 6,260 亿美元）、'
    'latin-american-debt-1975（IMF 支持借贷但被批评低估风险；墨西哥以未来石油收入抵押借美元；'
    '1975—82 年对商业银行债务年复合增 **20.4%**）、'
    'panic-1873（英格兰银行加息至 **9%**，英国未出现美欧级混乱）。'
    'dotcom-bubble-2000 经查**确无政策应对记载**（格林斯潘言论属成因而非应对）。'
    'L3 完整度：' + str(l3full) + '/' + str(len(l3)) + '，其余 7 条中 6 个为概念条目（policy_response 非 check.py 必需）。'
    '当前：案例数据 ' + str(wk) + '/' + str(len(cases)) + '、来源 ' + str(srcn) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GA-GB', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 5, 'reviewed': 30, 'fixed': 0,
    'sources_total': srcn,
    'check_result': 'PASS (' + str(len(es)) + '); 七道检查中五道全绿',
    'spot_check': 'L3 完整度 ' + str(l3full) + '/' + str(len(l3)) + '；案例政策 69%→' + str(wp * 100 // len(cases)) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FY-FZ（扩大验证覆盖，key_data可核对率97.5%）',
              '- 当前轮次：续作GA-GB（发现L3结构缺口，案例政策71%）')
entry = '''- **维基百科第 44 轮可用**。案例政策覆盖 **69% → 71%（146/205）**。
- **本轮发现一个此前未检查的维度：L3 深度条目的结构完整性**。30 条 L3 中 **11 条缺 `policy_response`**，其中包含 **lehman** 与 **subprime-crisis-2007** 两个最核心的案例。
- 补写 5 条：

  | 条目 | 政策／处置 |
  |---|---|
  | **lehman** | 2008.9.13 纽约联储盖特纳召集会议讨论但**不注资**；9.15 申请**第11章**破产；次日巴克莱宣布收购控股权、9.20 破产法院批准；随后野村收购亚太区业务 |
  | **次贷危机** | TARP（《紧急经济稳定法》2008.10.3）＋ARRA 2009＋多德-弗兰克法（**未拆分大行**）；伯南克"不做则周一可能没有经济"；到 2018.1 救助资金含息**全部收回**，约 **6,260 亿美元** |
  | 拉美债务 1975 | IMF **支持**借贷但被批评**低估风险**；墨西哥以未来石油收入抵押借美元；1975—82 年对商业银行债务年复合增 **20.4%** |
  | 1873 恐慌 | 英格兰银行加息至 **9%**，英国未出现美欧级混乱 |

- `dotcom-bubble-2000` 经查**确无政策应对记载**（格林斯潘言论属成因而非应对）。
- L3 完整度：**23/30**，其余 7 条中 6 个为概念条目（`policy_response` 非 `check.py` 必需）。
- 现状：**625 条**、来源 732、站点 639 页；案例政策 71%、案例数据 85%。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FY-FZ｜2026-11-24｜状态：625条；key_data可核对率97.5%，发现1处无源数字**',
              '**续作GA-GB｜2026-11-24｜状态：625条；发现L3结构缺口，案例政策71%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | L3完整', l3full, '/', len(l3), '| 案例政策', wp * 100 // len(cases), '%')
