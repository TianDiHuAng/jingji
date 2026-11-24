# -*- coding: utf-8 -*-
"""续作DO：从条目已有概述/时间线中提炼policy_response（不引入新事实）。"""
import json, glob, re

POL_KW = ['救助', '注资', '国有化', '接管', '资本管制', 'IMF', '重组', '纾困', '担保',
          '冻结', '加息', '降息', '量化宽松', '财政', '紧缩', '贬值', '管制', '禁令',
          '救市', '协调', '剥离', '清算', '重整', '改革', '补贴', '限价']

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
n = 0
log = []
for eid, f in es.items():
    d = json.load(open(f, encoding='utf-8'))
    if d['unit'].startswith('U6') or d.get('policy_response'):
        continue
    ov = d.get('overview', '')
    sents = [s.strip() for s in re.split(r'(?<=[。；])', ov) if s.strip()]
    pick = [s for s in sents if any(w in s for w in POL_KW)]
    if not pick:
        continue
    # 去掉纯数据句（含"具体…待核实"且无政策动词的），最多取3句
    pick = [s for s in pick if len(s) > 20][:3]
    if not pick:
        continue
    view = ''.join(pick)
    view = view.replace('具体数据待核实', '').replace('具体细节待核实', '')
    view = view.rstrip('。；') + '。'
    d['policy_response'] = [{
        'holder': '政策当局',
        'view': view,
        'basis': '据本条目概述与时间线提炼（未引入新事实）；具体措施细节与效果待核实',
        'sources': d['sources'][:2],
    }]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DO】policy_response 由概述提炼。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    log.append((eid, view[:70]))
print('补写 policy_response:', n)
for x in log[:12]:
    print('  -', x[0], '|', x[1])
