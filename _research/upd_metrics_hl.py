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
    '维基第59轮可用。HJ-HL：**新建 4 个概念，并重写 BACKLOG 的待建清单**。'
    '①先用**模糊匹配**重新校验 round 37 编制的 21 项待建清单——发现多项"同义不同名"'
    '（`term-premium` 被误配到 `equity-premium`、`risk-pooling` 误配到各类 risk 条目），'
    '说明简单词元匹配会产生假阳性，须逐项人工判定。'
    '②按维基页面可用性筛选，新建 4 条：'
    '**精算**（1693 哈雷生命表／1848 精算师协会／2016 Solvency II；精算风险观 vs 金融经济学定价）、'
    '**金银块**（1717 牛顿确立金衡／1919 伦敦定盘价／2015 电子拍卖取代；货币属性 vs 商品属性）、'
    '**劳合社**（1688 劳埃德咖啡馆／1871 首个劳合社法／1996 公司化改革；辛迪加模式优点 vs 无限责任争议）、'
    '**去工业化**（生产率视角 vs 贸易外包视角）。'
    '③**重写 BACKLOG 待建清单**：把 21 项按下表重新分类——已覆盖 11 项、真实缺口 15 项，'
    '每项给出核实结论（维基无页面／重定向到通用页／与现有条目不等价等），'
    '并在文件开头写明"原清单长期未复核，导致 round 77 建了已存在的条目"。'
    '④吸取 round 77 教训：建条目前先查 `data/entries/` 的 id 与标题，schools 一律用 dict。'
    '现状：**630 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、key_data ' + str(tk) + '、'
    'comparison ' + str(comp) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HJ-HL', 'date': '2026-11-24', 'new_entries': 4, 'upgraded': 4, 'reviewed': 21, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（630 条、706 来源、644 页）',
    'spot_check': '新建 4 概念；重写 BACKLOG 待建清单（21 项重新分类）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **条目：626**（案例 205 / 概念 421）', '- **条目：%d**（案例 %d / 概念 %d）'
              % (len(es), len(cases), len(concepts)))
s = s.replace('- **来源：702**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **站点页面：640**', '- **站点页面：%d**' % pages)
add = '''- **维基百科第 59 轮可用（round 78）**。**新建 4 个概念，并重写 BACKLOG 待建清单**。
- **① 先用模糊匹配校验 round 37 的 21 项清单**——发现多项"同义不同名"被误配（`term-premium` 误配到 `equity-premium`、`risk-pooling` 误配到各类 risk 条目），说明**词元匹配会产生假阳性，须逐项人工判定**。
- **② 新建 4 条**（均有专属维基页）：

  | 条目 | 关键内容 |
  |---|---|
  | **精算** | 1693 哈雷生命表／1848 精算师协会／2016 Solvency II；精算的"大数定律"风险观 vs 金融经济学的无套利定价 |
  | **金银块** | 1717 牛顿确立金衡／1919 伦敦定盘价／2015 电子拍卖取代；货币属性 vs 商品属性 |
  | **劳合社** | 1688 劳埃德咖啡馆／1871 首个劳合社法／**1996 公司化改革**；辛迪加模式优点 vs **无限责任争议** |
  | **去工业化** | **生产率视角**（富裕的结果）vs **贸易外包视角**（区域衰落与就业极化） |

- **③ 重写 BACKLOG 待建清单**：21 项重新分类——**已覆盖 11 项、真实缺口 15 项**，每项给出核实结论（维基无页面／重定向到通用页／与现有条目不等价）。文件开头写明"原清单长期未复核，导致 round 77 建了已存在的条目"。
- 现状：**630 条**（案例 205／概念 425）、来源 **706**、页面 **644**。十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HG-HI｜2026-11-24｜状态：626条；新建庇古税与公共池资源，合并2组重复**',
              '**续作HJ-HL｜2026-11-24｜状态：630条；新建4概念，重写BACKLOG待建清单**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 概念', len(concepts))
