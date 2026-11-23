# -*- coding: utf-8 -*-
"""阶段5生成器：data/ + coverage + sources → site/ 纯HTML+CSS（零JS）。
页面：首页、单元页×6、条目页×106、索引、时间线、来源列表、覆盖矩阵。"""
import json, os, glob, re, html
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT,'site')
os.makedirs(SITE, exist_ok=True)

def load(p):
    return json.load(open(os.path.join(ROOT,p),encoding='utf-8'))

cov = load('coverage.json')
src = load('data/sources.json')
sources = {s['id']:s for s in src['sources']}
entries = {}
for f in sorted(glob.glob(os.path.join(ROOT,'data/entries/*.json'))):
    d = json.load(open(f,encoding='utf-8'))
    entries[d['id']] = d

# ---------- CSS（浅/深双模式，CSS变量）----------
CSS = r'''
:root{
 --bg:#f7f8fa; --fg:#1a1d24; --card:#ffffff; --border:#dfe3ea; --muted:#616a7a;
 --accent:#1d5fa8; --accent-soft:#e8f1fb; --box:#eef3f9; --warn:#8a5a00; --warn-bg:#fff6e0;
 --shadow:0 1px 3px rgba(20,30,50,.08);
}
@media (prefers-color-scheme: dark){
 :root{
  --bg:#12151c; --fg:#e8ecf3; --card:#1c212b; --border:#333b49; --muted:#a7b0c0;
  --accent:#7db4f0; --accent-soft:#1e2d40; --box:#232b38; --warn:#f0c674; --warn-bg:#3a2f18;
  --shadow:0 1px 3px rgba(0,0,0,.3);
 }
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;line-height:1.65;font-size:15px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
header{background:var(--card);border-bottom:1px solid var(--border);box-shadow:var(--shadow);position:sticky;top:0;z-index:10}
header .wrap{display:flex;align-items:center;gap:22px;flex-wrap:wrap;padding-top:12px;padding-bottom:12px}
header .brand{font-weight:700;font-size:17px;color:var(--fg)}
nav{display:flex;gap:16px;flex-wrap:wrap}
nav a{color:var(--muted);font-size:14px}
main{padding:28px 0 60px}
h1{font-size:26px;margin:0 0 6px}h2{font-size:20px;margin:30px 0 12px}h3{font-size:16px;margin:20px 0 8px}
.lead{color:var(--muted);margin:0 0 20px}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px 20px;box-shadow:var(--shadow);margin-bottom:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:20px 0}
.stat{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center}
.stat .n{font-size:30px;font-weight:700;color:var(--accent)}.stat .l{font-size:13px;color:var(--muted)}
.tag{display:inline-block;background:var(--accent-soft);color:var(--accent);border-radius:20px;padding:1px 10px;font-size:12px;margin-right:6px}
.tag.warn{background:var(--warn-bg);color:var(--warn)}
.lvl{font-size:11px;border:1px solid var(--border);border-radius:4px;padding:0 5px;color:var(--muted)}
.entry h2{margin-top:0}
.section{margin:22px 0}.section h3{border-left:3px solid var(--accent);padding-left:10px}
ol,ul{padding-left:22px}li{margin:5px 0}
table{border-collapse:collapse;width:100%;font-size:14px;background:var(--card)}
th,td{border:1px solid var(--border);padding:7px 10px;text-align:left}
th{background:var(--accent-soft);color:var(--fg);font-weight:600}
.empty{color:var(--muted);font-style:italic}
.note{background:var(--warn-bg);color:var(--warn);border:1px solid var(--border);border-radius:8px;padding:12px 14px;font-size:13px}
.src-list{font-size:13px;color:var(--muted)}
figure{margin:18px 0;background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px;overflow-x:auto}
figure svg{max-width:100%;height:auto}
/* SVG 内文字与图形使用 CSS 变量，浅深双模式可读 */
svg .ttl{fill:var(--fg);font-size:15px;font-weight:600}
svg .lbl{fill:var(--fg);font-size:13px;font-weight:600}
svg .sub{fill:var(--muted);font-size:11px}
svg .note{fill:var(--muted);font-size:11px}
svg .box{fill:var(--box);stroke:var(--border);stroke-width:1.5}
svg .ar{stroke:var(--accent);stroke-width:2;marker-end:url(#arrowhead)}
svg .axis{stroke:var(--border);stroke-width:1.5}
svg .dot{fill:var(--accent)}
footer{border-top:1px solid var(--border);color:var(--muted);font-size:13px;padding:20px 0;text-align:center}
'''

