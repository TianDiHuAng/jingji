# -*- coding: utf-8 -*-
"""续作FW：核对 overview / comparison / one_line 中提到的数字能否溯源。

与 check_polnum 同一思路：把条目正文的数字与「来源全文 + 条目自身数据」
（key_data、timeline、policy_response）对照，发现可能的抄写错误。

用法：python -X utf8 tools/check_body_num.py
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, '_research', 'wiki_full')
NUM = re.compile(r'(\d[\d,]*\.?\d*)')


def variants(num_str, after):
    out = set()
    s = num_str.replace(',', '')
    try:
        f = float(s)
    except ValueError:
        return out
    out |= {num_str, s}
    if f == int(f):
        out.add(str(int(f)))
        out.add('{:,}'.format(int(f)))
    else:
        out.add('%.1f' % f)
        out.add('%.2f' % f)
    if '亿' in (after or ''):
        out.add(('%g' % (f / 10)).rstrip('0').rstrip('.'))
        out.add(('%g' % (f * 100)).rstrip('0').rstrip('.'))
    if '万' in (after or ''):
        out.add(('%g' % (f / 10000)).rstrip('0').rstrip('.'))
        out.add(('%g' % (f / 100)).rstrip('0').rstrip('.'))
    return out



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

def main():
    entries = [json.load(open(f, encoding='utf-8'))
               for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))]
    checked, no_full = 0, 0
    strong_n, weak_n = 0, 0
    suspect = []
    for e in entries:
        p = os.path.join(FULL, e['id'] + '.txt')
        if not os.path.exists(p):
            no_full += 1
            continue
        txt = open(p, encoding='utf-8').read().lower()
        # 条目自身已核验的数据也作为可比对范围
        own = []
        for k in e.get('key_data', []):
            own.append(str(k['value']))
            if isinstance(k['value'], float) and k['value'] == int(k['value']):
                own.append(str(int(k['value'])))
        for t in e.get('timeline', []):
            own.append(str(t.get('year')))
        own_txt = ' '.join(own).lower()
        for field in ('one_line', 'overview', 'comparison'):
            body = e.get(field) or ''
            for m in NUM.finditer(body):
                num = m.group(1)
                after = body[m.end():m.end() + 4]
                checked += 1
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
                hits = [c for c in cands if c and (c in txt or c in own_txt)]
                if not hits:
                    suspect.append((e['id'], field, num, after,
                                    body[max(0, m.start() - 30):m.end() + 25]))
                else:
                    hints = _hints(after)
                    if any(_strong(txt, c, hints) for c in hits if c in txt):
                        strong_n += 1
                    elif any(c in own_txt for c in hits):
                        strong_n += 1
                    else:
                        weak_n += 1
    print('检查正文数字: %d 个 | 无来源全文的条目: %d' % (checked, no_full))
    print('  ★ 强匹配（数字+单位提示，或与自身已核数据结构一致）: %d' % strong_n)
    print('  ○ 弱匹配（仅数字出现，需人工判断）: %d' % weak_n)
    if suspect:
        print('未匹配: %d 个（去重后如下）' % len(suspect))
        seen = set()
        for eid, field, num, after, ctx in suspect:
            k = (eid, num)
            if k in seen:
                continue
            seen.add(k)
            print('  %-26s %-11s %-8s "%-4s" | %s' % (eid, field, num, after, ctx[:56]))
        print('\n结果：需人工判断')
        return 1
    print('\n结果：正文数字均可溯源')
    return 0


if __name__ == '__main__':
    sys.exit(main())
