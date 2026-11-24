# -*- coding: utf-8 -*-
text = open('scope.md', encoding='utf-8').read()
rows = [('procyclicality', '顺周期性与逆周期变量', '理论'),
        ('margin-call', '保证金与追加保证金', '制度'),
        ('secular-stagnation', '长期停滞', '理论'),
        ('financialization', '金融化', '其他'),
        ('asset-liability-mismatch', '资产负债错配（含货币错配）', '理论')]
for eid, t, c in rows:
    if eid in text:
        continue
    sec = '## U6 理论与制度'
    s = text.find(sec)
    n = text.find('\n## ', s + 4)
    if n < 0:
        n = len(text)
    text = text[:s] + text[s:n].rstrip('\n') + '\n' + \
        f'| {eid} | {t} | 理论制度 | 全球 | {c} | 重要 | 续作CW |\n' + text[n:]
open('scope.md', 'w', encoding='utf-8').write(text)
print('scope +5')
