# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('european-central-bank', '欧洲中央银行(ECB)', '制度', '欧洲'),
        ('circuit-breaker', '熔断机制（交易限制）', '制度', '全球'),
        ('commodity-price-index', '商品价格指数与商品周期', '理论', '全球'),
        ('municipal-bond', '市政债券与地方政府债务', '制度', '全球')]
for eid, t, c, r in rows:
    if eid in text:
        continue
    sec = '## U6 理论与制度'
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | 理论制度 | {r} | {c} | 重要 | 续作DD |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +4')
