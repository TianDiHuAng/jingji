# -*- coding: utf-8 -*-
"""续作FP：为12个案例补充 key_data（均取自维基原文，标注来源与待核实）。"""
import json
import os
import glob

# eid -> [ (label, value, unit, year, note) ]
KD = {
 'british-credit-1772': [
   ('阿姆斯特丹交易所银行营业额（1773年）', 30, '百万荷兰盾', 1773,
    '原文：turnover with the Amsterdam Exchange Bank plummeted from more than 50 million guilders in 1772 to 30 million in 1773'),],
 'china-liquidity-2013': [
   ('短期回购利率峰值（2013-06-20）', 25, '%', 2013,
    '原文：a sudden shortfall in the cash market resulting in short term repo rates in excess of 25%'),],
 'danish-bankruptcy-1813': [
   ('丹麦木材市场降幅（1806→1808）', 99, '%', 1808,
    '原文：reported a drop of 99% from 1806 to 1808'),],
 'defi': [
   ('DeFi 抵押品规模（2020年9月）', 9, '十亿美元', 2020,
    '原文：DeFi collateral levels had reached $9 billion'),
   ('加密资产总估值（监管讨论时）', 2.5, '万亿美元', 2022,
    '原文：crypto-assets already valued at $2.5 trillion'),],
 'dutch-collapse-1780': [
   ('被英国俘获的荷兰商船货物价值', 15, '百万荷兰盾', 1780,
    '原文：more than 200 Dutch merchantmen, with cargo to the amount of 15 million guilders, had been captured'),],
 'first-bank': [
   ('第一合众国银行政府认购股本', 2, '百万美元', 1791,
    '原文：government did not have $2 million, proposed that the government purchase the stock'),
   ('第一合众国银行公众认购股本', 8, '百万美元', 1791,
    '原文：The remaining $8 million of stock would be available to the public'),],
 'roman-currency': [
   ('安东尼安银币含银量（3世纪后半）', 2, '%', 260,
    '原文：the silver content of the antonianus fell to only 2%'),],
 'sherman-silver-purchase': [
   ('政府每月须购银量（1890年法）', 4.5, '百万盎司', 1890,
    '原文：the US government was now required to purchase 4.5 million ounces of silver bullion monthly'),],
 'sterling-area': [
   ('以英镑结算的全球贸易占比', 60, '%以上', 1930,
    '原文：More than 60 percent of global trade was financed, invoiced, and settled in sterling'),],
 'uruguay-2002': [
   ('美元化债务占GDP比重（2002）', 60, '%以上', 2002,
    '原文：Uruguay\'s mostly dollar-dominated debt added up to more than 60 percent on the GDP in 2002'),
   ('银行存款流失（截至2002年3月）', 12, '%', 2002,
    '原文：Uruguay lost approximately 12 percent of its bank deposits by March 2002'),],
 'stocks-fall-2011': [
   ('股市两周跌幅（2011）', 11, '%', 2011,
    '原文：due to the 11 percent stock market fall in two weeks'),],
 'jamaica-accords': [
   ('美国占全球产出份额（战后→1971）', 27, '%（自35%降至）', 1971,
    '原文：share of global economic output dropped from 35% to 27%'),],
 'panic-1884': [
   ('从美国流出的黄金（19世纪末）', 150, '百万美元以上', 1884,
    '原文：more than $150 million in gold was exported from the United States'),],
 'second-bank': [
   ('私人投资者持有第二合众国银行资本比例', 80, '%', 1816,
    '原文：Four thousand private investors held 80 percent of the bank\'s capital'),],
}

n_entry, n_kd = 0, 0
for eid, items in KD.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('key_data'):
        print('已有 key_data', eid); continue
    sid = next((s for s in d['sources'] if s.startswith('w-en')), d['sources'][0])
    rows = []
    for label, value, unit, year, note in items:
        rows.append({
            'label': label, 'value': value, 'unit': unit, 'year': year,
            'comparable_price': False,
            'note': note + '；单一来源待核实。',
            'sources': [sid],
        })
    d['key_data'] = rows
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FP】补充 key_data（取自维基原文）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n_entry += 1
    n_kd += len(rows)
    print('补数据', eid, len(rows), '条')

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)
print()
print('本轮补 %d 条目 / %d 条数据 | 案例有数据 %d/%d = %d%% | 全站 key_data %d 条'
      % (n_entry, n_kd, wk, len(cases), wk * 100 // len(cases), tk))