def page(title, body, depth=0):
    """depth: 相对站点根目录的层级；条目页在 site/ 根，depth=0"""
    prefix = '../'*depth
    if depth==0: prefix=''
    nav = (f'<a href="{prefix}index.html">首页</a>'
           f'<a href="{prefix}index.html#units">单元</a>'
           f'<a href="{prefix}index-all.html">索引</a>'
           f'<a href="{prefix}cases.html">案例</a>'
           f'<a href="{prefix}concepts.html">概念</a>'
           f'<a href="{prefix}timeline.html">时间线</a>'
           f'<a href="{prefix}sources.html">来源</a>'
           f'<a href="{prefix}matrix.html">覆盖矩阵</a>')
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — 经济史与金融危机案例库</title>
<link rel="stylesheet" href="{prefix}style.css"></head><body>
<header><div class="wrap"><span class="brand">经济史与金融危机案例库</span><nav>{nav}</nav></div></header>
<main><div class="wrap">{body}</div></main>
<footer><div class="wrap">数据驱动 · 机器校验 · 诚实标注 · 零依赖静态站点</div></footer>
</body></html>'''

def esc(s): return html.escape(str(s or ''))

def fix_svg(svg):
    """给含 marker-end 但缺 defs 的 SVG 注入箭头 marker 定义（保证双模式可读）。"""
    if not svg or 'id="arrowhead"' in svg or ("class='ar'" not in svg and 'class="ar"' not in svg):
        return svg
    defs = ('<defs><marker id="arrowhead" markerWidth="8" markerHeight="8" '
            'refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" '
            'fill="var(--accent)"/></marker></defs>')
    return svg.replace('<svg ', '<svg ', 1).replace('>', '>'+defs, 1)

def entry_card(e):
    lv = e.get('level','L1')
    tier = e.get('tier','')
    return (f'<div class="card"><span class="lvl">{lv}</span> '
            f'<span class="tag">{esc(e.get("crisis_type",""))}</span>'
            f'<a href="{e["id"]}.html"><strong>{esc(e.get("title",""))}</strong></a>'
            f'<div class="src-list">{esc(e.get("period",""))} · {esc(e.get("region",""))} · {esc(tier)}</div></div>')

# ---------- 首页 ----------
units = ['U1 早期—17世纪','U2 18—19世纪','U3 20世纪上半','U4 20世纪下半','U5 21世纪','U6 理论与制度']
by_unit = defaultdict(list)
for e in entries.values(): by_unit[e.get('unit','')].append(e)
lv_count = Counter(e.get('level') for e in entries.values())
ver_count = sum(1 for s in src['sources'] if s['verified'])
home = [
 '<h1>经济史与金融危机案例库</h1>',
 '<p class="lead">按 时期 × 地区 × 危机类型 组织的历史案例与理论制度条目。数据驱动、机器校验、诚实标注。</p>',
 f'<div class="stats"><div class="stat"><div class="n">{len(entries)}</div><div class="l">条目总数</div></div>'
 f'<div class="stat"><div class="n">{lv_count["L2"]}</div><div class="l">L2 标准条目</div></div>'
 f'<div class="stat"><div class="n">{lv_count["L1"]}</div><div class="l">L1 骨架条目</div></div>'
 f'<div class="stat"><div class="n">{ver_count}</div><div class="l">已核对来源</div></div></div>',
 '<div class="note">本站所有数字除明确标注来源与口径外一律列为"待核实"；有争议观点并列各方说法，不替读者下结论。不做预测，不提供投资建议。</div>',
 '<h2 id="units">单元导航</h2><div class="grid">'
]
for u in units:
    home.append(f'<div class="card"><h3><a href="unit-{u.split()[0].lower()}.html">{esc(u)}</a></h3>'
                f'<p class="src-list">{len(by_unit[u])} 条</p></div>')
home += ['</div>',
 '<h2>快速入口</h2><div class="grid">',
 '<div class="card"><a href="cases.html"><strong>案例索引</strong></a><p class="src-list">按时期分组的全部危机案例，标注地区与类型</p></div>',
 '<div class="card"><a href="concepts.html"><strong>概念索引</strong></a><p class="src-list">按类型分组的理论与制度概念，含定义摘要</p></div>',
 '<div class="card"><a href="index-all.html"><strong>全站条目索引</strong></a><p class="src-list">按标题与时期浏览全部条目</p></div>',
 '<div class="card"><a href="timeline.html"><strong>时间线</strong></a><p class="src-list">按年份排列的历史事件</p></div>',
 '<div class="card"><a href="sources.html"><strong>来源列表</strong></a><p class="src-list">来源库与核验状态</p></div>',
 '<div class="card"><a href="matrix.html"><strong>覆盖矩阵</strong></a><p class="src-list">时期×地区×危机类型覆盖与空白</p></div>',
 '</div>']
open(os.path.join(SITE,'index.html'),'w',encoding='utf-8').write(page('首页',''.join(home)))

# ---------- 单元页 ----------
for u in units:
    uid = u.split()[0].lower()
    body = [f'<h1>{esc(u)}</h1>', f'<p class="lead">本单元共 {len(by_unit[u])} 条。</p>', '<div class="grid">']
    for e in sorted(by_unit[u], key=lambda x:x.get('period','')):
        body.append(entry_card(e))
    body.append('</div>')
    open(os.path.join(SITE,f'unit-{uid}.html'),'w',encoding='utf-8').write(page(u,''.join(body)))

# ---------- 条目页 ----------
def src_link(sid):
    s = sources.get(sid)
    if not s: return esc(sid)
    flag = '' if s['verified'] else '（待核实）'
    u = s.get('url','')
    return f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(s["title"])}</a>{flag}'

def render_entry(e):
    b = [f'<div class="entry"><h1>{esc(e.get("title",""))}</h1>',
         f'<p class="lead">{esc(e.get("one_line",""))}</p>',
         '<p><span class="tag">'+esc(e.get('crisis_type',''))+'</span>'
         f'<span class="tag">{esc(e.get("period",""))}</span>'
         f'<span class="tag">{esc(e.get("region",""))}</span>'
         f'<span class="lvl">{esc(e.get("level",""))} · {esc(e.get("tier",""))}</span></p>']
    def sec(title, content):
        if content:
            b.append(f'<div class="section"><h3>{title}</h3>{content}</div>')
    sec('概述', f'<p>{esc(e.get("overview",""))}</p>' if e.get('overview') else '')
    tl = e.get('timeline',[])
    if tl:
        sec('时间线', '<ul>'+''.join(f'<li><strong>{esc(t.get("display",""))}</strong>：{esc(t.get("event",""))} '
             f'<span class="src-list">[{", ".join(src_link(s) for s in t.get("sources",[]))}]</span></li>' for t in tl)+'</ul>')
    if e.get('background'):
        sec('背景条件', '<ul>'+''.join(f'<li>{esc(x)}</li>' for x in e['background'])+'</ul>')
    cc = e.get('causal_chain',[])
    if cc:
        sec('触发与传导机制','<ol>'+''.join(f'<li>{esc(s.get("step",""))} '
            f'<span class="src-list">[{", ".join(src_link(x) for x in s.get("sources",[]))}]</span></li>' for s in cc)+'</ol>')
    kd = e.get('key_data',[])
    if kd:
        rows='<table><tr><th>指标</th><th>数值</th><th>单位/口径</th><th>年份</th><th>来源</th></tr>'
        for d in kd:
            rows+=f'<tr><td>{esc(d.get("label"))}</td><td>{esc(d.get("value"))}</td><td>{esc(d.get("unit"))}</td><td>{esc(d.get("year"))}</td><td>{", ".join(src_link(s) for s in d.get("sources",[]))}</td></tr>'
        rows+='</table>'
        sec('关键数据', rows)
    sch = e.get('schools',[])
    if sch:
        sec('各方解释','<ul>'+''.join(f'<li><strong>{esc(s.get("holder"))}</strong>：{esc(s.get("view"))} '
            f'<span class="src-list">（依据：{esc(s.get("basis",""))} [{", ".join(src_link(x) for x in s.get("sources",[]))}]）</span></li>' for s in sch)+'</ul>')
    pol = e.get('policy_response',[])
    if pol:
        sec('政策应对及评价分歧','<ul>'+''.join(f'<li><strong>{esc(p.get("holder"))}</strong>：{esc(p.get("view"))} '
            f'<span class="src-list">（{esc(p.get("basis",""))}）</span></li>' for p in pol)+'</ul>')
    if e.get('comparison'):
        sec('与其他案例的相似与不同', f'<p>{esc(e["comparison"])}</p>')
    if e.get('svg'):
        sec('一图：机制示意', f'<figure>{fix_svg(e["svg"])}</figure>')
    # L3 深度：数据口径说明 + 复杂反馈回路图
    l3 = e.get('l3_detail')
    if l3:
        detail = (f'<p>{esc(l3.get("data_caveat",""))}</p>'
                  f'<p>{esc(l3.get("controversy_summary",""))}</p>')
        sec('L3 深度说明：数据口径与争议', detail)
    if e.get('deep_svg'):
        sec('L3 深度图：机制与反馈回路', f'<figure>{fix_svg(e["deep_svg"])}</figure>')
    if e.get('pending_notes'):
        sec('待核实', f'<div class="note">{esc(e["pending_notes"])}</div>')
    srcs = e.get('sources',[])
    sec('来源', '<div class="src-list">' + ('<br>'.join('• '+src_link(s) for s in srcs) if srcs else '<span class="empty">暂无</span>') + '</div>')
    if e.get('related'):
        sec('相关条目', '<ul>'+''.join(f'<li><a href="{esc(r)}.html">{esc(entries.get(r,{}).get("title",r))}</a></li>' for r in e['related'])+'</ul>')
    b.append('</div>')
    return ''.join(b)

for eid, e in entries.items():
    open(os.path.join(SITE,f'{eid}.html'),'w',encoding='utf-8').write(page(e.get('title',eid), render_entry(e)))

# ---------- 全站索引 ----------
idx = ['<h1>全站条目索引</h1>', '<p class="lead">共 '+str(len(entries))+' 条，按单元与标题排列。</p>']
for u in units:
    idx.append(f'<h2>{esc(u)}</h2>')
    for e in sorted(by_unit[u], key=lambda x:x.get('title','')):
        idx.append(f'<div class="card"><span class="lvl">{e.get("level")}</span> '
            f'<a href="{e["id"]}.html">{esc(e.get("title"))}</a> '
            f'<span class="src-list">{esc(e.get("crisis_type"))} · {esc(e.get("region"))}</span></div>')
open(os.path.join(SITE,'index-all.html'),'w',encoding='utf-8').write(page('全站索引',''.join(idx)))

# ---------- 时间线 ----------
tl_entries = []
for e in entries.values():
    for t in e.get('timeline',[]):
        y = t.get('year')
        if isinstance(y,(int,float)):
            tl_entries.append((int(y), e))
tl_entries.sort(key=lambda x:x[0])
timeline = ['<h1>时间线</h1>', '<p class="lead">按年份排列（仅含已写时间节点的条目）。</p>', '<table><tr><th>年份</th><th>条目</th><th>类型</th></tr>']
for y,e in tl_entries:
    timeline.append(f'<tr><td>{y}</td><td><a href="{e["id"]}.html">{esc(e.get("title"))}</a></td><td>{esc(e.get("crisis_type"))}</td></tr>')
timeline.append('</table>')
open(os.path.join(SITE,'timeline.html'),'w',encoding='utf-8').write(page('时间线',''.join(timeline)))

# ---------- 来源列表 ----------
sl = ['<h1>来源列表</h1>', f'<p class="lead">共 {len(src["sources"])} 条；已核对 {ver_count} 条，待核实 {len(src["sources"])-ver_count} 条。</p>',
      '<table><tr><th>标题</th><th>作者/机构</th><th>年份</th><th>类型</th><th>核验</th></tr>']
for s in src['sources']:
    flag = '✅已核对' if s['verified'] else '⚠待核实'
    link = f'<a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["title"])}</a>' if s.get('url') else esc(s['title'])
    sl.append(f'<tr><td>{link}</td><td>{esc(s.get("author"))}</td><td>{esc(s.get("year"))}</td><td>{esc(s.get("type"))}</td><td>{flag}</td></tr>')
sl.append('</table>')
open(os.path.join(SITE,'sources.html'),'w',encoding='utf-8').write(page('来源列表',''.join(sl)))

# ---------- 覆盖矩阵页 ----------
matrix_html = open(os.path.join(ROOT,'COVERAGE_MATRIX.md'),encoding='utf-8').read()
# 简易 Markdown 表格转 HTML
mbody=['<h1>覆盖矩阵</h1>','<p class="lead">时期 × 地区 × 危机类型覆盖；空白格子已标注。</p>']
for line in matrix_html.splitlines():
    if line.startswith('#'):
        mbody.append(f'<h2>{esc(line.lstrip("# "))}</h2>')
    elif line.startswith('|') and '---' not in line:
        cells=[c.strip() for c in line.strip('|').split('|')]
        mbody.append('<table><tr>'+''.join(f'<td>{esc(c)}</td>' for c in cells)+'</tr></table>')
    elif line.startswith('- '):
        mbody.append(f'<p class="src-list">{esc(line[2:])}</p>')
    elif line.strip() and not line.startswith('>'):
        mbody.append(f'<p>{esc(line)}</p>')
open(os.path.join(SITE,'matrix.html'),'w',encoding='utf-8').write(page('覆盖矩阵',''.join(mbody)))

# ---------- 概念索引页 ----------
CONCEPT_ORDER = ['理论', '制度', '货币', '银行', '债务', '泡沫', '其他']
concepts = [e for e in entries.values() if e.get('unit') == 'U6 理论与制度']
by_type = {}
for e in concepts:
    by_type.setdefault(e.get('crisis_type') or '其他', []).append(e)
cb = ['<h1>概念索引</h1>',
      f'<p class="lead">共 {len(concepts)} 条理论与制度概念，按类型分组；每条给出定义摘要，点击进入详情。</p>',
      '<p class="src-list">' + ' · '.join(
          f'<a href="#t-{esc(t)}">{esc(t)}（{len(by_type[t])}）</a>'
          for t in CONCEPT_ORDER if t in by_type) + '</p>']
for t in CONCEPT_ORDER:
    if t not in by_type:
        continue
    rows = sorted(by_type[t], key=lambda x: x.get('title') or '')
    cb.append(f'<h2 id="t-{esc(t)}">{esc(t)}（{len(rows)} 条）</h2>')
    cb.append('<table><tr><th>概念</th><th>定义摘要</th></tr>')
    for e in rows:
        cb.append(f'<tr><td><a href="{e["id"]}.html">{esc(e.get("title"))}</a></td>'
                  f'<td>{esc(e.get("one_line"))}</td></tr>')
    cb.append('</table>')
open(os.path.join(SITE,'concepts.html'),'w',encoding='utf-8').write(page('概念索引',''.join(cb)))

# ---------- 案例索引页 ----------
UNIT_ORDER = ['U1 早期—17世纪', 'U2 18—19世纪', 'U3 20世纪上半', 'U4 20世纪下半', 'U5 21世纪']
cases = [e for e in entries.values() if e.get('unit') != 'U6 理论与制度']
by_unit = {}
for e in cases:
    by_unit.setdefault(e.get('unit') or '未归类', []).append(e)
kb = ['<h1>案例索引</h1>',
      f'<p class="lead">共 {len(cases)} 条历史与当代危机案例，按时期单元分组；标注地区与危机类型，便于横向比较。</p>',
      '<p class="src-list">' + ' · '.join(
          f'<a href="#u-{i}">{esc(u)}（{len(by_unit[u])}）</a>'
          for i, u in enumerate(UNIT_ORDER) if u in by_unit) + '</p>']
for i, u in enumerate(UNIT_ORDER):
    if u not in by_unit:
        continue
    rows = by_unit[u]
    # 按首个时间线年份排序（无年份者置于末尾）
    def _key(e):
        ys = [t.get('year') for t in e.get('timeline', []) if isinstance(t.get('year'), (int, float))]
        return (min(ys) if ys else 99999, e.get('title') or '')
    rows.sort(key=_key)
    kb.append(f'<h2 id="u-{i}">{esc(u)}（{len(rows)} 条）</h2>')
    kb.append('<table><tr><th>案例</th><th>地区</th><th>类型</th><th>层级</th></tr>')
    for e in rows:
        kb.append(f'<tr><td><a href="{e["id"]}.html">{esc(e.get("title"))}</a></td>'
                  f'<td>{esc(e.get("region"))}</td><td>{esc(e.get("crisis_type"))}</td>'
                  f'<td>{esc(e.get("level"))}</td></tr>')
    kb.append('</table>')
open(os.path.join(SITE,'cases.html'),'w',encoding='utf-8').write(page('案例索引',''.join(kb)))

# ---------- CSS 文件 ----------
open(os.path.join(SITE,'style.css'),'w',encoding='utf-8').write(CSS)

# ---------- 站内链接核验 ----------
import urllib.parse
broken=[]
for f in glob.glob(os.path.join(SITE,'*.html')):
    d=open(f,encoding='utf-8').read()
    for m in re.finditer(r'href="([^"#]+)',d):
        href=m.group(1)
        if href.startswith(('http://','https://')): continue
        target=os.path.join(SITE,urllib.parse.unquote(href.split('#')[0]))
        if not os.path.exists(target):
            broken.append((os.path.basename(f),href))
print('生成页面:', len(glob.glob(os.path.join(SITE,'*.html'))))
print('站内断链:', len(broken))
for x in broken[:20]: print('  BROKEN',x)
if broken: raise SystemExit(1)
