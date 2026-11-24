# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('fixed-exchange-rate', '固定汇率制度', '制度'), ('floating-exchange-rate', '浮动汇率制度', '制度'),
        ('transition-economy', '转轨经济', '其他'), ('lemons-market', '柠檬市场（信息不对称与逆向选择）', '理论'),
        ('money-laundering', '洗钱', '其他'), ('currency-war', '货币战（竞争性贬值）', '货币'),
        ('malinvestment', '错误投资（奥地利学派）', '理论')]
for eid, t, c in rows:
    if eid in text:
        continue
    sec = '## U6 理论与制度'
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | 理论制度 | 全球 | {c} | 重要 | 续作DF |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +7')
