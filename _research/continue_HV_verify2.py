# -*- coding: utf-8 -*-
"""续作HV：修正验证页分类（分步、简化写法）。"""
P = 'tools/gen_site.py'
s = open(P, encoding='utf-8').read()

# --- 步骤1：初始化 statview ---
if 'statview = []' not in s:
    s = s.replace("confirmed, discrepant, crosslang = [], [], []",
                  "confirmed, discrepant, crosslang, statview = [], [], [], []")
    print('1) 已初始化 statview')

# --- 步骤2：拆分类别 ---
old2 = "        elif has_official and any(w in note for w in _confkw):\n            confirmed.append((e, k, has_official))       # 独立机构互证"
new2 = ("        elif any(str(x).startswith('fed-') for x in srcs) and any(w in note for w in _confkw):\n"
        "            confirmed.append((e, k, has_official))       # 独立撰写（美联储历史研究）\n"
        "        elif any(str(x).startswith(('owid-', 'org-')) for x in srcs) and any(w in note for w in _confkw):\n"
        "            statview.append((e, k, has_official))        # 不同统计口径对照")
if old2 in s and 'statview.append' not in s:
    s = s.replace(old2, new2, 1)
    print('2) 已拆分类别')

# --- 步骤3：插入统计口径板块 ---
anchor = "vb.append(f'<h2>跨语言维基对照（{len(crosslang)} 条）</h2>')"
block_lines = [
    "vb.append(f'<h2>不同统计口径对照（{len(statview)} 条）</h2>')",
    "vb.append('<p class=\"src-list\">以下数值由 OWID／世界银行等统计汇总机构与维基来源相互对照。须说明：这些机构的数据本身汇总自各国官方统计，而维基所载数字往往源自同一批官方统计——两者属不同加工口径（国际可比调整 vs 原始公布），不构成严格独立的信息生产链。故本板块单列，不与「独立机构印证」合并计数。</p>')",
    "if statview:",
    "    vb.append('<table><tr><th>条目</th><th>数据项</th><th>数值</th><th>年份</th></tr>'",
    "              + ''.join(_kd_row(e, k) for e, k, _ in sorted(statview, key=lambda x: x[0]['id'])) + '</table>')",
    "else:",
    "    vb.append('<p>（暂无）</p>')",
    "",
]
block = '\n'.join(block_lines) + anchor
if '不同统计口径对照' not in s:
    s = s.replace(anchor, block, 1)
    print('3) 已插入统计口径板块')

# --- 步骤4：更新独立印证说明（用较短的匹配串）---
old4 = '美联储历史站、世界银行/OWID 等'
new4 = '独立撰写的历史研究机构，如美联储历史站 Federal Reserve History'
if old4 in s:
    s = s.replace(old4, new4, 1)
    print('4) 已更新独立印证说明')

# --- 步骤5：日志 ---
s = s.replace("len(confirmed), len(crosslang), len(discrepant), len(_off)",
              "len(confirmed), len(statview), len(crosslang), len(discrepant), len(_off)")
s = s.replace("独立机构印证 %d 条、跨语言对照 %d 条、差异并列 %d 条",
              "独立机构印证 %d 条、统计口径对照 %d 条、跨语言对照 %d 条、差异并列 %d 条")

open(P, 'w', encoding='utf-8').write(s)
print('写入完成')
