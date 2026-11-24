# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('archegos-2021', 'Archegos 爆仓(2021)', '银行', '北美'),
        ('uk-ldi-crisis-2022', '英国LDI危机(2022)', '制度', '欧洲')]
for eid, t, c, r in rows:
    if eid in text:
        continue
    sec = '## U5 21世纪'
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | 21世纪 | {r} | {c} | 重要 | 续作CV |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +2')
