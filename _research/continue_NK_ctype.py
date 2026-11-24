# -*- coding: utf-8 -*-
"""round 134b：crisis_type 与标题关键词的合理性。"""
import glob, json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]

KW = {
 '银行': ['银行', '挤兑', 'Bank', 'bank'],
 '货币': ['货币危机', '汇率', '贬值', '货币'],
 '债务': ['债务', '主权违约', '违约'],
 '泡沫': ['泡沫', '狂热', '投机'],
 '恶性通胀': ['恶性通胀', '恶性通货膨胀', 'hyperinflation'],
 '信用': ['信用'],
}
mis = []
for e in cases:
    t = e['title']
    ct = e['crisis_type']
    # 只检查"标题强烈暗示某类、但 crisis_type 明显不同"的
    for reg, kws in KW.items():
        if any(k in t for k in kws):
            if ct not in (reg, '其他'):
                # 允许一些合理跨类：货币危机也可能是债务；银行也可能是货币
                if reg == '银行' and ct in ('货币', '债务'):
                    continue
                if reg == '货币' and ct in ('银行', '债务'):
                    continue
                if reg == '债务' and ct in ('货币', '银行'):
                    continue
                mis.append((e['id'], e['title'][:24], ct, '标题暗示:' + reg))
            break
print('crisis_type 与标题可能不匹配的案例: %d' % len(mis))
for m in mis:
    print('  %-30s %-24s ct=%-6s %s' % m)
