# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
pct = cmpn * 100 // len(es)

note = (
    '维基第17轮不可达。EC一次补70组概念辨析，覆盖达 ' + str(pct) + '%。重点：'
    '固定vs浮动汇率（谁承担调整：汇率vs国内物价就业）、'
    '外汇储备vs主权财富基金（消防水vs长期储蓄，风险偏好与治理不同）、'
    '前瞻指引vs规则（承诺强度；2013缩减恐慌即沟通失误）、'
    '政府债务vs私人债务（能否印钞，决定相同债务率的天壤风险差异）、'
    '大稳健的错觉（低CPI不等于金融稳定）、'
    '房地产泡沫vs股票泡沫（杠杆与银行绑定，故破坏力远超股市）、'
    '恶性通胀vs高通胀（月率50%是质变：货币职能瓦解、铸币税收入反降）、'
    '指数化vs通胀目标制（适应通胀vs压制通胀，逻辑相反）、'
    '信息不对称vs根本不确定性（可缓解vs只能靠缓冲）、'
    '利率风险vs信用风险（2023年SVB与2022年LDI核心是利率风险）、'
    '柠檬市场vs道德风险（交易前逆向选择vs交易后行为改变）、'
    '明斯基时刻vs明斯基理论（何时崩vs为何崩）、'
    '货币市场vs资本市场（货币市场是体系水管，冻结即失灵）、'
    '波动率≠风险（高波动可双向、低波动可掩盖尾部）、'
    '二级市场流动性决定一级发行成本、'
    '养老基金vs主权财富基金（负债驱动vs资产驱动，LDI危机的关键）。'
    'comparison覆盖 ' + str(cmpn) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EC', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 70, 'reviewed': 70, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': 'comparison 450→' + str(cmpn) + '条(' + str(pct) + '%)',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EB（58组概念辨析，comparison 450条）',
              '- 当前轮次：续作EC（70组概念辨析，comparison 520条）')
entry = '''- **维基百科第 17 轮不可达**。
- 续作EC：**一次补 70 组概念辨析**，`comparison` 覆盖 **450 → 520 条（87%）**。重点区分：
  - **固定 vs 浮动汇率**：核心是"谁承担调整"——浮动由**汇率**吸收（价格调整），固定由**国内物价与就业**吸收（数量调整，更痛苦）。这解释了大萧条中坚持金本位的国家为何承受更久通缩
  - **外汇储备 vs 主权财富基金**：前者是"**消防水**"（高流动性低风险、不能亏损），后者是"长期储蓄"（可逆周期投资）。混淆会导致储备被不当投资
  - **政府债务 vs 私人债务**：关键在"能否印钞"——同样是债务/GDP 100%，本币债务与外币债务的风险天差地别（原罪问题）
  - **大稳健的错觉**：低 CPI **不等于**金融稳定——2008年前"通胀目标制运转良好"与"系统性风险悄悄累积"可以并存
  - **房地产泡沫 vs 股票泡沫**：房市有**高杠杆+银行深度绑定+供给调整慢**，故破坏力远超股市——2000年纳指跌78%只造成温和衰退，2007年房价下跌引发全球危机
  - **波动率 ≠ 风险**：高波动可双向（不必然是坏），低波动可掩盖尾部风险（2007年"低波动"被视为安全，实为杠杆累积）
  - **养老基金 vs 主权财富基金**：**负债驱动 vs 资产驱动**——2022年英国LDI危机正因养老基金为匹配久期而杠杆对冲，反在利率急升时被迫抛售
- 现状：**总592条，来源695，站点606页**。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EB｜2026-11-24｜状态：592条；comparison 450条（76%）**',
              '**续作EC｜2026-11-24｜状态：592条；comparison 520条（87%）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', cmpn, '/', len(es), '=', pct, '%')
