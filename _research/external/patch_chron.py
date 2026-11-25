# 给 gen_site.py 增加 chronology.html（年表对照页）、导航与首页卡片；保留 CRLF
p='tools/gen_site.py'
b=open(p,'rb').read(); crlf=b'\r\n' in b
s=b.decode('utf-8').replace('\r\n','\n')
assert 'chronology.html' not in s
s=s.replace("""           f'<a href="{prefix}verification.html">核实状态</a>'\n""","""           f'<a href="{prefix}verification.html">核实状态</a>'\n           f'<a href="{prefix}chronology.html">年表对照</a>'\n""",1)
s=s.replace("""    '<div class="card"><a href="verification.html"><strong>数据核实状态</strong></a><p class="src-list">已双源印证的数据与两源差异并列项</p></div>',\n""","""    '<div class="card"><a href="verification.html"><strong>数据核实状态</strong></a><p class="src-list">已双源印证的数据与两源差异并列项</p></div>',\n    '<div class="card"><a href="chronology.html"><strong>年表对照</strong></a><p class="src-list">本库案例年份与 IMF 系统性危机数据库并列</p></div>',\n""",1)
s=s.replace("_SPECIAL = {'index','cases','concepts','index-all','timeline','sources','verification','matrix'}","_SPECIAL = {'index','cases','concepts','index-all','timeline','sources','verification','matrix','chronology'}",1)
anchor="# ---------- 概念索引页 ----------"
code='''# ---------- 年表对照页（Laeven–Valencia 2018） ----------
_chp = os.path.join(os.path.dirname(SITE), 'data', 'chronology_lv.json')
if os.path.exists(_chp):
    _ch = json.load(open(_chp, encoding='utf-8'))
    _sid = _ch['source']
    _order = ['一致', '相差1年', '该类型年份不同', 'LV未列该类型']
    _expl = {'一致': '数据库所列同类型危机起始年落在本库时间段内',
             '相差1年': '数据库起始年与本库时间段相差 1 年',
             '该类型年份不同': '数据库对该国列有同类型危机，但起始年不在本库时间段附近',
             'LV未列该类型': '数据库未将该国此时期列为同类型危机'}
    cb = ['<h1>年表对照：本库案例 × IMF 系统性危机数据库</h1>',
          '<p>把本库案例的时间段与 Laeven 与 Valencia（2018）附录 Table 1「Crisis Dates」中同一国家、同一类型危机的起始年并列。',
          '两者口径不同：该数据库只收录<strong>系统性</strong>银行危机及货币、主权债务危机，起始年按其自身判定标准；本库时间段取条目时间线最早与最晚年份。',
          '因此「不一致」只说明口径或定义不同，本页不判断哪一方正确。</p>',
          '<p class="src-list">来源：' + src_link(_sid) + '。泡沫类案例按银行危机列对照。</p>']
    for st in _order:
        rs = [r for r in _ch['rows'] if r['status'] == st]
        if not rs: continue
        cb.append(f'<h2>{esc(st)}（{len(rs)}）</h2><p class="src-list">{esc(_expl[st])}</p>')
        cb.append('<table><thead><tr><th>案例</th><th>国家</th><th>本库时间段</th><th>对照类型</th><th>数据库起始年</th><th>同期其他类型</th></tr></thead><tbody>')
        for r in sorted(rs, key=lambda r: r['our_span'][0]):
            e = entries.get(r['id'], {})
            oth = '；'.join(f'{esc(k)} {"、".join(map(str, v))}' for k, v in r['lv_other_in_span'].items()) or '—'
            cb.append(f'<tr><td><a href="{esc(r["id"])}.html">{esc(e.get("title", r["id"]))}</a></td>'
                      f'<td>{esc(r["country"])}</td><td>{r["our_span"][0]}–{r["our_span"][1]}</td>'
                      f'<td>{esc(r["lv_type"])}</td><td>{"、".join(map(str, r["lv_years"])) or "—"}</td><td>{oth}</td></tr>')
        cb.append('</tbody></table>')
    open(os.path.join(SITE, 'chronology.html'), 'w', encoding='utf-8').write(
        page('年表对照', ''.join(cb), desc='本库危机案例年份与 IMF Laeven–Valencia 系统性危机数据库并列对照'))
    print('生成 chronology.html：%d 个案例对照' % len(_ch['rows']))


'''
assert anchor in s
s=s.replace(anchor,code+anchor,1)
if crlf: s=s.replace('\n','\r\n')
open(p,'w',encoding='utf-8',newline='').write(s)
print('patched crlf=',crlf)
