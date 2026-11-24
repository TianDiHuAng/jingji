# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
reln = sum(1 for e in es if e.get('related'))

note = (
    '维基第21轮不可达。EI做两件事：'
    '①数据字段一致性核查：unit/period 对应关系 0 处不一致；region 取值合法（全球411/欧洲64/北美59/'
    '拉美17/亚洲17/中东11/非洲8/大洋洲5）；crisis_type 取值合法（制度169/理论127/货币91/银行75/'
    '泡沫41/债务37/其他37/恶性通胀15）；U6 条目可有具体地区（如 bank-of-england 为欧洲），属合理设计。'
    '②站点性能核查：style.css 仅 3.6KB、平均页面 6KB、全站 3MB/606页，深色模式齐备，无 JS。'
    '③**为6个单元页添加时期导语**（此前仅有"本单元共N条"一句）——'
    '按已有条目归纳各时期主线：U1货币成色与贸易信贷、U2恐慌序列与最后贷款人确立、'
    'U3金本位解体与大萧条、U4处置方式演进(1974任其倒闭→1984全面保护→1990s瑞典国有化)、'
    'U5危机主体转向非银机构、U6按主题分类导读。'
    '修复 markdown 粗体未渲染问题（**→<strong>）。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EI', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 6, 'reviewed': 606, 'fixed': 2,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': '字段一致性0问题；6个单元页新增时期导语',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EG-EH（related达成100%全覆盖）',
              '- 当前轮次：续作EI（单元页导语+字段/性能核查）')
entry = '''- **维基百科第 21 轮不可达**。转向站点质量工作。
- **字段一致性核查（0 问题）**：`unit`/`period` 对应关系全部正确；`region` 取值合法（全球411／欧洲64／北美59／拉美17／亚洲17／中东11／非洲8／大洋洲5）；`crisis_type` 取值合法（制度169／理论127／货币91／银行75／泡沫41／债务37／其他37／恶性通胀15）。U6 条目可有具体地区（如 `bank-of-england` 为欧洲），属合理设计而非错误。
- **站点性能核查**：`style.css` 仅 **3.6KB**、平均页面 **6KB**、全站 **3MB/606页**，深色模式齐备，零 JavaScript。
- **为 6 个单元页添加时期导语**（此前只有"本单元共 N 条"一句）。导语由已有条目归纳，不引入新事实：
  - **U1**：主角是货币成色、贸易信贷与国家财政；三条线索是罗马贬损、14世纪佛罗伦萨银行崩塌、17世纪早期泡沫
  - **U2**：现代危机形态成形的时期——恐慌序列（1792→1910）、金本位确立、最后贷款人原则确立
  - **U3**：货币秩序崩塌——金本位解体、大萧条、退出 vs 坚持金本位决定复苏速度
  - **U4**：**处置方式演进**的关键期——1974"任其倒闭"→1984"全面保护存款人"→1990s瑞典"及时国有化"，这条路径通向2008
  - **U5**：危机主体**从银行转向非银机构**（Archegos、LDI、加密）
  - **U6**：按主题分类的导读，建议与案例对照阅读
- 同时修复导语中 Markdown 粗体未渲染的问题（`**` → `<strong>`）。
- 现状：**总592条，来源695，站点606页**。comparison 与 related 双 100%。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EG-EH｜2026-11-24｜状态：592条；comparison 与 related 双100%**',
              '**续作EI｜2026-11-24｜状态：592条；单元页导语已加，双100%维持**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
