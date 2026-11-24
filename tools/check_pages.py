# -*- coding: utf-8 -*-
"""检查生成页面之间的数字一致性。

起因：round 82 把验证页的"独立机构印证"由 15 修正为 2，但**首页仍显示 15**——
两处用不同代码计算同一指标。
本工具直接解析**已生成的 HTML**，与真实数据交叉核对，可发现这类"改了 A 忘了 B"。

用法：python -X utf8 tools/check_pages.py
退出码：0 = 一致；1 = 发现不一致
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kdclass import counts as _kdcounts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')


def text_of(path):
    if not os.path.exists(path):
        return ''
    d = open(path, encoding='utf-8').read()
    return re.sub(r'<[^>]+>', ' ', d)


def nums(s):
    """提取页面上的纯数字（去千分位）。"""
    return [int(x.replace(',', '')) for x in re.findall(r'\b\d[\d,]*\b', s)]


def main():
    es = [json.load(open(f, encoding='utf-8'))
          for f in glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json'))]
    srcs = json.load(open(os.path.join(ROOT, 'data', 'sources.json'), encoding='utf-8'))['sources']
    cases = [e for e in es if not e['unit'].startswith('U6')]
    kd_total = sum(len(e.get('key_data', [])) for e in es)
    pages = len(glob.glob(os.path.join(SITE, '*.html')))

    # 统一口径（与 gen_site.py 内部一致）
    def _note(k):
        return k.get('note') or ''

    def _conf(k):
        n = _note(k)
        if any(w in n for w in ('两源差异', '存在差异', '数据分歧', '口径不同')):
            return False
        if not ('双源' in n or '印证' in n or '完全一致' in n):
            return False
        return any(str(x).startswith('fed-') for x in (k.get('sources') or []))

    def _stat(k):
        n = _note(k)
        if any(w in n for w in ('两源差异', '存在差异', '数据分歧', '口径不同')):
            return False
        if not ('双源' in n or '印证' in n or '完全一致' in n):
            return False
        s = k.get('sources') or []
        return (any(str(x).startswith(('owid-', 'org-')) for x in s)
                and not any(str(x).startswith('fed-') for x in s))

    _c = _kdcounts(es)
    conf, stat = _c['confirmed'], _c['statview']

    expect = {
        '条目总数': len(es),
        '可用来源': sum(1 for s in srcs if s.get('verified')),
        '关键数据条数': kd_total,
        '独立机构双源印证': conf,
        '统计口径对照': stat,
    }

    problems = []
    home = os.path.join(SITE, 'index.html')
    ht = text_of(home)
    for label, val in expect.items():
        # 在首页上找 "<数字> <label>" 形式
        m = re.search(r'(\d[\d,]*)\s*' + re.escape(label), ht)
        if not m:
            problems.append(('index.html', label, '未找到该统计项', val))
            continue
        got = int(m.group(1).replace(',', ''))
        if got != val:
            problems.append(('index.html', label, got, val))

    # 验证页板块标题中的条数
    vt = text_of(os.path.join(SITE, 'verification.html'))
    for label, val in (('独立机构双源印证', conf), ('不同统计口径对照', stat),
                       ('跨语言维基对照', None)):
        m = re.search(re.escape(label) + r'（(\d+)\s*条）', vt)
        if not m:
            problems.append(('verification.html', label, '未找到该板块', val))
            continue
        if val is not None and int(m.group(1)) != val:
            problems.append(('verification.html', label, int(m.group(1)), val))

    # ── 文案与导航一致性：comparison 提到的条目应出现在 related 中 ──
    _ids = {e['id'] for e in es}
    for e in es:
        comp = e.get('comparison') or ''
        if not comp:
            continue
        mentioned = {i for i in _ids if i != e['id'] and i in comp}
        missing = mentioned - set(e.get('related', []))
        if missing:
            problems.append(('data/' + e['id'] + '.json', '文案与导航一致性',
                             '提到但未在related中', ','.join(sorted(missing)[:3])))

    print('期望值:', expect)
    print('页面数:', pages)
    print()
    if problems:
        print('页面间数字不一致 %d 处：' % len(problems))
        for p in problems:
            print('  %-18s %-14s 页面=%s 应为=%s' % p)
        return 1
    print('结果：首页与验证页的数字均与真实数据一致')
    return 0


if __name__ == '__main__':
    sys.exit(main())
