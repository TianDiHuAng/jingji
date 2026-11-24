# -*- coding: utf-8 -*-
"""续作EK：重写覆盖矩阵页的 Markdown→HTML 转换（合并表格行、首行为 th）。"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

old = '''for line in matrix_html.splitlines():
    if line.startswith('#'):
        mbody.append(f'<h2>{esc(line.lstrip("# "))}</h2>')
    elif line.startswith('|') and '---' not in line:
        cells=[c.strip() for c in line.strip('|').split('|')]
        mbody.append('<table><tr>'+''.join(f'<td>{esc(c)}</td>' for c in cells)+'</tr></table>')
    elif line.startswith('- '):
        mbody.append(f'<p class="src-list">{esc(line[2:])}</p>')
    elif line.strip() and not line.startswith('>'):
        mbody.append(f'<p>{esc(line)}</p>')'''

new = '''_tbl = []          # 收集连续表格行
def _flush():
    if not _tbl:
        return
    rows = []
    for i, cells in enumerate(_tbl):
        tag = 'th' if i == 0 else 'td'
        rows.append('<tr>' + ''.join(f'<{tag}>{esc(c)}</{tag}>' for c in cells) + '</tr>')
    mbody.append('<table>' + ''.join(rows) + '</table>')
    _tbl.clear()

for line in matrix_html.splitlines():
    if line.startswith('#'):
        _flush()
        mbody.append(f'<h2>{esc(line.lstrip("# "))}</h2>')
    elif line.startswith('|') and '---' not in line:
        _tbl.append([c.strip() for c in line.strip('|').split('|')])
    elif line.startswith('- '):
        _flush()
        mbody.append(f'<p class="src-list">{esc(line[2:])}</p>')
    elif line.strip() and not line.startswith('>'):
        _flush()
        mbody.append(f'<p>{esc(line)}</p>')
    else:
        _flush()
_flush()'''

if old in s:
    s = s.replace(old, new, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('矩阵页转换逻辑已重写')
else:
    print('未匹配')
