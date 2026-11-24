# -*- coding: utf-8 -*-
"""round 129b：region 与标题/内容的一致性；timeline year 类型；schools 空字段。"""
import glob
import json
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]

# 关键词 → 期望区域
KW = {
 '中国': '亚洲', '日本': '亚洲', '韩国': '亚洲', '印度': '亚洲', '泰国': '亚洲',
 '印尼': '亚洲', '马来': '亚洲', '越南': '亚洲', '缅甸': '亚洲', '斯里兰卡': '亚洲',
 '巴基斯坦': '亚洲', '孟加拉': '亚洲', '台湾': '亚洲', '香港': '亚洲', '海南': '亚洲',
 '阿根廷': '拉美', '巴西': '拉美', '墨西哥': '拉美', '智利': '拉美', '乌拉圭': '拉美',
 '哥伦比亚': '拉美', '委内瑞拉': '拉美', '秘鲁': '拉美', '玻利维亚': '拉美',
 '美国': '北美', '加拿大': '北美',
 '英国': '欧洲', '德国': '欧洲', '法国': '欧洲', '意大利': '欧洲', '西班牙': '欧洲',
 '希腊': '欧洲', '爱尔兰': '欧洲', '冰岛': '欧洲', '挪威': '欧洲', '芬兰': '欧洲',
 '瑞典': '欧洲', '丹麦': '欧洲', '荷兰': '欧洲', '瑞士': '欧洲', '奥地利': '欧洲',
 '葡萄牙': '欧洲', '俄罗斯': '欧洲', '土耳其': '欧洲', '波兰': '欧洲', '匈牙利': '欧洲',
 '埃及': '中东', '黎巴嫩': '中东', '伊朗': '中东', '以色列': '中东', '叙利亚': '中东',
 '沙特': '中东', '迪拜': '中东',
 '南非': '非洲', '尼日利亚': '非洲', '加纳': '非洲', '赞比亚': '非洲', '津巴布韦': '非洲',
 '安哥拉': '非洲', '肯尼亚': '非洲', '喀麦隆': '非洲',
 '新西兰': '大洋洲', '澳大利亚': '大洋洲',
}
mism = []
for e in cases:
    t = e['title']
    for kw, reg in KW.items():
        if kw in t and e['region'] not in (reg, '全球'):
            mism.append((e['id'], e['title'], e['region'], reg))
            break
print('=== 标题地名与 region 不一致 ===')
print('条数:', len(mism))
for m in mism:
    print('  %-28s %-22s region=%-4s 期望=%s' % (m[0], m[1][:20], m[2], m[3]))

# timeline year 非 int
print('\n=== timeline year 非整数 ===')
bad = [(e['id'], t.get('year')) for e in es for t in (e.get('timeline') or [])
       if not isinstance(t.get('year'), int)]
print('条数:', len(bad), bad[:8])

# schools 空 view
print('\n=== schools.view 空的 ===')
bad2 = [(e['id'], i) for e in es for i, s in enumerate(e.get('schools') or [])
        if not (s.get('view') or '').strip()]
print('条数:', len(bad2), bad2[:8])

# 空 one_line / overview
print('\n=== one_line 或 overview 为空的 ===')
bad3 = [e['id'] for e in es if not (e.get('one_line') or '').strip() or not (e.get('overview') or '').strip()]
print('条数:', len(bad3), bad3[:8])
