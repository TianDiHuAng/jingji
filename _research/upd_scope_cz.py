# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('second-bank', '美国第二合众国银行', '制度', '北美', '## U2 18—19世纪', '18—19世纪', '补充'),
        ('free-banking', '自由银行时代', '制度', '北美', '## U2 18—19世纪', '18—19世纪', '补充'),
        ('national-banking-act', '国民银行法(1863–1864)', '制度', '北美', '## U2 18—19世纪', '18—19世纪', '补充'),
        ('sherman-silver-purchase', '谢尔曼购银法(1890)', '货币', '北美', '## U2 18—19世纪', '18—19世纪', '补充'),
        ('federal-reserve-act', '联邦储备法(1913)', '制度', '北美', '## U3 20世纪上半', '20世纪上半', '重要')]
for eid, t, c, r, sec, per, tier in rows:
    if eid in text:
        continue
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | {per} | {r} | {c} | {tier} | 续作CZ |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +5')
