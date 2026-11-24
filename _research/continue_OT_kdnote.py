# -*- coding: utf-8 -*-
"""round 156：key_data.value 与 note 中"原文"引述数字是否一致（粗筛，供人工判断）。"""
import glob, json, re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
NUM = re.compile(r'\d[\d,]*\.?\d*')

def canon(x):
    try:
        return float(str(x).replace(',', ''))
    except ValueError:
        return None

flags=[]
for e in es:
    for k in e.get('key_data') or []:
        v = canon(k.get('value'))
        if v is None: continue
        note = k.get('note') or ''
        # 只处理含"原文："的（英文维基直引）
        m = re.search(r'原文[：:]\s*(.+)', note, re.S)
        if not m: continue
        quote = m.group(1)
        nums = [canon(x) for x in NUM.findall(quote)]
        nums = [n for n in nums if n is not None]
        if not nums: continue
        # 是否有一个数与 value "相近"（等值、或 ×/÷10/100/1e6 之类单位换算后）
        ok = False
        for n in nums:
            for f in (1, 10, 100, 1000, 1e4, 1e6, 1e9, 0.1, 0.01, 0.001):
                if n != 0 and abs(n*f - v) <= max(abs(v)*0.02, 0.5):
                    ok = True; break
            if ok: break
        if not ok:
            flags.append((e['id'], k.get('label','')[:26], k.get('value'), [round(x,4) for x in nums[:5]], quote[:70]))
print('value 与 note 原文数字疑似不一致:', len(flags))
for f in flags[:40]:
    print('  %-24s %-26s v=%-10s noteNum=%s | %s' % f)
