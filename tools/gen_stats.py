"""生成项目统计可视化：docs/charts/*.svg（供 README 引用）与 docs/dashboard.html（单页总览）。
只读 data/，不改动 site/，因此不影响站点检查。全部为内联 SVG，零 JS，浅/深双模式可读。
用法：python -X utf8 tools/gen_stats.py
"""
import json, glob, os, re, collections, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'docs')
CH = os.path.join(OUT, 'charts')
os.makedirs(CH, exist_ok=True)

E = [json.load(open(f, encoding='utf-8')) for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'entries', '*.json')))]
SRC = json.load(open(os.path.join(ROOT, 'data', 'sources.json'), encoding='utf-8'))['sources']
cases = [e for e in E if e.get('unit') != 'U6 理论与制度']
kd = [k for e in E for k in e.get('key_data', [])]

STYLE = """<style>
.t{font:600 15px sans-serif;fill:#1f2328}.l{font:12px sans-serif;fill:#1f2328}.v{font:12px sans-serif;fill:#57606a}
.b{fill:#2f6fb3}.b2{fill:#c0602a}.g{stroke:#d0d7de;stroke-width:1}.bg{fill:#ffffff}
@media (prefers-color-scheme:dark){.t,.l{fill:#e6edf3}.v{fill:#9da7b3}.b{fill:#5aa0e6}.b2{fill:#e08a55}.g{stroke:#30363d}.bg{fill:#0d1117}}
</style>"""


def esc(s):
    return html.escape(str(s))


def hbar(name, title, items, note=''):
    """横向条形图。items: [(label, value)]"""
    items = [i for i in items if i[1] > 0]
    W, lw, top, row = 640, 150, 44, 26
    H = top + row * len(items) + (34 if note else 14)
    mx = max(v for _, v in items)
    pw = W - lw - 70
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(title)}">', STYLE,
           f'<rect class="bg" width="{W}" height="{H}" rx="6"/>', f'<text class="t" x="16" y="26">{esc(title)}</text>']
    for i, (lab, v) in enumerate(items):
        y = top + i * row
        w = max(2, pw * v / mx)
        out.append(f'<text class="l" x="{lw - 8}" y="{y + 15}" text-anchor="end">{esc(lab)}</text>')
        out.append(f'<rect class="b" x="{lw}" y="{y + 3}" width="{w:.1f}" height="17" rx="2"/>')
        out.append(f'<text class="v" x="{lw + w + 6:.1f}" y="{y + 16}">{v}</text>')
    if note:
        out.append(f'<text class="v" x="16" y="{H - 12}">{esc(note)}</text>')
    out.append('</svg>')
    svg = '\n'.join(out)
    open(os.path.join(CH, name + '.svg'), 'w', encoding='utf-8').write(svg)
    return svg


