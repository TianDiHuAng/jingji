# -*- coding: utf-8 -*-
"""续作HX：首页"已获第二来源印证"改用与验证页一致的判据（仅 fed-* 独立撰写），
并把"统计口径对照"作为独立卡片显示。"""
P = 'tools/gen_site.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

old = """conf_total = sum(1 for e in entries.values() for k in (e.get('key_data', []) or [])
                 if ('双源' in (k.get('note') or '') or '印证' in (k.get('note') or '')
                     or '完全一致' in (k.get('note') or ''))
                 and any(str(x).startswith(('fed-', 'owid-')) for x in (k.get('sources') or [])))"""
new = """# 独立机构印证：仅限 fed-*（美联储历史站等独立撰写的史学研究），与验证页判据一致
conf_total = sum(1 for e in entries.values() for k in (e.get('key_data', []) or [])
                 if ('双源' in (k.get('note') or '') or '印证' in (k.get('note') or '')
                     or '完全一致' in (k.get('note') or ''))
                 and any(str(x).startswith('fed-') for x in (k.get('sources') or []))
                 and not any(w in (k.get('note') or '') for w in
                             ('两源差异', '存在差异', '数据分歧', '口径不同')))
# 统计口径对照：OWID／世界银行等（与维基数字同源于各国官方统计，独立性有限）
stat_total = sum(1 for e in entries.values() for k in (e.get('key_data', []) or [])
                 if ('双源' in (k.get('note') or '') or '印证' in (k.get('note') or '')
                     or '完全一致' in (k.get('note') or ''))
                 and any(str(x).startswith(('owid-', 'org-')) for x in (k.get('sources') or []))
                 and not any(str(x).startswith('fed-') for x in (k.get('sources') or []))
                 and not any(w in (k.get('note') or '') for w in
                             ('两源差异', '存在差异', '数据分歧', '口径不同')))"""

if old in s:
    s = s.replace(old, new, 1)
    print('1) 判据已修正')
else:
    print('1) 未匹配判据')

card_old = """ f'<div class="stat"><div class="n">{conf_total}</div><div class="l">已获第二来源印证</div></div>'"""
card_new = (""" f'<div class="stat"><div class="n">{conf_total}</div><div class="l">独立机构双源印证</div></div>'
 f'<div class="stat"><div class="n">{stat_total}</div><div class="l">统计口径对照</div></div>'""")
if card_old in s:
    s = s.replace(card_old, card_new, 1)
    print('2) 卡片已拆分')
else:
    print('2) 未匹配卡片')

with open(P, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print('写入完成')
