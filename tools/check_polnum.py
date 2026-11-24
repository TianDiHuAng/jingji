# -*- coding: utf-8 -*-
"""续作FU：改进数值核对——支持中文"亿/万"单位换算与英文月份。

用法：python -X utf8 tools/check_polnum.py
退出码：0 全部可解释；1 存在可疑数字
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, '_research', 'wiki_full')

MONTHS = {'1': 'january', '2': 'february', '3': 'march', '4': 'april', '5': 'may', '6': 'june',
          '7': 'july', '8': 'august', '9': 'september', '10': 'october', '11': 'november',
          '12': 'december'}


def variants(num_str, next_ctx):
    """生成可能的原文写法。

    中文按"亿/万"表述时，原文通常是 X billion / X million。
    next_ctx 是数字后面的中文片段，用于判断单位。
    """
    out = set()
    s = num_str.replace(',', '')
    try:
        f = float(s)
    except ValueError:
        return out
    # 直接写法
    out.add(num_str)
    out.add(s)
    if f == int(f):
        out.add(str(int(f)))
        out.add('{:,}'.format(int(f)))
    else:
        out.add('%.1f' % f)
        out.add('%.2f' % f)
    # 中文单位换算
    if '亿' in next_ctx:
        out.add(('%g' % (f / 10)).rstrip('0').rstrip('.'))   # 亿 → billion（/10）
        out.add(('%g' % (f * 100)).rstrip('0').rstrip('.'))  # 亿 → million（×100）
    if '万' in next_ctx:
        out.add(('%g' % (f / 10000)).rstrip('0').rstrip('.'))  # 万 → billion
        out.add(('%g' % (f / 100)).rstrip('0').rstrip('.'))    # 万 → million
        out.add(('%g' % (f / 10)).rstrip('0').rstrip('.'))     # 万 → 十万
    # 月份：中文"3月" ↔ 原文 March
    m = re.match(r'^\s*月', next_ctx or '')
    if m and not num_str.replace('.', '').isdigit() is False:
        mn = MONTHS.get(num_str)
        if mn:
            out.add(mn)
            out.add(mn.capitalize())
    return out



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

def main():
    entries = [json.load(open(f, encoding='utf-8'))
               for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))]
    NUM = re.compile(r'(\d[\d,]*\.?\d*)')
    checked = 0
    missing = 0
    weak = 0
    suspect = []
    for e in entries:
        pr = e.get('policy_response') or []
        if not pr:
            continue
        p = os.path.join(FULL, e['id'] + '.txt')
        if not os.path.exists(p):
            continue
        txt = open(p, encoding='utf-8').read().lower()
        # 条目自身正文也并入查找范围：部分数字出自 overview/comparison 而非维基全文
        own = ' '.join([e.get('overview') or '', e.get('comparison') or '', e.get('one_line') or ''])
        txt += ' ' + own.lower()

        for r in pr:
            view = r.get('view', '')
            for m in NUM.finditer(view):
                num = m.group(1)
                after = view[m.end():m.end() + 4]
                checked += 1
                cands = variants(num, after)
                hints = _hints(after)
                found = False
                strong = False
                for c in cands:
                    if not c:
                        continue
                    start = 0
                    while True:
                        j = txt.find(c, start)
                        if j < 0:
                            break
                        start = j + 1
                        found = True
                        # 排除被更长数字包含（如 8 命中 12.7 的 8）
                        b = txt[j - 1] if j > 0 else ' '
                        a2 = txt[j + len(c)] if j + len(c) < len(txt) else ' '
                        if b.isdigit() or a2.isdigit() or a2 == '.':
                            continue
                        if _ctx_ok(txt, txt, j, len(c), hints):
                            strong = True
                            break
                    if strong:
                        break
                if not found:
                    suspect.append((e['id'], num, after, view[max(0, m.start() - 25):m.end() + 30]))
                    missing += 1
                elif not strong:
                    weak += 1
    print('检查 policy_response 中的数字: %d 个' % checked)
    print('  ★ 强匹配（数字+单位提示）: %d' % (checked - missing - weak))
    print('  ○ 弱匹配（仅数字出现，上下文无单位提示，需人工判断）: %d' % weak)
    print('  × 完全找不到: %d' % missing)
    if suspect:
        print('未能在来源全文中匹配: %d 个' % len(suspect))
        seen = set()
        for eid, num, after, ctx in suspect:
            if (eid, num) in seen:
                continue
            seen.add((eid, num))
            print('  %-26s %-8s 后接"%-4s" | %s' % (eid, num, after, ctx[:60]))
        print('\n结果：需人工判断（多为单位换算或月份写法差异）')
        return 1
    print('\n结果：未发现「完全找不到」的数字；但**弱匹配不视为通过**，仍需人工抽查。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
