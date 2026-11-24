# -*- coding: utf-8 -*-
"""续作JD：check_polnum 改用与 check_kd 一致的两级判据，并声明局限。

round 101 抽查发现：check_polnum 原判据（"数字出现在来源全文即通过"）存在高比例假匹配，
例如"8月1日"命中原文 "7 August 2018" 的 8、"6%"命中 "6.9%" 的 6。
"""
P = 'tools/check_polnum.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

# 1) 在 variants 后加入上下文校验
helper = '''

def _ctx_ok(txt, txt_raw, idx, length, hints):
    """数字附近须出现单位提示词，才视为强匹配。"""
    win = txt[max(0, idx - 60):idx + length + 60]
    raw = txt_raw[max(0, idx - 60):idx + length + 60]
    if not hints:
        return False
    return any(h.lower() in win for h in hints)


UNIT_HINT = {
    '%': ['%', 'percent', 'per cent'],
    '亿': ['billion', 'million', '亿'],
    '万': ['million', 'thousand', '万'],
    '年': ['year', '年'],
    '月': ['month', '月'],
    '日': ['day', '日', 'december', 'november', 'october', 'january', 'august', 'july', 'june'],
    '点': ['points', 'point'],
    '倍': ['times', 'fold'],
}


def _hints(after):
    out = []
    a = str(after or '')
    for k, vs in UNIT_HINT.items():
        if k in a:
            out.extend(vs)
    return list(dict.fromkeys(out))
'''

if '_ctx_ok' not in s:
    anchor = "\ndef main():"
    s = s.replace(anchor, helper + anchor, 1)
    print('1) 已插入上下文校验辅助函数')

# 2) 主循环改为两级统计
old_loop = """                checked += 1
                cands = variants(num, after)
                if not any(c and c in txt for c in cands):
                    suspect.append((e['id'], num, after, view[max(0, m.start() - 25):m.end() + 30]))"""
new_loop = """                checked += 1
                cands = variants(num, after)
                hit_idx = None
                for c in cands:
                    if c and c in txt:
                        hit_idx = txt.find(c)
                        break
                if hit_idx is None:
                    suspect.append((e['id'], num, after, view[max(0, m.start() - 25):m.end() + 30]))
                    missing += 1
                elif not _ctx_ok(txt, txt, hit_idx, len(num), _hints(after)):
                    weak += 1"""
if old_loop in s:
    s = s.replace(old_loop, new_loop, 1)
    print('2) 主循环已改为两级')

# 3) 初始化计数
s = s.replace("    checked = 0\n", "    checked = 0\n    missing = 0\n    weak = 0\n", 1)

# 4) 输出改为两级
old_out = """    print('检查 policy_response 中的数字: %d 个' % checked)"""
new_out = """    print('检查 policy_response 中的数字: %d 个' % checked)
    print('  ★ 强匹配（数字+单位提示）: %d' % (checked - missing - weak))
    print('  ○ 弱匹配（仅数字出现，上下文无单位提示，需人工判断）: %d' % weak)
    print('  × 完全找不到: %d' % missing)"""
if old_out in s:
    s = s.replace(old_out, new_out, 1)
    print('3) 输出已改为两级')

# 5) 结论说明
s = s.replace("    print('\\n结果：全部数字均可在来源全文中找到（含亿/万换算与月份换算）')",
              "    print('\\n结果：未发现「完全找不到」的数字；但**弱匹配不视为通过**，仍需人工抽查。')")

with open(P, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print('写入完成')
