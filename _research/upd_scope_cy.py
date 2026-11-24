# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('housing-bubble', '房地产泡沫', '泡沫'),
        ('informal-economy', '非正规经济', '其他'),
        ('family-office', '家族办公室', '制度'),
        ('pension-fund', '养老基金', '制度'),
        ('stabilization-program', '稳定化政策', '制度')]
for eid, t, c in rows:
    if eid in text:
        continue
    sec = '## U6 理论与制度'
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | 理论制度 | 全球 | {c} | 重要 | 续作CY |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +5')
