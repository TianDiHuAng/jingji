# -*- coding: utf-8 -*-
"""续作HV：修正验证页的"独立机构印证"分类——区分「独立撰写」与「不同统计口径」。

问题（round 82 发现）：
原分类把凡引用 fed-* 或 owid-* 且 note 含"印证"的数据都算作"独立机构双源印证"。
但严格说：
  · 美联储历史站（fed-*）是**独立撰写的历史研究**，与维基不共享写作链条 → 算独立。
  · OWID／世界银行（owid-*）的数据**本身汇总自各国官方统计**，而维基的数字往往也源自
    同一批官方统计——两者是"不同加工口径"，**不构成严格独立的信息生产链**。

修正：
  · confirmed  → 仅 fed-*（独立撰写）
  · 新增 statview → owid-* 等（不同统计口径对照），并在页面明确说明其独立性有限
"""
p = 'tools/gen_site.py'
s = open(p, encoding='utf-8').read()

# 1) 拆分类别
old = """        if _is_diff:
            discrepant.append((e, k, has_official))
        elif has_official and any(w in note for w in _confkw):
            confirmed.append((e, k, has_official))       # 独立机构互证"""
new = """        _is_fed = any(str(x).startswith('fed-') for x in srcs)
        _is_stat = any(str(x).startswith(('owid-', 'org-')) for x in srcs)
        if _is_diff:
            discrepant.append((e, k, has_official))
        elif _is_fed and any(w in note for w in _confkw):
            confirmed.append((e, k, has_official))       # 独立撰写（美联储历史研究）
        elif _is_stat and any(w in note for w in _confkw):
            statview.append((e, k, has_official))        # 不同统计口径对照"""
if old in s:
    s = s.replace(old, new, 1)
    print('已拆分 confirmed / statview')

# 2) 初始化 statview 列表
s = s.replace("confirmed, discrepant, crosslang = [], [], []",
              "confirmed, discrepant, crosslang, statview = [], [], [], []")

# 3) 在独立机构印证之后插入新板块
anchor = "vb.append(f'<h2>跨语言维基对照（{len(crosslang)} 条）</h2>')"
block = '''vb.append(f'<h2>不同统计口径对照（{len(statview)} 条）</h2>')
vb.append('<p class="src-list">以下数值由 OWID／世界银行等**统计汇总机构**与维基来源相互对照。'
          '须说明：这些机构的数据本身<span class="em">汇总自各国官方统计</span>，而维基所载数字往往源自同一批官方统计——'
          '两者属<b>不同加工口径</b>（国际可比调整 vs 原始公布），<b>不构成严格独立的信息生产链</b>。'
          '故本板块单列，不与"独立机构印证"合并计数。</p>')
if statview:
    vb.append('<table><tr><th>条目</th><th>数据项</th><th>数值</th><th>年份</th></tr>'
              + ''.join(_kd_row(e, k) for e, k, _ in sorted(statview, key=lambda x: x[0]['id'])) + '</table>')
else:
    vb.append('<p>（暂无）</p>')

''' + anchor
if '不同统计口径对照' not in s:
    s = s.replace(anchor, block, 1)
    print('已插入统计口径对照板块')

# 4) 更新"独立机构印证"的说明
s = s.replace("vb.append('<p class=\"src-list\">以下数值由<b>维基百科之外的独立机构</b>（美联储历史站、世界银行/OWID 等）与维基来源相互印证。</p>')",
              "vb.append('<p class=\"src-list\">以下数值由<b>独立撰写的历史研究机构</b>（如美联储历史站 Federal Reserve History）与维基来源相互印证——'
              "两者不共享写作链条，故可视为独立。</p>')")

# 5) 生成日志
s = s.replace("print('生成 verification.html：独立机构印证 %d 条、跨语言对照 %d 条、差异并列 %d 条、官方来源 %d 个' % (len(confirmed), len(crosslang), len(discrepant), len(_off)))",
              "print('生成 verification.html：独立机构印证 %d 条、统计口径对照 %d 条、跨语言对照 %d 条、差异并列 %d 条、官方来源 %d 个' % (len(confirmed), len(statview), len(crosslang), len(discrepant), len(_off)))")

open(p, 'w', encoding='utf-8').write(s)
print('gen_site.py 已更新')
