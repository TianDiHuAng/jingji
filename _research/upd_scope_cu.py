# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('continental-illinois-1984', '伊利诺伊大陆银行救助(1984)', '银行', '北美', '## U4 20世纪下半', '重要'),
        ('penn-square-1982', 'Penn Square 银行倒闭(1982)', '银行', '北美', '## U4 20世纪下半', '补充'),
        ('franklin-national-1974', 'Franklin National 银行倒闭(1974)', '银行', '北美', '## U4 20世纪下半', '补充'),
        ('albania-pyramid-1997', '阿尔巴尼亚金字塔骗局与1997年动乱', '泡沫', '欧洲', '## U4 20世纪下半', '重要'),
        ('settlement-risk', '结算风险(Herstatt风险)', '制度', '全球', '## U6 理论与制度', '补充')]
for eid, t, c, r, sec, tier in rows:
    if eid in text:
        continue
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    per = '理论制度' if sec.startswith('## U6') else '20世纪下半'
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | {per} | {r} | {c} | {tier} | 续作CU |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +5')
