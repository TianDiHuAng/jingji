# -*- coding: utf-8 -*-
"""round 129g：核心/重要案例缺 key_data 的清单。"""
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
noK = [e for e in cases if not e.get('key_data')]
noT = [e for e in cases if not e.get('timeline')]
print('案例总数:', len(cases))
print('缺 key_data:', len(noK), '| 缺 timeline:', len(noT))
print('\n缺 key_data 的核心/重要案例:')
for e in sorted([x for x in noK if x['tier'] in ('核心', '重要')], key=lambda x: x['id']):
    print('  %-30s %-4s %s' % (e['id'], e['tier'], e['title'][:22]))
print('\n缺 key_data 的补充案例:', len([x for x in noK if x['tier'] == '补充']))