def vbar(name, title, items, note=''):
    """纵向柱状图（时间轴用）。"""
    W, H, l, b, t = 760, 300, 40, 50, 44
    n = len(items)
    mx = max(v for _, v in items) or 1
    cw = (W - l - 16) / n
    ph = H - t - b
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(title)}">', STYLE,
           f'<rect class="bg" width="{W}" height="{H}" rx="6"/>', f'<text class="t" x="16" y="26">{esc(title)}</text>',
           f'<line class="g" x1="{l}" y1="{H - b}" x2="{W - 16}" y2="{H - b}"/>']
    for i, (lab, v) in enumerate(items):
        x = l + i * cw
        h = ph * v / mx
        if v:
            out.append(f'<rect class="b2" x="{x + 1:.1f}" y="{H - b - h:.1f}" width="{cw - 2:.1f}" height="{h:.1f}"/>')
            out.append(f'<text class="v" x="{x + cw / 2:.1f}" y="{H - b - h - 4:.1f}" text-anchor="middle">{v}</text>')
        if i % max(1, n // 12) == 0:
            out.append(f'<text class="v" x="{x + cw / 2:.1f}" y="{H - b + 16}" text-anchor="middle">{esc(lab)}</text>')
    if note:
        out.append(f'<text class="v" x="16" y="{H - 12}">{esc(note)}</text>')
    out.append('</svg>')
    svg = '\n'.join(out)
    open(os.path.join(CH, name + '.svg'), 'w', encoding='utf-8').write(svg)
    return svg


def cnt(seq):
    return collections.Counter(seq).most_common()


charts = []
charts.append(hbar('by_unit', f'条目按单元分布（共 {len(E)} 条）', cnt(e.get('unit', '?') for e in E)))
charts.append(hbar('by_type', '条目按危机/条目类型分布', cnt(e.get('crisis_type', '?') for e in E)))
charts.append(hbar('cases_by_region', f'案例按地区分布（不含理论制度，共 {len(cases)} 条）', cnt(e.get('region', '?') for e in cases)))
charts.append(hbar('by_tier', '条目分级（层级 / 重要度）', cnt(f"{e.get('level')} · {e.get('tier')}" for e in E)))

# 案例年代分布：取时间线最早年份
dec = collections.Counter()
for e in cases:
    ys = [t.get('year') for t in e.get('timeline', []) if isinstance(t.get('year'), int)]
    if ys:
        y = min(ys)
        dec[max(1500, (y // 50) * 50) if y < 1800 else (y // 10) * 10] += 1
keys = sorted(dec)
labs = [(f'{k}s' if k >= 1800 else f'≤{k + 49}' if k == 1500 else f'{k}s'), dec[k]] if False else None
charts.append(vbar('cases_by_decade', '案例按起始年代分布（取时间线最早年份；1800 年前按 50 年分组）',
                   [((f'{k}' if k >= 1800 else f'{k}'), dec[k]) for k in keys]))


def skind(s):
    i = s.get('id', '')
    m = re.match(r'(w-[a-z]{2}|org|fed|bk|owid)', i)
    return {'w-en': '英文维基', 'w-zh': '中文维基', 'org': '机构文件', 'fed': '美联储史', 'bk': '图书', 'owid': 'OWID/世行数据'}.get(
        m.group(1) if m else '', '其他维基' if i.startswith('w-') else '其他')


charts.append(hbar('sources_by_kind', f'来源库构成（共 {len(SRC)} 条，全部 verified）', cnt(skind(s) for s in SRC)))
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(__file__)); from kdclass import is_single
single = sum(1 for k in kd if is_single(k))
charts.append(hbar('key_data_status', f'key_data 共 {len(kd)} 条：来源状态', [('本行列有 ≥2 个来源', len(kd) - single), ('本行只有 1 个来源', single)],
                   note='单一来源的数据已在页面明示“待核实”，不视为已独立印证。'))

# 仪表盘页
cards = [('条目', len(E)), ('案例', len(cases)), ('理论制度', len(E) - len(cases)), ('来源', len(SRC)), ('key_data', len(kd))]
dash = ['<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
        '<title>案例库统计总览</title><style>body{font-family:sans-serif;max-width:820px;margin:24px auto;padding:0 16px;color:#1f2328;background:#fff}'
        '.c{display:flex;gap:12px;flex-wrap:wrap;margin:16px 0}.c div{border:1px solid #d0d7de;border-radius:6px;padding:10px 16px}'
        '.c b{display:block;font-size:22px}svg{max-width:100%;height:auto;margin:10px 0}'
        '@media (prefers-color-scheme:dark){body{background:#0d1117;color:#e6edf3}.c div{border-color:#30363d}}</style></head><body>',
        '<h1>经济史与金融危机案例库 · 统计总览</h1><p>由 <code>tools/gen_stats.py</code> 从 <code>data/</code> 自动生成。</p><div class="c">']
dash += [f'<div><b>{v}</b>{esc(k)}</div>' for k, v in cards]
dash.append('</div>')
dash += charts
dash.append('</body></html>')
open(os.path.join(OUT, 'dashboard.html'), 'w', encoding='utf-8').write('\n'.join(dash))
print('charts', len(charts), 'entries', len(E), 'cases', len(cases), 'sources', len(SRC), 'key_data', len(kd), 'single', single)
