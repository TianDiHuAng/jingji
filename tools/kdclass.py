# -*- coding: utf-8 -*-
"""key_data 核实等级分类——**唯一权威判据**，供 gen_site.py 与 check_pages.py 共用。

起因：round 83 首页与验证页用不同代码算同一指标而矛盾；round 88 同类问题在
check_pages.py 与 gen_site.py 之间再现。故把判据抽为共享模块，两处 import 同一函数。

三类：
  confirmed  独立机构印证——独立撰写的机构文献（美联储历史站等）与维基互证
  statview   统计口径对照——汇总各国官方统计的数据源（OWID/世界银行等），与维基常同源
  discrepant 两源存在差异——note 明示差异

排除规则（按顺序）：
  1) note 含差异词 → discrepant
  2) note 明示"不构成独立/原始出处/系转引" → 不计入任何印证类（转引关系不构成双源）
  3) 有独立撰写机构来源且有印证词 → confirmed
  4) 有统计汇总来源且有印证词 → statview
"""

DIFF_KW = ('两源差异', '存在差异', '差异显著', '数据分歧', '分歧较大', '口径不同',
           '不宜直接比较', '相差')
CONF_KW = ('双源印证', '完全一致', '印证')
NOT_INDEP_KW = ('不构成独立', '不构成相互独立', '原始出处', '系转引')

# 机构独立撰写的文献
INDEP_DOC_IDS = {'org-imf-glossary', 'org-bis', 'org-fsb',
                 'org-fed-history', 'org-fed-essay-1907', 'org-fed-essay-greatdep',
                 'org-ecb'}
# 汇总各国官方统计的数据源
STAT_DATA_IDS = {'owid-dataset', 'owid-inflation', 'owid-gdp', 'owid-real-gdp',
                 'owid-unemployment', 'owid-population', 'org-imf-data',
                 'org-worldbank', 'org-hbs-rr-global', 'org-fred', 'org-bea', 'org-ourworldindata'}


def classify(kd):
    """返回 'discrepant' / 'confirmed' / 'statview' / None。"""
    note = kd.get('note') or ''
    srcs = [str(x) for x in (kd.get('sources') or [])]

    if any(w in note for w in DIFF_KW) and '方向与量级一致' not in note:
        return 'discrepant'
    if any(w in note for w in NOT_INDEP_KW):
        return None
    if not any(w in note for w in CONF_KW):
        return None
    if any(s.startswith('fed-') for s in srcs) or any(s in INDEP_DOC_IDS for s in srcs):
        return 'confirmed'
    if any(s.startswith('owid-') for s in srcs) or any(s in STAT_DATA_IDS for s in srcs):
        return 'statview'
    return None


def counts(entries):
    """统计全站三类条数。entries 可为 dict 或 list。"""
    vals = entries.values() if isinstance(entries, dict) else entries
    c = {'confirmed': 0, 'statview': 0, 'discrepant': 0}
    for e in vals:
        for k in (e.get('key_data') or []):
            r = classify(k)
            if r:
                c[r] += 1
    return c


def is_single(kd):
    """单一来源判据（唯一口径）：该行 sources 去重后少于 2 个。
    不看 note 措辞——round 297 发现按 note 中"单一来源待核实"字样计数会漏掉
    "单源待核实""待第二来源核实"等写法及 OWID/IMF 对照行，README 因此少计。"""
    return len(set(kd.get('sources') or [])) < 2
