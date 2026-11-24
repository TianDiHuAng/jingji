# -*- coding: utf-8 -*-
"""
tools/check.py — 《经济史与金融危机案例库》质量守门员
数据层 → 校验层 → 渲染层架构中的机器校验环节。

校验规则 R1–R15：
 R1  条目必填字段完整
 R2  id 仅 a-z0-9-（R16 换域适配）
 R3  层级合法（L1/L2/L3）且与 tier 目标关系一致
 R4  来源 id 必须在 sources.json 中定义
 R5  关键事实的 sources 必须 verified=true
 R6  双源规则：关键数据≥2个 verified 来源，否则 needs_verification=true 且 pending 非空
 R7  无重复条目（同 id / 同标题）
 R8  时间线年份升序
 R9  数字合法：value 可解析、unit 非空、year 合理、可比价声明
 R10 SVG 合法：XML 可解析、viewBox 必填、元素白名单、无脚本、元素不出界
 R11 内部链接可达（related 指向的条目文件存在；未写作者降级为 warning）
 R12 coverage.json 与条目文件一致
 R13 同一数据全站一致（同名指标在多个页面数值一致）
 R14 分层写作顺序：L2/L3 条目存在时 L1 骨架应已覆盖全部条目
 R15 needs_verification 与 pending_notes 联动

用法：
 python tools/check.py                 # 全量校验
 python tools/check.py --file data/entries/xxx.json   # 单条校验
退出码：0=通过，1=有 error
"""
import json, sys, os, re, glob, xml.etree.ElementTree as ET
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(ROOT, 'data', 'sources.json')
COV_PATH = os.path.join(ROOT, 'coverage.json')
ENT_DIR = os.path.join(ROOT, 'data', 'entries')

errors = []
warnings = []

def err(rule, where, msg):
    errors.append(f'[{rule}] {where}: {msg}')

def warn(rule, where, msg):
    warnings.append(f'[W{rule}] {where}: {msg}')

