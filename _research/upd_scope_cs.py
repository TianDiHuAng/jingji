# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('nyc-fiscal-1975', '纽约市财政危机(1975)', '债务', '北美', '## U4 20世纪下半'),
        ('swedish-crisis-1990s', '瑞典金融危机(1990–1994)', '银行', '欧洲', '## U4 20世纪下半')]
for eid, t, c, r, sec in rows:
    if eid in text:
        continue
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | 20世纪下半 | {r} | {c} | 重要 | 续作CS |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +2')
