# -*- coding: utf-8 -*-
"""key_data 数值可核对性检查（两级判据）。

★ 强匹配：数字 + 单位提示词 / label 关键词 / 英文数字拼写 紧邻出现 → 高置信可核对
○ 弱匹配：仅数字出现，无上下文佐证 → 需人工判断
× 未匹配：全文找不到该数字

**判据局限（务必知悉）**：
纯字符串匹配无法同时避免假阳性与假阴性——
  · 假阳性例：value=5 命中原文 "50 cents" 的 "5"；
  · 假阴性例：原文用英文数字（eight-day）或文字表述（more than half），
    或单位不同（400 million livres vs 0.4 百万里弗）。
故本工具**只把强匹配作为可核对依据**，弱匹配列为需人工判断，不宣称"全部核对通过"。

用法：python -X utf8 tools/check_kd.py
退出码：0 = 无强判据冲突；1 = 存在需关注项
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, '_research', 'wiki_full')

UNIT_PAT = {
    '%': ['%', 'percent', 'per cent', 'percentage'],
    '百分点': ['percentage point', 'points', 'pp'],
    '倍': ['times', 'fold', '-fold'],
    '万亿美元': ['trillion'], '十亿美元': ['billion'], '亿美元': ['billion'],
    '百万美元': ['million'], '百万英镑': ['million'], '百万': ['million'],
    '十亿': ['billion'], '亿': ['billion', 'million'], '万': ['million', 'thousand'],
    '人': ['people', 'persons', 'inhabitants', 'population'],
    '年': ['year', 'years'], '个月': ['month', 'months'],
    '天': ['day', 'days'], '点': ['points', 'point'],
}
EN_NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
          'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'fifteen': 15,
          'twenty': 20, 'thirty': 30, 'fifty': 50}


def unit_hints(u):
    u = str(u or '')
    out = []
    for k, vs in UNIT_PAT.items():
        if k in u:
            out.extend(vs)
    return list(dict.fromkeys(out))


def label_kws(label):
    zh = re.findall(r'[\u4e00-\u9fff]{2,}', str(label or ''))
    en = [w.lower() for w in str(label or '').split() if len(w) >= 4 and w.isascii()]
    return zh[:4], en[:3]


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


def derived_by_unit(value, unit):
    """按中文单位推导等值数字，匹配来源中以 billion/million/thousand 表述的同一数值。
    例：750（亿）→ 75（billion）；12（亿）→ 1.2（billion）、1200（million）；
        1200（万）→ 12（million）、12000（thousand）。"""
    out = set()
    if not isinstance(value, (int, float)):
        return out
    u = str(unit or '')
    if '万亿' in u:
        return out
    if '亿' in u:
        out |= variants(value / 10.0)     # billion
        out |= variants(value * 100.0)    # million
    elif '万' in u:
        out |= variants(value / 100.0)    # million
        out |= variants(value * 10.0)     # thousand
    return out


def classify(k, txt):
    low = txt.lower()
    hints = unit_hints(k.get('unit'))
    zh, en = label_kws(k.get('label'))
    weak = False
    cands = set(variants(k['value'])) | derived_by_unit(k['value'], k.get('unit'))
    for c in cands:
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
            raw = txt[max(0, i - 60):i + len(c) + 60]
            if hints and any(h.lower() in win for h in hints):
                return 'strong'
            if any(w in raw for w in zh) or any(w in win for w in en):
                return 'strong'
            weak = True
    if isinstance(k['value'], (int, float)) and float(k['value']).is_integer():
        for w, n in EN_NUM.items():
            if n == int(k['value']) and w in low:
                return 'strong'
    return 'weak' if weak else None


def main():
    entries = [json.load(open(f, encoding='utf-8'))
               for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))]
    strong = weak = none = nofull = 0
    weak_items = []
    for e in entries:
        p = os.path.join(FULL, e['id'] + '.txt')
        if not os.path.exists(p):
            nofull += len(e.get('key_data') or [])
            continue
        txt = open(p, encoding='utf-8').read()
        for k in (e.get('key_data') or []):
            r = classify(k, txt)
            if r == 'strong':
                strong += 1
            elif r == 'weak':
                weak += 1
                weak_items.append((e['id'], k.get('label', '')[:28], k['value']))
            else:
                none += 1
    total = strong + weak + none
    print('可核对 key_data: %d（另有 %d 条无来源全文）' % (total, nofull))
    if total:
        print('  ★ 强匹配（数字+单位/关键词/英文数字）: %d (%.0f%%)' % (strong, strong * 100 / total))
        print('  ○ 弱匹配（仅数字出现，需人工判断）: %d (%.0f%%)' % (weak, weak * 100 / total))
        print('  × 未匹配: %d' % none)
    if weak_items:
        print('\n弱匹配示例（前 8，需人工判断）:')
        for w in weak_items[:8]:
            print('  %-26s %-28s v=%s' % w)
    print('\n说明：本工具只把强匹配作为可核对依据；弱匹配不视为通过。')
    return 0 if none == 0 and weak == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
