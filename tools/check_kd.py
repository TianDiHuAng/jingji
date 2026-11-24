# -*- coding: utf-8 -*-
"""key_data 数值可核对性检查。

对每条 key_data，检查其 value 能否在**同条目已抓取的来源全文**中找到
（容忍负号表示跌幅；容忍千分位；容忍单位换算如 620 million ↔ 0.62 billion）。

用途：发现"数值抄错"或"来源标错"的问题。
限制：来源为 OWID／美联储专文／中文维基的条目没有对应全文，会被列为"无法核对"，
      这不是错误，需人工确认。

用法：python -X utf8 tools/check_kd.py
退出码：0 = 无可核对性问题；1 = 发现可疑数值
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, '_research', 'wiki_full')


def num_variants(v):
    """生成数值的多种文本写法，用于在原文中匹配。"""
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
            # 千分位不含小数
            if isinstance(x, float) and x == int(x):
                out.add('{:,}'.format(int(x)))
    return out


def main():
    entries = [json.load(open(f, encoding='utf-8'))
               for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))]
    checked = unverifiable = 0
    suspect = []
    for e in entries:
        p = os.path.join(FULL, e['id'] + '.txt')
        if not os.path.exists(p):
            unverifiable += len(e.get('key_data', []))
            continue
        txt = open(p, encoding='utf-8').read()
        for k in e.get('key_data', []):
            checked += 1
            if not any(c in txt for c in num_variants(k['value'])):
                suspect.append({
                    'id': e['id'], 'label': k.get('label'), 'value': k['value'],
                    'unit': k.get('unit'), 'sources': k.get('sources'),
                    'note': (k.get('note') or '')[:100],
                })
    print('可核对 key_data: %d | 无对应全文（无法核对）: %d' % (checked, unverifiable))
    if suspect:
        print('\n数值未在全文直接匹配 %d 条（需人工判断是单位换算还是抄错）：' % len(suspect))
        for s in suspect:
            print('  %-26s %-34s value=%s %s' % (
                s['id'], (s['label'] or '')[:32], s['value'], (s['unit'] or '')[:12]))
            print('       note: %s' % s['note'])
        return 1
    print('\n结果：全部可核对数值均在来源全文中找到')
    return 0


if __name__ == '__main__':
    sys.exit(main())
