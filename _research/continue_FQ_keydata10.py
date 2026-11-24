# -*- coding: utf-8 -*-
"""续作FQ：为10个案例补充 key_data（取自维基原文）。"""
import json
import os
import glob

KD = {
 'banking-act-1935': [
   ('存款在5000美元保险限额以下的占比', 98.5, '%', 1935,
    '原文：At this time 98.5% of all deposits were under the $5,000 limit'),],
 'cameroon-crisis-1987': [
   ('1987—88年预算削减幅度', 18, '%', 1988,
    '原文：The 1987–1988 budget reduced government spending by 18%'),
   ('IMF 援助规模', 150, '百万美元', 1988,
    '原文：Cameroon agreed to an IMF aid package worth $150 million'),],
 'ghana-banking-2017': [
   ('Capital Bank 与 UT Bank 无法回收债务', 11, '十亿塞地', 2017,
    '原文：noncollectable debts of GH₵11 billion owed to Capital Bank and UT Bank'),
   ('对 Capital Bank 的流动性支持', 0.62, '十亿塞地', 2017,
    '原文：The liquidity support of GH₵620 million, that was issued by the central bank of Ghana'),],
 'myanmar-2003': [
   ('私营银行占储蓄比重（1994年）', 10, '%', 1994,
    '原文：private banks accounted for only about 10% of savings in 1994'),
   ('私营银行占储蓄比重（2003年）', 66, '%', 2003,
    '原文：by 2003, the amount increased to about 66%'),],
 'overend-gurney': [
   ('倒闭时欠债（1866年）', 11, '百万英镑', 1866,
    '原文：collapsed in 1866 owing about £11 million, equivalent to £1,132 million in 2025'),],
 'panic-1866': [
   ('危机后失业率', 8, '%', 1866,
    '原文：The crisis led to a sharp rise in unemployment to 8%'),],
 'rhode-island-banking-1990': [
   ('州政府为偿付储户发行的债券', 697, '百万美元', 1991,
    '原文：selling $697 million in bonds to repay people'),],
 'souk-al-manakh-1982': [
   ('全股市值（暴涨前）', 5, '十亿美元', 1981,
    '原文：market capitalization of all shares jumped in a few months from $5 billion to $100 billion'),
   ('全股市值（暴涨后）', 100, '十亿美元', 1982,
    '原文：from $5 billion to $100 billion'),
   ('无法兑付的未结支票总值', 94, '十亿美元', 1982,
    '原文：summed the value of worthless outstanding checks at the equivalent of US$94 billion from about 6,000 investors'),],
 'uk-secondary-banking-1973': [
   ('英格兰银行在救生艇行动中的损失', 100, '百万英镑', 1974,
    '原文：the Bank of England lost an estimated £100 million'),
   ('1973年10月加息后的利率', 13, '%', 1973,
    '原文：interest rates were raised to 13% in October 1973'),],
 'flash-crash-2010': [
   ('触发闪崩的单笔交易规模', 4.1, '十亿美元', 2010,
    '原文：A $4.1 billion trade on the New York Stock Exchange (NYSE)'),
   ('道指盘中跌幅点数', 1000, '点（以上）', 2010,
    '原文：a loss to the Dow Jones Industrial Average of over 1,000 points'),],
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FQ】补充 key_data（取自维基原文）。')
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
