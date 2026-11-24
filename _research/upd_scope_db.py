# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('first-bank', '美国第一合众国银行', '制度', '北美', '## U2 18—19世纪', '18—19世纪', '补充'),
        ('overend-gurney', 'Overend, Gurney 倒闭(1866)', '银行', '欧洲', '## U2 18—19世纪', '18—19世纪', '重要'),
        ('indexation', '指数化', '制度', '全球', '## U6 理论与制度', '理论制度', '补充'),
        ('interest-rate-risk', '利率风险', '理论', '全球', '## U6 理论与制度', '理论制度', '补充')]
for eid, t, c, r, sec, per, tier in rows:
    if eid in text:
        continue
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | {per} | {r} | {c} | {tier} | 续作DB |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +4')
