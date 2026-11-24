# -*- coding: utf-8 -*-
"""续作GB：为 latin-american-debt-1975 与 panic-1873 补写 policy_response。"""
import json
import os
import glob

POL = {
 'latin-american-debt-1975': (
   '**IMF 的角色及其批评**：IMF **支持**了这波借贷潮（作为更广的发展政策目标的一部分），'
   '但批评者认为该基金**低估了过度外债累积的风险**——尤其对高度依赖商品出口的经济体。'
   '**借贷结构的问题**：拉美各国政府以**短期贷款**形式增加债务而未建立适当保障，'
   '使该地区对汇率波动与外部冲击的暴露度不断上升；'
   '墨西哥尤其以**未来石油收入**为抵押借入**美元计价**贷款，'
   '因此当油价崩溃时其偿付能力迅速恶化，触发更广泛的危机。'
   '**规模**：1975—1982 年间，拉美对商业银行的债务以 **20.4%** 的年复合率增长。',
   '据 Wikipedia「Latin American debt crisis」International Monetary Fund 章节；'
   '政策主体：IMF 与拉美各国政府；'
   '说明：正文主要记载 IMF 的事前支持与事后批评，而非具体救助条款'),

 'panic-1873': (
   '**货币政策反应**：危机来临时，**英格兰银行将利率提高到 9%**。'
   '尽管如此，英国**并未经历**美国与欧洲大陆那种规模的金融混乱。'
   '（正文在 Britain 章节中把这一对比作为分析重点。）',
   '据 Wikipedia「Panic of 1873」Britain 章节；'
   '政策主体：英格兰银行；动作：将利率提高至 9%'),
}

n = 0
for eid, (view, basis) in POL.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('policy_response'):
        print('已有', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
                             'basis': basis + '；效果评价待核实',
                             'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作GB】补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('\n案例政策覆盖 %d/%d = %d%%' % (wp, len(cases), wp * 100 // len(cases)))

l3 = [e for e in es if e.get('level') == 'L3']
miss = [(e['id'], [x for x in ('deep_svg','l3_detail','key_data','timeline','policy_response') if not e.get(x)])
        for e in l3]
miss = [m for m in miss if m[1]]
print('L3 仍不完整 %d 条:' % len(miss))
for m in miss:
    print('  %-26s 缺: %s' % (m[0], ','.join(m[1])))
