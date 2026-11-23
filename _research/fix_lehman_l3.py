# -*- coding: utf-8 -*-
"""修正：lehman 升L3（core应对应L3），补 deep_svg + l3_detail。"""
import json

def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def deep_svg(title, cat):
    parts = [
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 780 300' role='img' aria-label='机制与反馈回路深度图'>",
        f"<text x='20' y='26' class='ttl'>{esc(title)}：机制与反馈回路（类型：{esc(cat)}）</text>",
        # 第一行：触发 -> 传导 -> 后果
        "<g><rect x='30' y='60' width='160' height='56' rx='7' class='box'/>"
        "<text x='39' y='84' class='lbl'>冲击/触发</text>"
        "<text x='39' y='103' class='sub'>房价下跌、按揭违约上升</text></g>",
        "<g><rect x='215' y='60' width='160' height='56' rx='7' class='box'/>"
        "<text x='224' y='84' class='lbl'>资产端受损</text>"
        "<text x='224' y='103' class='sub'>MBS/衍生品估值下跌</text></g>",
        "<g><rect x='400' y='60' width='160' height='56' rx='7' class='box'/>"
        "<text x='409' y='84' class='lbl'>杠杆放大</text>"
        "<text x='409' y='103' class='sub'>净资产缩水快于资产</text></g>",
        "<g><rect x='585' y='60' width='160' height='56' rx='7' class='box'/>"
        "<text x='594' y='84' class='lbl'>破产</text>"
        "<text x='594' y='103' class='sub'>2008年申请破产保护</text></g>",
        "<line x1='190' y1='88' x2='210' y2='88' class='ar'/>",
        "<line x1='375' y1='88' x2='395' y2='88' class='ar'/>",
        "<line x1='560' y1='88' x2='580' y2='88' class='ar'/>",
        # 第二行：融资端与反馈
        "<g><rect x='30' y='150' width='160' height='56' rx='7' class='box'/>"
        "<text x='39' y='174' class='lbl'>融资依赖</text>"
        "<text x='39' y='193' class='sub'>短期回购/批发融资</text></g>",
        "<g><rect x='215' y='150' width='160' height='56' rx='7' class='box'/>"
        "<text x='224' y='174' class='lbl'>抵押品折价</text>"
        "<text x='224' y='193' class='sub'>对手方提高haircut</text></g>",
        "<g><rect x='400' y='150' width='160' height='56' rx='7' class='box'/>"
        "<text x='409' y='174' class='lbl'>流动性枯竭</text>"
        "<text x='409' y='193' class='sub'>无法续滚负债</text></g>",
        "<g><rect x='585' y='150' width='160' height='56' rx='7' class='box'/>"
        "<text x='594' y='174' class='lbl'>系统性传染</text>"
        "<text x='594' y='193' class='sub'>对手方与市场恐慌</text></g>",
        "<line x1='190' y1='178' x2='210' y2='178' class='ar'/>",
        "<line x1='375' y1='178' x2='395' y2='178' class='ar'/>",
        "<line x1='560' y1='178' x2='580' y2='178' class='ar'/>",
        # 反馈回路：传染 -> 抵押品进一步贬值
        "<path d='M665 210 L665 240 L190 240 L190 210' class='ar' fill='none'/>",
        "<text x='300' y='260' class='note'>反馈回路：市场恐慌 → 抵押品进一步贬值 → 更多追缴与抛售</text>",
        "</svg>",
    ]
    return ''.join(parts)

f = 'data/entries/lehman.json'
d = json.load(open(f, encoding='utf-8'))
d['level'] = 'L3'
d['deep_svg'] = deep_svg(d['title'], d['crisis_type'])
d['l3_detail'] = {
    'data_caveat': '本条目数值（如破产前员工数约2.5万）均为单一来源（Wikipedia）所载，未经第二独立来源核实，故标注为待核实；跨年数据如需比较须说明统计口径。',
    'controversy_summary': '关于雷曼破产的成因与"是否应当救助"存在显著分歧：一方强调其自身杠杆与流动性管理失败、应自行承担后果；另一方认为不救助引发系统性传染、代价更大。本站并列各方说法，不替读者下结论。',
    'framework_type': '银行',
}
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('lehman -> L3, deep_svg', len(d['deep_svg']), 'chars')

cov = json.load(open('coverage.json', encoding='utf-8'))
for e in cov['entries']:
    if e['id'] == 'lehman':
        e['level'] = 'L3'
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage synced')
