# -*- coding: utf-8 -*-
"""续作JA：修复 check_kd 的假匹配——数字出现 ≠ 数据可核对。

发现（round 100）：
抽查 6 条被判"匹配成功"的数据，3 条是假匹配：
  · "3元券实际储备支撑 = 5" → 匹配到全文中的 "50 cents" 的 "5"
  · "金融部门占机构贷款比重 = 3" → 匹配到 "$3 billion" 的 "3"
  · "亚历山大城人口降幅 = -62" → 匹配到 "249 to 262" 的 "62"

根因：原判据只检查数字字符串是否出现，不与单位/上下文绑定。

改进：要求匹配**带单位或紧邻百分号**的表达；若无单位可用，则要求数字前后 40 字符内
出现该数据项 label 中的关键词。
"""
import glob
import json
import os

ROOT = '.'
FULL = '_research/wiki_full'

UNIT_PAT = {
    '%': ['%', 'percent', 'per cent', 'percentage'],
    '百分点': ['percentage point', 'points', 'pp'],
    '倍': ['times', 'fold', '-fold'],
    '万亿美元': ['trillion'],
    '十亿美元': ['billion'],
    '亿美元': ['billion'],
    '百万美元': ['million'],
    '百万英镑': ['million'],
    '百万': ['million'],
    '十亿': ['billion'],
    '亿美元': ['billion'],
    '人': ['people', 'persons', 'inhabitants', 'population'],
    '年': ['year', 'years'],
    '个月': ['month', 'months'],
    '天': ['day', 'days'],
    '点': ['points', 'point'],
}


def unit_hints(unit):
    u = str(unit or '')
    out = []
    for k, vs in UNIT_PAT.items():
        if k in u:
            out.extend(vs)
    # 提取 % 之类直接符号
    for sym in ('%', '％'):
        if sym in u:
            out.append('%')
    return list(dict.fromkeys(out))


def label_keywords(label):
    import re
    zh = re.findall(r'[\u4e00-\u9fff]{2,}', str(label or ''))
    return [w for w in zh if len(w) >= 2][:4]


def num_variants(v):
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


def verified_match(k, txt, txt_lower):
    """严格判据：数字附近须有单位或 label 关键词。"""
    hints = unit_hints(k.get('unit'))
    kws = label_keywords(k.get('label'))
    eng_kw = [w for w in str(k.get('label') or '').split() if len(w) >= 4 and w.isascii()][:3]
    for c in num_variants(k['value']):
        start = 0
        while True:
            i = txt.find(c, start)
            if i < 0:
                break
            start = i + 1
            # 排除被更长数字包含的情况（如 "5" 命中 "50"、"3" 命中 "300"）
            before = txt[i - 1] if i > 0 else ' '
            after = txt[i + len(c)] if i + len(c) < len(txt) else ' '
            if before.isdigit() or (after.isdigit()) or after == '.':
                continue
            win = txt_lower[max(0, i - 60):i + len(c) + 60]
            if hints and any(h.lower() in win for h in hints):
                return True, c, 'unit'
            if any(w in win for w in kws) or any(w.lower() in win for w in eng_kw):
                return True, c, 'keyword'
    return False, None, None


def main():
    es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
    checked = strong = weak = 0
    fails = []
    for e in es:
        p = os.path.join(FULL, e['id'] + '.txt')
        if not os.path.exists(p):
            continue
        txt = open(p, encoding='utf-8').read()
        low = txt.lower()
        for k in (e.get('key_data') or []):
            checked += 1
            ok, c, how = verified_match(k, txt, low)
            if ok:
                strong += 1
            else:
                weak += 1
                fails.append((e['id'], k['label'][:30], k['value'], k.get('unit', '')[:12]))
    print('可核对 key_data: %d' % checked)
    print('严格判据通过: %d' % strong)
    print('未通过: %d' % weak)
    print('\n未通过示例（前 12）:')
    for f in fails[:12]:
        print('  %-26s %-30s v=%s %s' % f)


if __name__ == '__main__':
    main()
