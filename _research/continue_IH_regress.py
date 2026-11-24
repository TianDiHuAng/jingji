# -*- coding: utf-8 -*-
"""续作IH：修正回归——NBER 与维基是"原始出处与转引"关系，不得计入独立印证。

round 81 已在两条衰退条目的 note 中写明"NBER 为原始出处、维基为转引，二者不构成相互独立的双源印证"，
但 round 88 把 org-nber 加入 INDEP_DOC_IDS 后，这两条又被算进了"独立机构印证"。

修正：判据中增加**否定词排除**——note 含"不构成""原始出处""转引"者，一律不计入独立印证。
"""
P = 'tools/gen_site.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

# 1) 从 INDEP_DOC_IDS 移除 org-nber
if "'org-nber'," in s:
    s = s.replace("INDEP_DOC_IDS = {'org-imf-glossary', 'org-bis', 'org-fsb', 'org-nber',",
                  "INDEP_DOC_IDS = {'org-imf-glossary', 'org-bis', 'org-fsb',")
    print('1) 已从 INDEP_DOC_IDS 移除 org-nber')

# 2) 判据增加否定词排除
old = "        _is_diff = any(w in note for w in _diffkw) and not ('方向与量级一致' in note)"
new = ("        _is_diff = any(w in note for w in _diffkw) and not ('方向与量级一致' in note)\n"
       "        # 若 note 明示"非独立来源/系转引"，则不计入独立印证\n"
       "        _not_indep = any(w in note for w in ('不构成独立', '不构成相互独立', '原始出处', '系转引'))")
if old in s and '_not_indep' not in s:
    s = s.replace(old, new, 1)
    print('2) 已加入否定词排除')

# 3) 在 confirmed 分支加 _not_indep 条件
old2 = ("        elif (any(str(x).startswith('fed-') for x in srcs)\n"
        "              or any(str(x) in INDEP_DOC_IDS for x in srcs)) \\\n"
        "             and any(w in note for w in _confkw):")
new2 = ("        elif (any(str(x).startswith('fed-') for x in srcs)\n"
        "              or any(str(x) in INDEP_DOC_IDS for x in srcs)) \\\n"
        "             and any(w in note for w in _confkw) and not _not_indep:")
if old2 in s:
    s = s.replace(old2, new2, 1)
    print('3) confirmed 已加入 _not_indep 条件')

with open(P, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print('写入完成')
