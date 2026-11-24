# -*- coding: utf-8 -*-
"""续作EP：为所有页面补 meta description（此前606页全部缺失）。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

# 1) page() 增加 desc 参数并输出 meta description
old_sig = '''def page(title, body, depth=0):
    """depth: 相对站点根目录的层级；条目页在 site/ 根，depth=0"""'''
new_sig = '''def page(title, body, depth=0, desc=''):
    """depth: 相对站点根目录的层级；条目页在 site/ 根，depth=0
    desc: 页面摘要（SEO/分享用）；缺省用站点通用描述。"""'''
if old_sig in s:
    s = s.replace(old_sig, new_sig, 1)
    print('签名已更新')

old_head = '''<title>{html.escape(title)} — 经济史与金融危机案例库</title>
<link rel="stylesheet" href="{prefix}style.css"></head><body>'''
new_head = '''<title>{html.escape(title)} — 经济史与金融危机案例库</title>
<meta name="description" content="{html.escape(_DSC)}">
<link rel="stylesheet" href="{prefix}style.css"></head><body>'''
if old_head in s:
    s = s.replace(old_head, new_head, 1)
    print('head 已加入 meta description')

# 在 return 前构造 _DSC
old_ret = '''    return f\'\'\'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'''
new_ret = '''    _DSC = (desc or '').strip().replace('\\n', ' ')
    _DSC = re.sub(r'\\*\\*|\\[|\\]|【|】', '', _DSC)
    if len(_DSC) > 150:
        _DSC = _DSC[:148].rstrip('，。；、 ') + '…'
    if not _DSC:
        _DSC = ('按时期、地区与危机类型组织的经济史与金融危机案例库：'
                '含危机案例、理论概念、时间线与可核验来源。')
    return f\'\'\'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'''
if old_ret in s:
    s = s.replace(old_ret, new_ret, 1)
    print('_DSC 构造已加入')

open(p, 'w', encoding='utf-8').write(s)
