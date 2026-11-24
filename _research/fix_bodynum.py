# -*- coding: utf-8 -*-
"""改进 check_body_num：排除年份引用与术语，聚焦真实数值。"""
p = 'tools/check_body_num.py'
s = open(p, encoding='utf-8').read()

old = """                checked += 1
                cands = variants(num, after)
                if not any(c and (c in txt or c in own_txt) for c in cands):"""
new = """                checked += 1
                # 排除：4位年份（指向其他条目/历史时点）、常见术语中的数字
                bare = num.replace(',', '')
                try:
                    fv = float(bare)
                except ValueError:
                    continue
                if fv == int(fv) and 1000 <= fv <= 2100 and '.' not in bare and ',' not in num:
                    continue          # 视为年份
                if num in ('500', '100', '1000') and after in ('点', '只', '家', '万'):
                    pass              # 标普500等术语仍检查
                cands = variants(num, after)
                if not any(c and (c in txt or c in own_txt) for c in cands):"""

if old in s and '视为年份' not in s:
    s = s.replace(old, new, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('已排成年份引用')
else:
    print('未匹配或已改')
