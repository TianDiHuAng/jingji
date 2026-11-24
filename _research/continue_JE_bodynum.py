# -*- coding: utf-8 -*-
"""续作JE：给 check_body_num 加两级判据统计，与 check_kd／check_polnum 保持一致。

原实现只报告"未匹配"，不区分"强匹配（上下文有单位/关键词）"与"弱匹配（仅数字出现）"。
补上分级后，三个数字检查工具的口径统一：**弱匹配一律不视为通过**。
"""
P = 'tools/check_body_num.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

helper = '''

UNIT_HINT = {
    '%': ['%', 'percent', 'per cent'],
    '亿': ['billion', 'million', '亿'],
    '万': ['million', 'thousand', '万'],
    '年': ['year', '年'],
    '月': ['month', '月'],
    '日': ['day', '日'],
    '点': ['points', 'point', '点'],
    '倍': ['times', 'fold', '倍'],
    '家': ['banks', 'banks', '家', 'bank'],
    '人': ['people', 'persons', 'population', '人'],
}


def _hints(after):
    out = []
    for k, vs in UNIT_HINT.items():
        if k in str(after or ''):
            out.extend(vs)
    return list(dict.fromkeys(out))


def _strong(txt, c, hints):
    """遍历 c 的所有出现位置，任一位置 60 字内有单位提示即判强。"""
    start = 0
    while True:
        j = txt.find(c, start)
        if j < 0:
            return False
        start = j + 1
        b = txt[j - 1] if j > 0 else ' '
        a = txt[j + len(c)] if j + len(c) < len(txt) else ' '
        if b.isdigit() or a.isdigit() or a == '.':
            continue
        win = txt[max(0, j - 60):j + len(c) + 60]
        if hints and any(h.lower() in win for h in hints):
            return True
'''

if '_strong(' not in s:
    anchor = "\ndef main():"
    s = s.replace(anchor, helper + anchor, 1)
    print('1) 已插入分级辅助函数')

s = s.replace("    checked, no_full = 0, 0\n    suspect = []",
              "    checked, no_full = 0, 0\n    strong_n = 0\n    weak_n = 0\n    suspect = []", 1)

old = """                cands = variants(num, after)
                if not any(c and (c in txt or c in own_txt) for c in cands):
                    suspect.append((e['id'], field, num, after,
                                    body[max(0, m.start() - 30):m.end() + 25]))"""
new = """                cands = variants(num, after)
                hits = [c for c in cands if c and (c in txt or c in own_txt)]
                if not hits:
                    suspect.append((e['id'], field, num, after,
                                    body[max(0, m.start() - 30):m.end() + 25]))
                else:
                    hints = _hints(after)
                    if any(_strong(txt, c, hints) for c in hits if c in txt):
                        strong_n += 1
                    elif any(c in own_txt for c in hits):
                        strong_n += 1      # 与自身已核数据结构一致，视为可接受
                    else:
                        weak_n += 1"""
if old in s:
    s = s.replace(old, new, 1)
    print('2) 主循环已改为分级')
else:
    print('2) 主循环未匹配，需手工处理')

old_out = "    print('检查正文数字: %d 个 | 无来源全文的条目: %d' % (checked, no_full))"
new_out = """    print('检查正文数字: %d 个 | 无来源全文的条目: %d' % (checked, no_full))
    print('  ★ 强匹配（数字+单位提示，或与自身已核数据结构一致）: %d' % strong_n)
    print('  ○ 弱匹配（仅数字出现，需人工判断）: %d' % weak_n)"""
if old_out in s:
    s = s.replace(old_out, new_out, 1)
    print('3) 输出已加分级')

with open(P, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print('写入完成')
