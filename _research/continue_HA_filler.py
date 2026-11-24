# -*- coding: utf-8 -*-
"""续作HA：①调整 check_filler 的重复句检测（排除括号内元信息说明）；②清理 4 条空洞 comparison。"""
import glob
import json
import re

# ---- 1) 修正检测工具：括号内说明不算模板句 ----
p = 'tools/check_filler.py'
s = open(p, encoding='utf-8').read()
old = """            for s in re.split(r'[。；！？]', v):
                s = s.strip()
                if 15 <= len(s) <= 200 and s not in seen:"""
new = """            # 去掉括号内的元信息说明（如"（理论概念条目，标准教科书定义…）"），
            # 这类说明标注条目性质，重复出现属正常，不算模板套话
            _v = re.sub(r'（[^）]*）', '', v)
            for s in re.split(r'[。；！？]', _v):
                s = s.strip()
                if 15 <= len(s) <= 200 and s not in seen:"""
if old in s and '去掉括号内的元信息说明' not in s:
    s = s.replace(old, new, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('检测工具已排除括号内说明')

# ---- 2) 清理 4 条空洞 comparison ----
DROP = ['arendal-crash-1886', 'henan-2022', 'myanmar-2003', 'venezuelan-banking-1994']
for eid in DROP:
    fp = 'data/entries/%s.json' % eid
    d = json.load(open(fp, encoding='utf-8'))
    c = (d.get('comparison') or '').strip()
    if c and len(c) < 40:
        d.pop('comparison')
        d['pending_notes'] = (d.get('pending_notes', '')
                              + ' 【续作HA】移除空洞 comparison（原文「%s」仅复述危机类型，'
                                '未给出具体对照对象与分析）。' % c[:30])
        json.dump(d, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('删除空洞 comparison: %-24s %s' % (eid, c[:36]))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
print('\ncomparison 覆盖: %d/%d = %d%%'
      % (sum(1 for e in es if e.get('comparison')), len(es),
         sum(1 for e in es if e.get('comparison')) * 100 // len(es)))
