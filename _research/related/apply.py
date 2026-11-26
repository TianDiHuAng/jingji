# -*- coding: utf-8 -*-
"""把 _research/related/map.py 的概念→案例关联写入 data/entries/*.json。

只添加链接（不删除既有链接），保持 related 字母序与文件原有 CRLF 换行。
"""
import glob
import importlib.util
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
spec = importlib.util.spec_from_file_location('mapmod', os.path.join(ROOT, '_research', 'related', 'map.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
MAP = mod.MAP


def load(path):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        raw = f.read()
    crlf = '\r\n' in raw
    return json.loads(raw), crlf


def dump(path, data, crlf):
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if crlf:
        text = text.replace('\n', '\r\n')
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)


def main():
    entries = {}
    raw = {}
    for path in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json')):
        data, crlf = load(path)
        entries[data['id']] = data
        raw[data['id']] = (path, crlf)

    cases = {i for i, d in entries.items() if not d['unit'].startswith('U6')}
    changed = 0
    added_total = 0
    report = []
    for cid, case_ids in MAP.items():
        if cid not in entries:
            raise SystemExit('unknown concept: ' + cid)
        e = entries[cid]
        if not e['unit'].startswith('U6'):
            raise SystemExit('not a concept: ' + cid)
        rel = list(e.get('related') or [])
        add = [x for x in case_ids if x in cases and x not in rel]
        if not add:
            continue
        rel = sorted(set(rel) | set(add))
        e['related'] = rel
        changed += 1
        added_total += len(add)
        report.append((cid, add))

    for cid, (path, crlf) in raw.items():
        if cid in {r[0] for r in report}:
            dump(path, entries[cid], crlf)

    print('changed entries:', changed, 'added edges:', added_total)
    for cid, add in report:
        print(cid, '+', ','.join(add))


if __name__ == '__main__':
    main()