def load_json(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        err('R1', path, f'JSON 解析失败: {e}')
        return None

# ---------- 加载全局数据 ----------
src_data = load_json(SRC_PATH)
sources = {}
if src_data:
    for s in src_data.get('sources', []):
        sources[s.get('id')] = s
cov = load_json(COV_PATH)
cov_ids = set()
if cov:
    cov_ids = {e['id'] for e in cov.get('entries', [])}

TYPE_VOCAB = {'权威百科', '学术著作', '官方机构', '统计数据库'}
REQUIRED = ['id','title','level','tier','unit','period','region','crisis_type',
            'one_line','overview','sources']
VALID_LEVEL = {'L1','L2','L3'}
VALID_TIER = {'核心','重要','补充'}
TIER_TARGET = {'核心':'L3','重要':'L2','补充':'L1'}
SVG_ALLOWED = {'svg','g','text','tspan','line','rect','circle','ellipse','path','polyline',
               'polygon','defs','marker','title','desc','linearGradient','stop'}
NUM_RE = re.compile(r'^\s*[-+]?\d[\d,]*(\.\d+)?\s*(%|％|亿|万|千|人|年|月|日|次|倍|美元|欧元|英镑|比索|马克|个百分点|pp)?\s*$')

def check_sources_refs(ids, where):
    """R4/R5：来源合法且 verified"""
    for sid in ids:
        if sid not in sources:
            err('R4', where, f'来源 id "{sid}" 未在 sources.json 中定义')
        elif not sources[sid].get('verified'):
            warn('R5', where, f'来源 "{sid}" verified=false（待核实），不可作为关键事实唯一依据')

def check_svg(svg, where):
    """R10：SVG 合法性 + 元素不出界"""
    if not svg or not svg.strip():
        return
    try:
        root = ET.fromstring(svg)
    except Exception as e:
        err('R10', where, f'SVG XML 解析失败: {e}')
        return
    if root.tag.split('}')[-1] != 'svg':
        err('R10', where, 'SVG 根元素不是 <svg>')
    vb = root.get('viewBox')
    if not vb:
        err('R10', where, 'SVG 缺少 viewBox')
        return
    try:
        parts = [float(x) for x in re.split(r'[ ,]+', vb.strip())]
        if len(parts) != 4:
            raise ValueError('viewBox 必须4个数')
        vx, vy, vw, vh = parts
    except Exception as e:
        err('R10', where, f'viewBox 非法: {e}')
        return
    def walk(node, depth=0):
        if depth > 12: return
        tag = node.tag.split('}')[-1]
        if tag not in SVG_ALLOWED:
            err('R10', where, f'SVG 含非白名单元素 <{tag}>')
        if tag == 'script':
            err('R10', where, 'SVG 含 <script>')
        for k, v in node.attrib.items():
            if k.lower().startswith('on'):
                err('R10', where, f'SVG 含事件属性 {k}')
        # 元素出界检测（仅检测显式坐标属性）
        xs, ys = [], []
        for attr in ('x','x1','x2','cx'):
            if attr in node.attrib:
                try: xs.append(float(node.attrib[attr]))
                except: pass
        for attr in ('y','y1','y2','cy'):
            if attr in node.attrib:
                try: ys.append(float(node.attrib[attr]))
                except: pass
        # rect/circle 考虑宽高半径
        if tag == 'rect':
            try:
                xs.append(float(node.get('x',0))+float(node.get('width',0)))
                ys.append(float(node.get('y',0))+float(node.get('height',0)))
            except: pass
        if tag == 'circle':
            try:
                r=float(node.get('r',0)); cx=float(node.get('cx',0)); cy=float(node.get('cy',0))
                xs += [cx-r,cx+r]; ys += [cy-r,cy+r]
            except: pass
        tol = 2.0
        for x in xs:
            if x < vx-tol or x > vx+vw+tol:
                err('R10', where, f'SVG 元素 x={x} 超出 viewBox[{vx},{vx+vw}]')
        for y in ys:
            if y < vy-tol or y > vy+vh+tol:
                err('R10', where, f'SVG 元素 y={y} 超出 viewBox[{vy},{vy+vh}]')
        for ch in node:
            walk(ch, depth+1)
    walk(root)

def check_entry(e, path, all_ids=None):
    where = os.path.basename(path)
    # R1 必填
    for k in REQUIRED:
        v = e.get(k)
        if v is None or (isinstance(v,str) and not v.strip()) or (isinstance(v,list) and len(v)==0):
            err('R1', where, f'必填字段 "{k}" 为空或缺失')
    eid = e.get('id','')
    # R2 id 格式
    if eid and not re.fullmatch(r'[a-z0-9-]+', eid):
        err('R2', where, f'id "{eid}" 非法，只允许 a-z0-9-')
    # R3 层级
    if e.get('level') not in VALID_LEVEL:
        err('R3', where, f'level "{e.get("level")}" 非法')
    if e.get('tier') not in VALID_TIER:
        err('R3', where, f'tier "{e.get("tier")}" 非法')
    # 来源引用
    check_sources_refs(e.get('sources',[]), where)
    # R15 联动
    if e.get('needs_verification') and not e.get('pending_notes','').strip():
        err('R15', where, 'needs_verification=true 但 pending_notes 为空')
    if e.get('pending_notes','').strip() and not e.get('needs_verification'):
        warn('R15', where, '有 pending_notes 但 needs_verification=false，请确认')
    # R8 时间线升序
    tl = e.get('timeline',[])
    yrs = [t.get('year') for t in tl if isinstance(t.get('year'),(int,float))]
    if yrs != sorted(yrs):
        err('R8', where, f'timeline 年份非升序: {yrs}')
    # R9 数字合法 + R6 双源 + R5 verified
    for d in e.get('key_data',[]):
        val = d.get('value')
        if not isinstance(val,(int,float)):
            err('R9', where, f'数据 "{d.get("label","?")}" value 非数值: {val!r}')
        if not d.get('unit','').strip():
            err('R9', where, f'数据 "{d.get("label","?")}" 缺 unit')
        y = d.get('year')
        if not isinstance(y,(int,float)) or y < -5000 or y > 2026:
            err('R9', where, f'数据 "{d.get("label","?")}" year 非法: {y}')
        if 'comparable_price' not in d:
            warn('R9', where, f'数据 "{d.get("label","?")}" 未声明 comparable_price（是否可比价）')
        ds = [s for s in d.get('sources',[]) if s in sources and sources[s].get('verified')]
        if len(ds) < 2 and not e.get('needs_verification'):
            err('R6', where, f'数据 "{d.get("label","?")}" 仅有 {len(ds)} 个 verified 来源，需≥2或整条标待核实')
        check_sources_refs(d.get('sources',[]), where)
    # 因果链每步来源
    for i, st in enumerate(e.get('causal_chain',[])):
        check_sources_refs(st.get('sources',[]), f'{where} causal_chain[{i}]')
    # R10 SVG
    check_svg(e.get('svg',''), where)
    # R10b deep_svg（L3 机制图）同样须校验
    _dsvg = e.get('deep_svg')
    if _dsvg:
        check_svg(_dsvg, where + ' [deep_svg]')
    # R11 内部链接
    if all_ids is not None:
        for rid in e.get('related',[]):
            if rid not in all_ids:
                warn('R11', where, f'related 指向 "{rid}"，该文件尚不存在（分批写作中）')

# ---------- 主流程 ----------
def main():
    single = None
    if '--file' in sys.argv:
        i = sys.argv.index('--file')
        if i+1 < len(sys.argv):
            single = sys.argv[i+1]
    files = [single] if single else sorted(glob.glob(os.path.join(ENT_DIR,'*.json')))
    if not files:
        print('（无条目文件，仅校验全局数据）')
    entries = []
    seen_ids = set(); seen_titles = set()
    all_ids = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(ENT_DIR,'*.json'))}
    for f in files:
        e = load_json(f)
        if not e: continue
        entries.append(e)
        where = os.path.basename(f)
        # R7 去重
        eid = e.get('id','')
        if eid in seen_ids:
            err('R7', where, f'重复 id "{eid}"')
        seen_ids.add(eid)
        title = e.get('title','')
        if title in seen_titles:
            err('R7', where, f'重复标题 "{title}"')
        seen_titles.add(title)
        check_entry(e, f, all_ids)
    # R12 coverage 一致性
    if cov and not single:
        for cid in sorted(cov_ids - all_ids):
            warn('R12', 'coverage.json', f'条目 "{cid}" 在 scope 中但尚无条目文件')
        for fid in sorted(all_ids - cov_ids):
            err('R12', fid, '条目文件不在 coverage.json/scope 中')
    # R13 全站数据一致性
    metric = defaultdict(set)
    for e in entries:
        for d in e.get('key_data',[]):
            label = d.get('label','')
            if label:
                metric[label].add((d.get('value'), d.get('unit')))
    for label, vals in metric.items():
        if len(vals) > 1:
            # 同 label 出现不同数值——需看是否为不同年份/口径，降级为 warning 供人工确认
            warn('R13', '全站', f'指标 "{label}" 出现多个数值/单位: {sorted(vals, key=str)}')
    # R17 来源 type 词汇表
    for _s in (src_data or {}).get('sources', []):
        if _s.get('type') not in TYPE_VOCAB:
            err('R17', _s.get('id','?'), 'type "%s" 不在词汇表（%s）'
                % (_s.get('type'), '/'.join(sorted(TYPE_VOCAB))))
    # R18 来源 link_ok 不得为空
    for _s in (src_data or {}).get('sources', []):
        if _s.get('link_ok') is None:
            err('R18', _s.get('id', '?'), 'link_ok 未设置（须为 true/false）')
    # R4b 嵌套字段的来源 id 也必须存在（timeline/schools/policy_response/key_data）
    for _e in entries:
        for _f, _label in (('timeline', 'timeline'), ('schools', 'schools'),
                           ('policy_response', 'policy_response'), ('key_data', 'key_data')):
            for _i, _it in enumerate(_e.get(_f) or []):
                if not isinstance(_it, dict):
                    continue
                for _sid in (_it.get('sources') or []):
                    if _sid not in sources:
                        err('R4', '%s.%s[%d]' % (_e.get('id', '?'), _label, _i),
                            '来源 id "%s" 未在 sources.json 中定义' % _sid)
    # R19 结构化内容字段必须逐条带来源
    for _e in entries:
        _wid = _e.get('id', '?')
        for _f in ('timeline', 'schools', 'policy_response'):
            for _i, _item in enumerate(_e.get(_f) or []):
                if not (_item.get('sources') if isinstance(_item, dict) else None):
                    err('R19', _wid, '%s[%d] 缺 sources' % (_f, _i))
    # R20 U1（早期—17世纪）不适用"全球"标签
    for _e in entries:
        if str(_e.get('unit', '')).startswith('U1') and _e.get('region') == '全球':
            err('R20', _e.get('id', '?'), 'U1 时期尚无全球金融体系，不应标 region=全球')
    # R21 overview 须以中文为主（英文占比不得 >45%）
    import re as _re21
    for _e in entries:
        _ov = _e.get('overview') or ''
        _zh = len(_re21.findall(r'[\u4e00-\u9fff]', _ov))
        _en = len(_re21.findall(r'[A-Za-z]', _ov))
        if _zh + _en > 40:
            _r21 = _en / (_zh + _en)
            if _r21 > 0.45:
                err('R21', _e.get('id', '?'),
                    'overview 英文占比 %.0f%%（须 ≤45%%）' % (_r21 * 100))
    # R14 分层顺序
    if not single and entries:
        lv = Counter(e.get('level') for e in entries)
        if (lv['L2']+lv['L3'])>0 and len(entries) < len(cov_ids):
            warn('R14', '全局', f'已有 L2/L3 条目但仅 {len(entries)}/{len(cov_ids)} 条有文件；请确认 L1 骨架已覆盖全部后再深写')

    print('='*60)
    print(f'校验条目: {len(entries)} | 来源库: {len(sources)} 条')
    print(f'ERRORS: {len(errors)} | WARNINGS: {len(warnings)}')
    print('='*60)
    for x in errors[:80]: print('E', x)
    if len(errors)>80: print(f'... 另有 {len(errors)-80} 条 error')
    for x in warnings[:30]: print('W', x)
    if len(warnings)>30: print(f'... 另有 {len(warnings)-30} 条 warning')
    if errors:
        print('\n结果：未通过（存在 error）')
        sys.exit(1)
    else:
        print('\n结果：通过（0 error）')
        sys.exit(0)

if __name__ == '__main__':
    main()
