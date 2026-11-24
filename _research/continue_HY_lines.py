# -*- coding: utf-8 -*-
"""续作HY：用行号替换首页判据（CRLF 文件，字符串匹配不可靠）。"""
P = 'tools/gen_site.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    lines = f.readlines()

# 定位 conf_total 的起止（从 'conf_total = sum' 到该语句结束）
start = None
for i, l in enumerate(lines):
    if l.startswith('conf_total = sum'):
        start = i
        break

if start is None:
    print('未找到 conf_total')
else:
    # 该语句跨 4 行（到以 ')' 结尾且不含续行的行）
    end = start
    depth = 0
    for j in range(start, min(start + 12, len(lines))):
        depth += lines[j].count('(') - lines[j].count(')')
        if depth <= 0:
            end = j
            break
    print('替换行 %d—%d' % (start + 1, end + 1))

    nl = '\r\n'
    new = [
        "# 独立机构印证：仅限 fed-*（美联储历史站等独立撰写的史学研究），与验证页判据一致",
        "conf_total = sum(1 for e in entries.values() for k in (e.get('key_data', []) or [])",
        "                 if ('双源' in (k.get('note') or '') or '印证' in (k.get('note') or '')",
        "                     or '完全一致' in (k.get('note') or ''))",
        "                 and any(str(x).startswith('fed-') for x in (k.get('sources') or []))",
        "                 and not any(w in (k.get('note') or '') for w in",
        "                             ('两源差异', '存在差异', '数据分歧', '口径不同')))",
        "# 统计口径对照：OWID／世界银行等（与维基数字同源于各国官方统计，独立性有限）",
        "stat_total = sum(1 for e in entries.values() for k in (e.get('key_data', []) or [])",
        "                 if ('双源' in (k.get('note') or '') or '印证' in (k.get('note') or '')",
        "                     or '完全一致' in (k.get('note') or ''))",
        "                 and any(str(x).startswith(('owid-', 'org-')) for x in (k.get('sources') or []))",
        "                 and not any(str(x).startswith('fed-') for x in (k.get('sources') or []))",
        "                 and not any(w in (k.get('note') or '') for w in",
        "                             ('两源差异', '存在差异', '数据分歧', '口径不同')))",
    ]
    lines[start:end + 1] = [x + nl for x in new]
    with open(P, 'w', encoding='utf-8', newline='') as f:
        f.writelines(lines)
    print('已替换为 %d 行' % len(new))
