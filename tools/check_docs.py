# -*- coding: utf-8 -*-
"""核对项目文档中的"当前状态"数字与实际数据是否一致。

起因：round 65 曾把 schools 的统计口径写错（记成 153 条，实际 1205 条观点），
说明"验证机制只检查条目内容，不检查项目文档的统计数字"是缺口。

检查范围：REPORT.md 首行状态、PROGRESS.md 中"现状："所在行、METRICS.json 最后一条。
只核对"当前状态"型表述；历史轮次中的数字（如"round 30 时 4%"）属记录，不参与比对。

用法：python -X utf8 tools/check_docs.py
退出码：0 = 一致；1 = 发现不一致
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def actual():
    es = [json.load(open(f, encoding='utf-8'))
          for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))]
    src = json.load(open(os.path.join(ROOT, 'data', 'sources.json'), encoding='utf-8'))
    cases = [e for e in es if not e['unit'].startswith('U6')]
    pages = len(glob.glob(os.path.join(ROOT, 'site', '*.html')))
    return {
        '条目': len(es),
        '案例': len(cases),
        '概念': len(es) - len(cases),
        '来源': src['count'],
        '页面': pages,
        'L3': sum(1 for e in es if e.get('level') == 'L3'),
        'comparison': sum(1 for e in es if e.get('comparison')),
        'related': sum(1 for e in es if e.get('related')),
        'key_data': sum(len(e.get('key_data', [])) for e in es),
        'timeline': sum(len(e.get('timeline', [])) for e in es),
        'schools': sum(len(e.get('schools', [])) for e in es),
        '政策达标案例': sum(1 for e in cases if e.get('policy_response')),
        '数据达标案例': sum(1 for e in cases if e.get('key_data')),
    }


# 文档中用于表述"当前值"的模式：(正则, 实际值键)
PATTERNS = [
    (r'总条目[:：]?\s*\*{0,2}(\d+)', '条目'),
    (r'总(\d+)\s*条', '条目'),
    (r'来源\s*\*{0,2}(\d+)\*{0,2}\s*条', '来源'),
    (r'站点\s*\*{0,2}(\d+)\*{0,2}\s*页', '页面'),
    (r'生成页面[:：]\s*(\d+)', '页面'),
    (r'`key_data`\s*\*{0,2}(\d+)\*{0,2}\s*条', 'key_data'),
    (r'timeline`?\s*事件\s*\*{0,2}(\d+)', 'timeline'),
    (r'schools`?\s*观点\s*\*{0,2}([\d,]+)', 'schools'),
]


def scan(path):
    """只返回**最后一条**"现状/当前"型表述中的数字（历史轮次记录不参与比对）。"""
    if not os.path.exists(path):
        return []
    lines = open(path, encoding='utf-8').read().splitlines()
    last = None
    # 排除描述历史/错误的语境（如"曾停留在……""滞后……""此前"）
    HIST = re.compile(r'(曾|此前|原先|滞后|仍停留|误记|修正|改为|不一致)')
    for i, line in enumerate(lines, 1):
        if re.search(r'(现状|当前|状态[:：])', line) and not HIST.search(line):
            last = (i, line)
    if not last:
        return []
    i, line = last
    out = []
    for pat, key in PATTERNS:
        for m in re.finditer(pat, line):
            try:
                v = int(m.group(1).replace(',', ''))
            except ValueError:
                continue
            out.append((i, key, v, line.strip()[:110]))
    return out


def main():
    act = actual()
    print('实际统计：')
    for k, v in act.items():
        print('  %-10s %s' % (k, v))

    bad = []
    for name in ('REPORT.md', 'PROGRESS.md'):
        p = os.path.join(ROOT, name)
        for ln, key, v, txt in scan(p):
            if act.get(key) is not None and v != act[key]:
                bad.append((name, ln, key, v, act[key], txt))

    # METRICS.json 最后一条
    mp = os.path.join(ROOT, 'METRICS.json')
    m = json.load(open(mp, encoding='utf-8'))
    last = m['metrics'][-1]
    for key, pat in (('sources_total', None),):
        pass
    if last.get('sources_total') and last['sources_total'] != act['来源']:
        bad.append(('METRICS.json', 0, '来源', last['sources_total'], act['来源'], '最后一条 sources_total'))

    print()
    if bad:
        print('文档与实际不一致 %d 处：' % len(bad))
        for b in bad:
            print('  %-14s L%-5s %-8s 文档=%s 实际=%s | %s' % (b[0], b[1], b[2], b[3], b[4], b[5][:60]))
        return 1
    print('结果：文档"当前状态"数字与实际一致')
    return 0


if __name__ == '__main__':
    sys.exit(main())
