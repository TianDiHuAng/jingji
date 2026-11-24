# -*- coding: utf-8 -*-
"""续作HW：用行号插入"不同统计口径对照"板块（文件为 CRLF，字符串匹配不可靠）。"""
P = 'tools/gen_site.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    lines = f.readlines()          # 保留原有行尾

# 找到 "跨语言维基对照" 的 h2 行
idx = None
for i, l in enumerate(lines):
    if '跨语言维基对照（{len(crosslang)} 条）' in l:
        idx = i
        break

if idx is None:
    print('未找到锚点行')
elif any('不同统计口径对照' in l for l in lines):
    print('板块已存在，跳过')
else:
    nl = '\r\n'
    block = [
        "vb.append(f'<h2>不同统计口径对照（{len(statview)} 条）</h2>')",
        "vb.append('<p class=\"src-list\">以下数值由 OWID／世界银行等统计汇总机构与维基来源相互对照。"
        "须说明：这些机构的数据本身汇总自各国官方统计，而维基所载数字往往源自同一批官方统计——"
        "两者属不同加工口径（国际可比调整 vs 原始公布），不构成严格独立的信息生产链。"
        "故本板块单列，不与「独立机构印证」合并计数。</p>')",
        "if statview:",
        "    vb.append('<table><tr><th>条目</th><th>数据项</th><th>数值</th><th>年份</th></tr>'",
        "              + ''.join(_kd_row(e, k) for e, k, _ in sorted(statview, key=lambda x: x[0]['id'])) + '</table>')",
        "else:",
        "    vb.append('<p>（暂无）</p>')",
        "",
    ]
    lines[idx:idx] = [b + nl for b in block]
    with open(P, 'w', encoding='utf-8', newline='') as f:
        f.writelines(lines)
    print('已在第 %d 行前插入统计口径板块（%d 行）' % (idx + 1, len(block)))
