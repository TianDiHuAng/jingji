# -*- coding: utf-8 -*-
"""续作FS：为4个案例补充 key_data。"""
import json
import os
import glob

KD = {
 'brexit-crash-2016': [
   ('脱欧公投赞成票占比', 51.9, '%', 2016,
    '原文：The electorate voted to leave the EU by a slight margin, with a 51.9% share of the vote'),],
 'federal-reserve-act': [
   ('改革前全国硬币与纸币总额', 3.8, '十亿美元', 1913,
    '原文：the roughly $3.8 billion in coins and banknotes did not provide an adequate money supply'),
   ('会员银行在联邦储备银行享有的年度股息率', 6, '%', 1913,
    '原文：a 6% annual dividend in their Federal Reserve'),],
 'medici-bank': [
   ('英王欠美第奇银行的款项（14世纪）', 10500, '英镑', 1400,
    '原文：the English king owed 10,500 pounds sterling (equivalent to £10.5 million in 2025)'),],
 'national-banking-act': [
   ('1862年法定货币法授权发行额', 150, '百万美元', 1862,
    '原文：Congress approved the Legal Tender Act of 1862, allowing the issue of $150 million'),
   ('第二次法定货币法后的发行额', 450, '百万美元', 1862,
    '原文：The Second Legal Tender Act, enacted July 11, 1862'),],
}

n_entry, n_kd = 0, 0
for eid, items in KD.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('key_data'):
        print('已有', eid); continue
    sid = next((s for s in d['sources'] if s.startswith('w-en')), d['sources'][0])
    d['key_data'] = [{
        'label': label, 'value': value, 'unit': unit, 'year': year,
        'comparable_price': False,
        'note': note + '；单一来源待核实。', 'sources': [sid],
    } for label, value, unit, year, note in items]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FS】补充 key_data。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n_entry += 1
    n_kd += len(d['key_data'])
    print('补数据', eid, len(d['key_data']), '条')

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)
print('\n本轮 %d 条目 / %d 条 | 案例有数据 %d/%d = %d%% | 全站 %d 条'
      % (n_entry, n_kd, wk, len(cases), wk * 100 // len(cases), tk))
