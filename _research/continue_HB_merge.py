# -*- coding: utf-8 -*-
"""续作HB：合并重复条目 glass-steagall 与 glass-steagall-1933。

判断依据：两者讲的是同一部 1933 年美国《银行法》（格拉斯-斯蒂格尔条款），
仅 unit 归类不同（U3 20世纪上半 vs U6 理论与制度）。
保留 glass-steagall-1933（key_data 1／timeline 3／schools 2／policy 1，内容更完整），
把 glass-steagall 的引用重定向后删除。
"""
import glob
import json
import os

KEEP, DROP = 'glass-steagall-1933', 'glass-steagall'

k = json.load(open('data/entries/%s.json' % KEEP, encoding='utf-8'))
dr = json.load(open('data/entries/%s.json' % DROP, encoding='utf-8'))

# 1) 合并独有来源
for s in dr.get('sources', []):
    if s not in k['sources']:
        k['sources'].append(s)
        print('并入来源:', s)

# 2) 合并 schools 中独有观点
have = {(s.get('holder'), s.get('view')) for s in k.get('schools', [])}
for s in dr.get('schools', []):
    if (s.get('holder'), s.get('view')) not in have:
        k.setdefault('schools', []).append(s)
        print('并入学派观点:', s.get('holder'))

# 3) 合并 related
for r in dr.get('related', []):
    if r != DROP and r not in k.get('related', []):
        k.setdefault('related', []).append(r)

# 4) 在 overview 注明合并
k['overview'] = (k['overview'].rstrip()
                 + '（本条目合并了原 U6「格拉斯-斯蒂格尔法案(1933)」条目，'
                   '后者与本条指同一法案，已去重。）')
k['pending_notes'] = (k.get('pending_notes', '')
                      + ' 【续作HB】并入重复条目 glass-steagall（同一法案，原分列于 U3 与 U6）。')
json.dump(k, open('data/entries/%s.json' % KEEP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('保留条目已更新:', KEEP)

# 5) 全站重定向引用
cnt_rel, cnt_cmp = 0, 0
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    changed = False
    rel = d.get('related', [])
    if DROP in rel:
        d['related'] = sorted({KEEP if r == DROP else r for r in rel} - {DROP})
        cnt_rel += 1
        changed = True
    c = d.get('comparison') or ''
    if DROP in c:
        d['comparison'] = c.replace(DROP, KEEP)
        cnt_cmp += 1
        changed = True
    if changed:
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('重定向 related 引用: %d 个条目 | comparison 引用: %d 个条目' % (cnt_rel, cnt_cmp))

# 6) 删除旧条目
os.remove('data/entries/%s.json' % DROP)
print('已删除:', DROP)

# 7) 更新 coverage.json
cp = 'coverage.json'
cov = json.load(open(cp, encoding='utf-8'))
before = len(cov['entries'])
cov['entries'] = [e for e in cov['entries'] if e['id'] != DROP]
cov['total'] = len(cov['entries'])
json.dump(cov, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage.json: %d → %d' % (before, cov['total']))
