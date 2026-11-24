# -*- coding: utf-8 -*-
"""find_val.py — 全字段"同款数字"搜索工具（沉淀 round 148/149 教训）。

背景：同一处未核实数字常在多个字段重复出现（overview / one_line / comparison /
policy_response[].view / key_data / timeline / schools）。round 148 修 finnish 的 20%、
round 149 修 sterling 的 1.60，都是"只改了 overview、漏了 policy_response"。
本工具用于：改任何数字前/后，一次性列出它在**所有字段**的出现位置，避免漏改。

用法：
  python -X utf8 tools/find_val.py "1.60"              # 全库搜子串，列出所有字段命中
  python -X utf8 tools/find_val.py --id sterling-crisis-1976 "1.60"   # 限定单条
  python -X utf8 tools/find_val.py --regex "\\d+\\.\\d+%"             # 用正则搜全库
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENT = os.path.join(ROOT, 'data', 'entries')


def _fields(entry):
    """产出 (字段路径, 文本) —— 覆盖所有可能含数字的字符串字段。"""
    for f in ('one_line', 'overview', 'comparison'):
        if entry.get(f):
            yield f, entry[f]
    for i, pr in enumerate(entry.get('policy_response') or []):
        yield 'policy_response[%d].view' % i, pr.get('view') or ''
    for i, k in enumerate(entry.get('key_data') or []):
        yield 'key_data[%d].label' % i, k.get('label') or ''
        yield 'key_data[%d].value' % i, str(k.get('value', ''))
        yield 'key_data[%d].note' % i, k.get('note') or ''
    for i, t in enumerate(entry.get('timeline') or []):
        yield 'timeline[%d].event' % i, t.get('event') or ''
    for i, s in enumerate(entry.get('schools') or []):
        yield 'schools[%d].view' % i, s.get('view') or ''
    for i, c in enumerate(entry.get('causal_chain') or []):
        if isinstance(c, dict):
            yield 'causal_chain[%d].note' % i, (c.get('note') or c.get('text') or '')
        elif isinstance(c, str):
            yield 'causal_chain[%d]' % i, c


def main(argv):
    only_id = None
    use_re = False
    needle = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--id':
            only_id = argv[i + 1]; i += 2
        elif a == '--regex':
            use_re = True; needle = argv[i + 1]; i += 2
        else:
            needle = a; i += 1
    if not needle:
        print('用法: find_val.py [--id <entry>] [--regex] "<子串或正则>"'); return 2

    pat = re.compile(needle) if use_re else None
    hits = 0
    files = sorted(glob.glob(os.path.join(ENT, '*.json')))
    for fp in files:
        e = json.load(open(fp, encoding='utf-8'))
        eid = e.get('id')
        if only_id and eid != only_id:
            continue
        for path, text in _fields(e):
            if not text:
                continue
            occ = []
            if use_re:
                for m in pat.finditer(text):
                    s = m.start(); occ.append(text[max(0, s - 30):s + len(m.group(0)) + 30])
            else:
                s = text.find(needle)
                while s >= 0:
                    occ.append(text[max(0, s - 30):s + len(needle) + 30])
                    s = text.find(needle, s + 1)
            if occ:
                hits += 1
                print('%-28s %-26s …%s…' % (eid, path, occ[0].replace('\n', ' ')))
    print('\n命中字段数: %d' % hits)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
