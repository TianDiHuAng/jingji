# -*- coding: utf-8 -*-
"""续作GW：首页统计卡片增加"跨语言对照"与"政策应对覆盖"，让核实维度更完整可见。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

# 1) 计算 crosslang 总数（在生成首页前算出，供卡片使用）
anchor = "        and any(str(x).startswith(('fed-', 'owid-')) for x in (k.get('sources') or [])))"
add_calc = anchor + """
# 跨语言对照：条目引用 >=2 种语言的维基
def _nlang(e):
    ls = {str(x).split('-')[1] for x in (e.get('sources') or [])
          if str(x).startswith('w-') and len(str(x).split('-')) > 1}
    return len({l for l in ls if l in ('en', 'zh', 'de', 'fr', 'es', 'ja')})
_cross_total = sum(len(e.get('key_data') or []) for e in entries.values() if _nlang(e) >= 2)
_cases = [e for e in entries.values() if not str(e.get('unit', '')).startswith('U6')]
_pol_cases = sum(1 for e in _cases if e.get('policy_response'))"""

if '_cross_total' not in s:
    s = s.replace(anchor, add_calc, 1)

# 2) 卡片：把"已获第二来源印证"扩展为三项
old_card = (""" f'<div class="stat"><div class="n">{conf_total}</div><div class="l">已获第二来源印证</div></div></div>',""")
new_card = (""" f'<div class="stat"><div class="n">{conf_total}</div><div class="l">已获第二来源印证</div></div>'
 f'<div class="stat"><div class="n">{_cross_total}</div><div class="l">跨语言维基对照</div></div>'
 f'<div class="stat"><div class="n">{_pol_cases}/{len(_cases)}</div><div class="l">案例载有政策应对</div></div></div>',""")

if old_card in s:
    s = s.replace(old_card, new_card, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('首页统计已扩展')
else:
    print('未匹配卡片代码')
