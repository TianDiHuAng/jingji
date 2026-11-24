# -*- coding: utf-8 -*-
"""HTML 结构与质量检查（补充 check.py 的数据校验与 check_links.py 的链接校验）。

覆盖 round 39—43 陆续发现的"生成逻辑缺陷"类问题：
  1. 标题层次跳级（h1→h3 等）
  2. 重复 id（同页多 SVG 的 marker 等）
  3. 表格缺 <th> 表头
  4. 缺 <meta name="description">
  5. 重复 description
  6. 重复 <title>
  7. 页内锚点目标不存在
  8. h1 数量 ≠ 1
  9. 重复 style 属性（生成时合并出错）
 10. 必需 head 元素（charset / viewport / lang）

用法：python -X utf8 tools/check_quality.py
退出码：0 = 全部通过；1 = 存在问题
"""
import glob
import os
import re
import sys
from collections import Counter

SITE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'site')


def main():
    files = sorted(glob.glob(os.path.join(SITE, '*.html')))
    if not files:
        print('未找到 site/*.html，请先运行 gen_site.py')
        return 1

    problems = []
    dsc_counter = Counter()
    title_counter = Counter()

    for path in files:
        name = os.path.basename(path)
        d = open(path, encoding='utf-8').read()

        # 1) 标题层次
        levels = [int(m.group(1)) for m in re.finditer(r'<h([1-6])[ >]', d)]
        prev = 0
        for lv in levels:
            if prev and lv > prev + 1:
                problems.append((name, '标题跳级', 'h%d → h%d' % (prev, lv)))
                break
            prev = lv

        # 2) 重复 id
        ids = re.findall(r'\sid="([^"]+)"', d)
        for k, v in Counter(ids).items():
            if v > 1:
                problems.append((name, '重复id', '%s ×%d' % (k, v)))
                break

        # 3) 表格缺 th
        for tbl in re.findall(r'<table.*?</table>', d, re.S):
            if '<th' not in tbl:
                problems.append((name, '表格缺th', tbl[:50]))
                break

        # 4)(5) meta description
        m = re.search(r'<meta name="description" content="([^"]*)"', d)
        if not m:
            problems.append((name, '缺description', ''))
        else:
            dsc_counter[m.group(1)] += 1

        # 6) title
        mt = re.search(r'<title>(.*?)</title>', d, re.S)
        if mt:
            title_counter[mt.group(1).strip()] += 1

        # 7) 锚点目标
        anchors = set(ids)
        for tgt in re.findall(r'href="#([^"]+)"', d):
            if tgt and tgt not in anchors:
                problems.append((name, '锚点不存在', tgt))
                break

        # 8) h1 数量
        n1 = len(re.findall(r'<h1[ >]', d))
        if n1 != 1:
            problems.append((name, 'h1数量', str(n1)))

        # 9) 重复 style 属性
        if re.search(r'<[^>]*style=[^>]*style=[^>]*>', d):
            problems.append((name, '重复style属性', ''))

        # 10) 必需 head 元素
        if 'charset' not in d[:800]:
            problems.append((name, '缺charset', ''))
        if 'viewport' not in d[:800]:
            problems.append((name, '缺viewport', ''))
        if 'lang="zh-CN"' not in d[:200]:
            problems.append((name, '缺lang', ''))

    # 全站唯一性
    for k, v in dsc_counter.items():
        if v > 1:
            problems.append(('(多页)', '重复description', '%s ×%d' % (k[:40], v)))
    for k, v in title_counter.items():
        if v > 1:
            problems.append(('(多页)', '重复title', '%s ×%d' % (k[:40], v)))

    # 输出
    print('检查页面: %d' % len(files))
    print('唯一 description: %d' % len(dsc_counter))
    print('唯一 title: %d' % len(title_counter))
    if problems:
        print('\n发现问题 %d 项：' % len(problems))
        kinds = Counter(p[1] for p in problems)
        for k, v in kinds.most_common():
            print('  %s: %d' % (k, v))
        print('\n前 20 条明细：')
        for p in problems[:20]:
            print('  %-32s %-14s %s' % (p[0][:32], p[1], p[2][:60]))
        print('\n结果：失败')
        return 1
    print('\n结果：通过（0 problem）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
