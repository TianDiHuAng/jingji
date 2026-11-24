# -*- coding: utf-8 -*-
"""续作JB：把 check_kd 改为两级报告，并说明判据局限。

背景（round 100）：发现原判据会假匹配（"5" 命中 "50 cents"）；
但改用"数字+单位"严格判据后又产生假阴性——原文可能用
英文数字（eight-day／twelve Key Attributes）、文字表述（more than half）、
或不同单位（400 million livres vs 0.4 百万里弗）。

结论：**任何纯字符串匹配都无法同时避免假阳性与假阴性**。
故改为两级报告，对外只用"强匹配"作为可核对依据，"弱匹配"列为需人工判断。
"""
import glob
import json
import os

FULL = '_research/wiki_full'
UNIT_PAT = {
    '%': ['%', 'percent', 'per cent', 'percentage'],
    '倍': ['times', 'fold'],
    '万亿美元': ['trillion'], '十亿美元': ['billion'], '亿美元': ['billion'],
    '百万美元': ['million'], '百万英镑': ['million'], '百万': ['million'], '十亿': ['billion'],
    '人': ['people', 'persons', 'inhabitants'],
    '年': ['year'], '个月': ['month'], '天': ['day'], '点': ['points', 'point'],
}
EN_NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
          'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'fifteen': 15,
          'twenty': 20, 'thirty': 30, 'fifty': 50, 'hundred': 100}


def unit_hints(u):
    u = str(u or '')
    out = []
    for k, vs in UNIT_PAT.items():
        if k in u:
            out.extend(vs)
    return list(dict.fromkeys(out))


def label_kws(label):
    import re
    zh = re.findall(r'[\u4e00-\u9fff]{2,}', str(label or ''))
    en = [w for w in str(label or '').split() if len(w) >= 4 and w.isascii()]
    return zh[:4], [w.lower() for w in en[:3]]


def variants(v):
    out = set()
    vals = [v, abs(v)] if isinstance(v, (int, float)) and v < 0 else [v]
    for x in vals:
        if isinstance(x, float) and x == int(x):
            x = int(x)
        s = str(x)
        out.add(s)
        out.add(s.replace('.0', ''))
        if isinstance(x, (int, float)):
            out.add('{:,}'.format(x))
            if isinstance(x, float) and x == int(x):
                out.add('{:,}'.format(int(x)))
    return out


def check(k, txt):
    """返回 ('strong'|'weak'|None, 说明)"""
    low = txt.lower()
    hints = unit_hints(k.get('unit'))
    zh, en = label_kws(k.get('label'))
    weak_hit = False
    for c in variants(k['value']):
        start = 0
        while True:
            i = txt.find(c, start)
            if i < 0:
                break
            start = i + 1
            before = txt[i - 1] if i > 0 else ' '
            after = txt[i + len(c)] if i + len(c) < len(txt) else ' '
            if before.isdigit() or after.isdigit() or after == '.':
                continue
            win = low[max(0, i - 60):i + len(c) + 60]
            if hints and any(h.lower() in win for h in hints):
                return 'strong', 'unit'
            if any(w in txt[max(0, i - 60):i + len(c) + 60] for w in zh) or any(w in win for w in en):
                return 'strong', 'keyword'
            weak_hit = True
    # 英文数字拼写
    if isinstance(k['value'], (int, float)) and float(k['value']).is_integer():
        for w, n in EN_NUM.items():
            if n == int(k['value']) and w in low:
                return 'strong', 'en_num'
    return ('weak', 'num_only') if weak_hit else (None, None)


def main():
    es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
    strong = weak = none = 0
    weak_list = []
    for e in es:
        p = os.path.join(FULL, e['id'] + '.txt')
        if not os.path.exists(p):
            continue
        txt = open(p, encoding='utf-8').read()
        for k in (e.get('key_data') or []):
            r, why = check(k, txt)
            if r == 'strong':
                strong += 1
            elif r == 'weak':
                weak += 1
                weak_list.append((e['id'], k['label'][:28], k['value']))
            else:
                none += 1
    total = strong + weak + none
    print('可核对 key_data: %d' % total)
    print('  ★ 强匹配（数字+单位/关键词/英文数字）: %d (%.0f%%)' % (strong, strong * 100 / total))
    print('  ○ 弱匹配（仅数字出现，需人工判断）: %d (%.0f%%)' % (weak, weak * 100 / total))
    print('  × 未匹配: %d' % none)
    print('\n弱匹配示例（前 10）:')
    for w in weak_list[:10]:
        print('  %-26s %-28s v=%s' % w)


if __name__ == '__main__':
    main()
