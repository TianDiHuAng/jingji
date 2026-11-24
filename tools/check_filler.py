# -*- coding: utf-8 -*-
"""检测"无信息量内容"——模板套话、占位数值、空泛表述。

起因：round 73 发现 57 条模板化 comparison（"与同为X类共享传导机制…"）。
这类内容对同类条目**全都成立**，因此不含信息量；而它曾把 comparison 覆盖率
从 51% 推到 100%。此前 CO 轮手工清过 300 条，但未固化为检查，故后来重新长出。

本工具把判据固化，防止重犯。

用法：python -X utf8 tools/check_filler.py
退出码：0 = 未发现；1 = 发现问题
"""
import glob
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 模板套话特征（正则）
TEMPLATES = [
    (r'与同为「[^」]*」类', '模板句「与同为X类」'),
    (r'与同类案例共享', '模板句「与同类案例共享」'),
    (r'共享相似传导机制', '模板句「共享相似传导机制」'),
    (r'差异在(于)?时期(与)?地区', '模板句「差异在时期地区」'),
    (r'对其他案例均适用', '模板句「对其他案例均适用」'),
]

# 占位数值特征
PLACEHOLDER_UNIT = ('示意', '归一化', '非史料原值', '相对值（起点', '占位')

# 极短字段（无实质内容的下限）
MIN_LEN = {'comparison': 24, 'one_line': 8, 'overview': 40}


def main():
    files = sorted(glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json')))
    entries = [json.load(open(f, encoding='utf-8')) for f in files]
    issues = []

    # 1) 模板句检测
    for e in entries:
        for field in ('comparison', 'overview', 'policy_response', 'one_line'):
            v = e.get(field)
            if isinstance(v, str):
                for pat, name in TEMPLATES:
                    if re.search(pat, v):
                        issues.append((e['id'], field, name, v[:70]))
            elif isinstance(v, list):
                for item in v:
                    txt = item.get('view', '') if isinstance(item, dict) else str(item)
                    for pat, name in TEMPLATES:
                        if re.search(pat, txt):
                            issues.append((e['id'], field, name, txt[:70]))

    # 2) 占位数值检测
    for e in entries:
        for k in e.get('key_data', []) or []:
            unit = str(k.get('unit', ''))
            note = str(k.get('note', ''))
            if any(w in unit for w in PLACEHOLDER_UNIT) or '非史料原值' in note:
                issues.append((e['id'], 'key_data', '占位/示意数值',
                               '%s = %s %s' % (k.get('label', '')[:24], k.get('value'), unit[:16])))

    # 3) 极短字段
    for e in entries:
        for field, mn in MIN_LEN.items():
            v = e.get(field)
            if isinstance(v, str) and v.strip() and len(v.strip()) < mn:
                issues.append((e['id'], field, '字段过短', v[:50]))

    # 4) 跨条目重复句（同一句话出现在 >=3 个条目 → 视为模板）
    sent_map = Counter()
    sent_owner = {}
    for e in entries:
        seen = set()
        for field in ('comparison', 'overview'):
            v = e.get(field)
            if not isinstance(v, str):
                continue
            # 去掉括号内的元信息说明（如"（理论概念条目，标准教科书定义…）"），
            # 这类说明标注条目性质，重复出现属正常，不算模板套话
            _v = re.sub(r'（[^）]*）', '', v)
            for s in re.split(r'[。；！？]', _v):
                s = s.strip()
                if 15 <= len(s) <= 200 and s not in seen:
                    seen.add(s)
                    sent_map[s] += 1
                    sent_owner.setdefault(s, []).append(e['id'])
    for s, n in sent_map.items():
        if n >= 3:
            issues.append((sent_owner[s][0], '多条目', '跨条目重复句（%d次）' % n, s[:60]))

    print('扫描条目: %d' % len(entries))
    if issues:
        print('发现疑似无信息量内容 %d 处：' % len(issues))
        seen = set()
        for eid, field, kind, txt in issues:
            key = (kind, txt[:30])
            if key in seen:
                continue
            seen.add(key)
            print('  %-26s %-14s %-24s %s' % (eid[:26], field, kind, txt))
        print('\n结果：需人工判断或清理')
        return 1
    print('\n结果：未发现模板套话、占位数值或过短字段')
    return 0


if __name__ == '__main__':
    sys.exit(main())
