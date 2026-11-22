# -*- coding: utf-8 -*-
"""tools/check_links.py — 全站终检：站内链接完整性 + SVG 结构 + 图片禁用 + 页面必备区块。
用法：python tools/check_links.py
"""
import os, re, glob, urllib.parse, xml.etree.ElementTree as ET
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT,'site')
errors=[]

htmls = glob.glob(os.path.join(SITE,'*.html'))
for f in htmls:
    d = open(f,encoding='utf-8').read()
    rel = os.path.basename(f)
    # 链接核验
    for m in re.finditer(r'href="([^"#]+)', d):
        href=m.group(1)
        if href.startswith(('http://','https://','mailto:')): continue
        target=os.path.join(SITE,urllib.parse.unquote(href.split('#')[0]))
        if not os.path.exists(target):
            errors.append(f'{rel}: 断链 {href}')
    # 禁止图片
    if re.search(r'<img\b', d, re.I):
        errors.append(f'{rel}: 含 <img>（TASK 禁止使用图片）')
    # SVG 结构与坐标
    for sm in re.finditer(r'<svg\b.*?</svg>', d, re.S):
        svg=sm.group(0)
        try:
            root=ET.fromstring(svg)
        except Exception as e:
            errors.append(f'{rel}: SVG XML 解析失败 {e}'); continue
        vb=root.get('viewBox','')
        if not vb: errors.append(f'{rel}: SVG 缺 viewBox')
        if re.search(r'<script|on\w+\s*=', svg, re.I):
            errors.append(f'{rel}: SVG 含脚本/事件属性')
        # 文字出界粗检
        try:
            _, _, vw, vh=[float(x) for x in re.split(r'[ ,]+',vb)]
            for tm in re.finditer(r'<text[^>]*x=[\"\x27]([\d.]+)[\"\x27][^>]*y=[\"\x27]([\d.]+)[\"\x27]', svg):
                x,y=float(tm.group(1)),float(tm.group(2))
                if x>vw+2 or y>vh+2:
                    errors.append(f'{rel}: SVG text 出界 ({x},{y}) > ({vw},{vh})')
        except: pass
    # 必备结构
    if '<header' not in d or '<main' not in d or 'style.css' not in d:
        errors.append(f'{rel}: 缺 header/main/style')

print('终检页面:', len(htmls))
print('ERRORS:', len(errors))
for e in errors[:40]: print('E',e)
if len(errors)>40: print('... 另有',len(errors)-40)
if errors: raise SystemExit(1)
print('结果：通过（0 error）')
