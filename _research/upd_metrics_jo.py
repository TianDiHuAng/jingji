# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
from kdclass import counts
c = counts(es)
dist = Counter(e['region'] for e in cases)

note = (
    '维基第87轮可用。JM-JO：**回到内容建设——区域覆盖审计，并修正一处区域标注**。'
    '①**区域分布审计**（209 个案例）：欧洲 61／北美 59／全球 31／拉美 17／亚洲 17／'
    '中东 11／非洲 8／大洋洲 5。'
    '②**逐区核查**：'
    '（a）**亚洲 17 条覆盖良好**——已含 1991 年印度危机（id: indian-1991）、'
    '1997 亚洲金融危机（总括条目，涵盖泰／韩／印尼／马来）、日本泡沫、昭和恐慌、'
    '中国 5 条（1937 恶性通胀／2007 股市／2013 流动性／2020 房地产／2022 河南村镇银行）、'
    '缅甸、巴基斯坦、斯里兰卡、台湾、上海橡胶 1910、孟加拉泡沫、海南 1992；'
    '（b）**非洲 8 条／中东 11 条／大洋洲 5 条**——数量偏少，但与这些地区在全球金融危机史中的'
    '相对比重相符，未发现应予补充的重大遗漏；'
    '（c）**"全球"31 条经逐条审查**，绝大多数确为跨国事件（大萧条、两次石油危机、'
    '尼克松冲击、牙买加／史密森协定、2023 银行危机、FTX／Terra 崩盘等）。'
    '③**发现一处标注不一致**：`crisis-33ce`（公元 33 年罗马危机）标为"全球"，'
    '而 U1 单元其余 9 条（含罗马第三世纪危机、罗马货币体系、罗马价格敕令）均为"欧洲"。'
    '公元前后的罗马危机地理范围与后者完全一致，已改为**欧洲**，并同步 `coverage.json`。'
    '④**加入 R20 检查**：U1（早期—17 世纪）不得标 `region=全球`——'
    '该时期尚不存在全球性金融体系。并纳入自测。'
    '⑤自测现为 **18/18**。'
    '现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '）、来源 ' + str(len(srcs)) + '、'
    '页面 ' + str(pages) + '；区域：' + '／'.join('%s %d' % (k, v) for k, v in dist.most_common()) + '。'
    '**十一道检查全绿 + 自测 18/18**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JM-JO', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 209, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + 自测 18/18（新增 R20）',
    'spot_check': '区域覆盖审计通过；crisis-33ce 区域标注修正',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 87 轮可用（round 106）**。**回到内容建设——区域覆盖审计，并修正一处区域标注**。
- **区域分布**（209 个案例）：欧洲 61／北美 59／全球 31／拉美 17／亚洲 17／中东 11／非洲 8／大洋洲 5。
- **逐区核查**：

  | 区域 | 结论 |
  |---|---|
  | **亚洲 17** | **覆盖良好**——含 1991 印度危机、1997 亚洲金融危机（总括，涵盖泰/韩/印尼/马来）、日本泡沫、昭和恐慌、中国 5 条、缅甸、巴基斯坦、斯里兰卡、台湾、上海橡胶 1910、孟加拉泡沫、海南 1992 |
  | 非洲 8／中东 11／大洋洲 5 | 数量偏少，但与这些地区在全球危机史中的相对比重相符，**未发现应予补充的重大遗漏** |
  | “全球”31 | 逐条审查，绝大多数确为跨国事件（大萧条、两次石油危机、尼克松冲击、牙买加/史密森协定、2023 银行危机、FTX/Terra 崩盘） |

- **发现一处标注不一致**：`crisis-33ce`（公元 33 年罗马危机）标为“全球”，而 **U1 单元其余 9 条均为“欧洲”**（含罗马第三世纪危机、罗马货币体系、罗马价格敕令）。已改为**欧洲**，并同步 `coverage.json`。
- **加入 R20 检查**：U1（早期—17 世纪）不得标 `region=全球`——该时期尚不存在全球性金融体系。并纳入自测。
- 自测现为 **18/18**。十一道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JK-JL｜2026-11-24｜状态：641条；自测扩至17项，覆盖全部主要检查器**',
              '**续作JM-JO｜2026-11-24｜状态：641条；区域覆盖审计，修正crisis-33ce标注并加R20**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
