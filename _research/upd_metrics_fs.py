# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)
pct = wk * 100 // len(cases)

note = (
    '维基第39轮可用。FS：key_data 391→' + str(tk) + '条，案例数据覆盖 83%→' + str(pct) + '%（' + str(wk) + '/' + str(len(cases)) + '）。'
    '为4个条目补6项：脱欧公投赞成票51.9%；美联储改革前全国硬币与纸币总额38亿美元、会员银行6%年度股息；'
    '英王欠美第奇银行10,500英镑（合2025年1,050万英镑）；'
    '1862年法定货币法授权发行1.5亿美元、第二次法定货币法后4.5亿美元。'
    '**其余29个缺数据案例经数字提取确认维基页面无量化指标**——多为纯事件叙述（如1901年恐慌、1882年巴黎交易所崩盘）'
    '或理论/制度讨论（如自由银行、金集团、最高价格敕令），这些条目的 key_data 属来源边界，不再强补。'
    'check_kd 可核对数由251升至257条。三道检查+check_kd 全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FS', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 33, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿；check_kd 257条可核对',
    'spot_check': 'key_data 391→' + str(tk) + '条；案例数据覆盖 83%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FR（新增check_kd工具，复核391条数值）',
              '- 当前轮次：续作FS（再补6项key_data，案例数据覆盖85%）')
entry = '''- **维基百科第 39 轮可用**。案例数据覆盖 **83% → 85%（176/205）**，`key_data` **391 → 397 条**。
- 为 4 个条目补 6 项数据：

  | 条目 | 数据 |
  |---|---|
  | 脱欧公投 2016 | 赞成票占比 **51.9%** |
  | 1913 联邦储备法 | 改革前全国硬币与纸币总额 **38 亿美元**；会员银行 **6%** 年度股息 |
  | 美第奇银行 | 英王欠款 **10,500 英镑**（合 2025 年 1,050 万英镑） |
  | 1862 法定货币法 | 授权发行 **1.5 亿 → 4.5 亿美元**（第二次法案后） |

- **其余 29 个缺数据案例经数字提取确认维基页面无量化指标**——多为纯事件叙述（1901年恐慌、1882年巴黎交易所崩盘）或理论/制度讨论（自由银行、金集团、最高价格敕令）。这属**来源边界**，不再强补。
- `check_kd` 可核对数由 251 升至 **257 条**。三道检查 + `check_kd` 全绿。
- 现状：**625 条**、来源 732、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FR｜2026-11-24｜状态：625条；新增check_kd，复核391条数值无抄错**',
              '**续作FS｜2026-11-24｜状态：625条；案例数据覆盖85%（剩余29条属来源边界）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | key_data', tk, '| 案例数据覆盖', wk, '/', len(cases), '=', pct, '%')
