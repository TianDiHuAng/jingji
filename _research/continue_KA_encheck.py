# -*- coding: utf-8 -*-
import glob
import json
import re


def en_ratio(s):
    if not s:
        return 0.0
    zh = len(re.findall(r'[\u4e00-\u9fff]', s))
    en = len(re.findall(r'[A-Za-z]', s))
    return en / (zh + en) if (zh + en) else 0.0


es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
bad = [(e['id'], en_ratio(e.get('overview') or ''), len(e.get('overview') or '')) for e in es]
bad = [b for b in bad if b[1] > 0.45]
bad.sort(key=lambda x: -x[1])
print('overview 英文占比 >45%% 的条目: %d' % len(bad))
for b in bad[:20]:
    print('  %-32s 英文占比 %.0f%% | %d 字' % (b[0], b[1] * 100, b[2]))
print()
# 其他字段
for fld in ('one_line', 'comparison'):
    bad2 = [(e['id'], en_ratio(e.get(fld) or '')) for e in es if en_ratio(e.get(fld) or '') > 0.45]
    print('%s 英文占比 >45%%: %d' % (fld, len(bad2)))
    for b in sorted(bad2, key=lambda x: -x[1])[:6]:
        print('   %-30s %.0f%%' % (b[0], b[1] * 100))
