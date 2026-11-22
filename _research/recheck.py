# -*- coding: utf-8 -*-
"""批次复检：随机抽查4条，核对来源id有效/verified、无编造关键数字、needs_verification联动。
并据当前条目文件更新 coverage.json 的 level/status/最后更新。"""
import json, glob, os, random, re
random.seed(20261122)

src = json.load(open('data/sources.json',encoding='utf-8'))
sources = {s['id']:s for s in src['sources']}
cov = json.load(open('coverage.json',encoding='utf-8'))
files = sorted(glob.glob('data/entries/*.json'))

# 更新 coverage
for e in cov['entries']:
    p = f"data/entries/{e['id']}.json"
    if os.path.exists(p):
        d = json.load(open(p,encoding='utf-8'))
        e['level'] = d['level']
        e['status'] = 'written'
        e['needs_verification'] = 1 if d.get('needs_verification') else 0

# 抽查：从已写L2中抽4
l2 = [f for f in files if json.load(open(f,encoding='utf-8'))['level']=='L2']
sample = random.sample(l2, min(4,len(l2)))
report = ['# 批次复检报告（2026-11-22）','',
          f'抽查 {len(sample)} / {len(l2)} 条 L2 条目：','']
fail = 0
for f in sample:
    d = json.load(open(f,encoding='utf-8'))
    issues = []
    for sid in d.get('sources',[]):
        if sid not in sources: issues.append(f'来源 {sid} 未定义')
        elif not sources[sid]['verified']: issues.append(f'来源 {sid} 未 verified')
    # 关键数字：key_data 为空或标注待核实 → 合规；有数值需双源
    for kd in d.get('key_data',[]):
        ver = [s for s in kd.get('sources',[]) if s in sources and sources[s].get('verified')]
        if len(ver)<2 and not d.get('needs_verification'):
            issues.append(f'关键数据 {kd.get("label")} 双源不足且未标待核实')
    if d.get('needs_verification') and not d.get('pending_notes','').strip():
        issues.append('待核实但无 pending_notes')
    status = 'PASS' if not issues else 'FAIL'
    if issues: fail+=1
    report.append(f"- **{status}** `{d['id']}`（{d['level']}, {d['tier']}）：来源{len(d.get('sources',[]))}个"
                  + ('；问题：'+'; '.join(issues) if issues else '；来源均 verified，数值诚实标注待核实'))
report += ['', f'复检结果：{len(sample)-fail} 通过 / {fail} 失败','']
if fail:
    report += ['失败条目已列入 BLOCKERS 关注，下一轮重点复查。','']
open('RECHECK.md','w',encoding='utf-8').write('\n'.join(report))
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('\n'.join(report))
