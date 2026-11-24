# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])

note = (
    '维基第24轮不可达。EP为全部606页补充 meta description——此前**606页全部缺失**。'
    '实施：page() 增加 desc 参数；条目页用 one_line + 时期/地区/危机类型 自动生成'
    '（例：雷曼="美国全球金融服务公司雷曼兄弟1850年成立，2008年破产前为美国第四大投行、约2.5万员工。 21世纪 · 北美 · 银行"），'
    '9类索引页（首页/全站索引/时间线/来源/矩阵/概念/案例/单元）各有专门摘要，单元页复用 round 39 加入的时期导语。'
    '长度上限150字（超出截断加省略号），去除 Markdown 标记。'
    '结果：**606页零缺失、606个唯一 description**（无重复），check.py 与 check_links 均 0 error。'
    '同时核查通过：重复 title 0 个、h1 数量全部=1、页内锚点目标全部存在。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EP', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 606, 'reviewed': 606, 'fixed': 1,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': 'description 606/606 唯一；重复title 0；h1全=1；锚点全部有效',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EL-EO（SVG重复id与重复属性修复，三次迭代）',
              '- 当前轮次：续作EP（606页补 meta description）')
entry = '''- **维基百科第 24 轮不可达**。
- 续作EP：**为全部 606 页补充 `meta description`**——此前 **606 页全部缺失**（SEO 与社交分享的关键元数据）。
  - 条目页自动生成：`one_line` + 时期/地区/危机类型。例：雷曼 →「美国全球金融服务公司雷曼兄弟1850年成立，2008年破产前为美国第四大投行、约2.5万员工。 21世纪 · 北美 · 银行」
  - 9 类索引页（首页/全站索引/时间线/来源/矩阵/概念/案例/单元）各有专门摘要；单元页复用 round 39 加入的时期导语
  - 长度上限 150 字（超出截断加省略号），去除 Markdown 标记
- 结果：**606 页零缺失、606 个唯一 description（无重复）**。
- 同时核查**通过**：重复 `title` **0 个**；`h1` 数量全部 **=1**；页内锚点目标**全部存在**。
- 现状：**总592条，来源695，站点606页**；comparison 与 related 双 100%。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EL-EO｜2026-11-24｜状态：592条；SVG重复id清零（三次迭代）**',
              '**续作EP｜2026-11-24｜状态：592条；606页meta description补齐**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
