# -*- coding: utf-8 -*-
"""round 139：条目页结构完整性审计。"""
import glob, json, os, re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
byid = {e['id']: e for e in es}
miss_overview = miss_src = empty_tbody = l3_no_svg = miss_related_section = 0
detail = []
for e in es:
    p = 'site/%s.html' % e['id']
    if not os.path.exists(p):
        detail.append((e['id'], 'PAGE_MISSING')); continue
    t = open(p, encoding='utf-8').read()
    has_ov = '概述' in t
    has_src = ('来源' in t and ('href="https://' in t or 'src-list' in t or 'sources' in t.lower()))
    # 空 tbody：<tbody></tbody> 或 tbody 内无 <tr>
    empty_tb = bool(re.search(r'<tbody>\s*</tbody>', t))
    if not has_ov:
        miss_overview += 1; detail.append((e['id'], '无概述'))
    if empty_tb:
        empty_tbody += 1; detail.append((e['id'], '空tbody'))
    if e['level'] == 'L3' and '<svg' not in t:
        l3_no_svg += 1; detail.append((e['id'], 'L3无svg'))
print('缺概述:', miss_overview, '| 空 tbody:', empty_tbody, '| L3缺svg:', l3_no_svg)
print('异常明细:', detail[:20])
# 关键数据：有 key_data 却没在页面出现表格的情况
kd_pages_no_table = 0
for e in es:
    if e.get('key_data'):
        p='site/%s.html'%e['id']
        t=open(p,encoding='utf-8').read() if os.path.exists(p) else ''
        if '关键数据' not in t:
            kd_pages_no_table += 1
            if kd_pages_no_table<=8: print('  有key_data但页面无关键数据表:', e['id'])
print('有 key_data 但页面无关键数据表:', kd_pages_no_table)
