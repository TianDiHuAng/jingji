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

    # 文档完整性：关键文档的最小规模与关键章节（防止误删）
    integrity = []
    checks = [
        ('PROGRESS.md', 400, ['## 轮次记录', '## 当前状态']),
        ('BLOCKERS.md', 50, ['##']),
        ('BACKLOG.md', 30, ['##']),
        ('DECISIONS.md', 20, ['##']),
    ]
    for name, min_lines, keys in checks:
        fp = os.path.join(ROOT, name)
        if not os.path.exists(fp):
            integrity.append((name, '文件缺失', ''))
            continue
        txt = open(fp, encoding='utf-8').read()
        n = len(txt.splitlines())
        if n < min_lines:
            integrity.append((name, '行数过少', '%d < %d' % (n, min_lines)))
        for k in keys:
            if k not in txt:
                integrity.append((name, '缺关键章节', k))
    # REPORT.md 必须含"可核对的状态数字行"（否则 scan 跳过、陈旧不被发现）
    if not scan(os.path.join(ROOT, 'REPORT.md')):
        integrity.append(('REPORT.md', '缺可核对状态行',
                          '需含如：当前 总条目 N、来源 N 条、站点 N 页'))
    # 轮次记录条数
    pp = os.path.join(ROOT, 'PROGRESS.md')
    if os.path.exists(pp):
        cnt = len(re.findall(r'维基百科第\s*\d+\s*轮', open(pp, encoding='utf-8').read()))
        if cnt < 20:
            integrity.append(('PROGRESS.md', '轮次记录过少', '%d 条' % cnt))

    # BACKLOG 的"概念缺口"表不得包含已经建成的条目（防依过时清单重复建，round 77 教训）
    bp = os.path.join(ROOT, 'BACKLOG.md')
    if os.path.exists(bp):
        _bt = open(bp, encoding='utf-8').read()
        _m = re.search(r'##\s*概念缺口.*?(?=\n##\s)', _bt, re.S)
        if _m:
            _ids = {json.load(open(f, encoding='utf-8'))['id']
                    for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))}
            for _cid in re.findall(r'`([a-z][a-z0-9\-]{2,})`', _m.group(0)):
                if _cid in _ids:
                    integrity.append(('BACKLOG.md', '把已建成条目列为缺口', _cid))

    # scope.md 须覆盖全部条目（防规划清单漏列）
    sp = os.path.join(ROOT, 'scope.md')
    if os.path.exists(sp):
        _eids = {json.load(open(f, encoding='utf-8'))['id']
                 for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))}
        _sids = {m.group(1) for m in re.finditer(r'^\|\s*([a-z0-9][a-z0-9\-]+)\s*\|',
                                                 open(sp, encoding='utf-8').read(), re.M)}
        _miss = sorted(_eids - _sids)
        if _miss:
            integrity.append(('scope.md', '未覆盖条目 %d 个' % len(_miss), ','.join(_miss[:5])))

    # SATURATION.json 不得误报饱和（项目规则：永不写 ALL_DONE，饱和为唯一终态且尚未达到）
    satp = os.path.join(ROOT, 'SATURATION.json')
    if os.path.exists(satp):
        try:
            _sat = json.load(open(satp, encoding='utf-8'))
            if _sat.get('saturated') is True:
                integrity.append(('SATURATION.json', '误报饱和(saturated=true)',
                                  '项目未终止，不应声明饱和'))
        except Exception:
            integrity.append(('SATURATION.json', '无法解析', ''))

    print()
    if integrity:
        print('文档完整性检查未通过 %d 项：' % len(integrity))
        for x in integrity:
            print('  %-14s %-12s %s' % x)
        return 1
    print('文档完整性：通过（规模与关键章节齐备）')
    if bad:
        print('文档与实际不一致 %d 处：' % len(bad))
        for b in bad:
            print('  %-14s L%-5s %-8s 文档=%s 实际=%s | %s' % (b[0], b[1], b[2], b[3], b[4], b[5][:60]))
        return 1
    print('结果：文档"当前状态"数字与实际一致')
    return 0


if __name__ == '__main__':
    sys.exit(main())
