# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['count'] if False else
           json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
tl = sum(len(e.get('timeline', [])) for e in es)
sc = sum(len(e.get('schools', [])) for e in es)

note = (
    '维基第47轮可用。GK：**新增第 9 个检查工具 tools/check_docs.py**，'
    '并借此**发现并修复了一处滞后 40 轮的文档错误**。'
    '①工具功能：核对文档中"最新一条现状/当前表述"的数字与实际数据是否一致。'
    '初版把历史轮次的"现状"也纳入比对，产生了 20+ 条假报警（那些是当时的真实记录），'
    '改为只核对**最后一条**后通过。'
    '②**修复的问题**：PROGRESS.md 顶部的"当前状态"区块仍停留在**轮次 25**——'
    '声称"当前轮次 25／SATURATED=true／总计 135 条、来源 212 条"，'
    '而实际已是 **625 条／732 来源／639 页**，**滞后整 40 轮**。'
    '已重写为与真实数据一致，并标注"以 check_docs.py 核对"。'
    '③README 登记第 9 道检查。'
    '当前：' + str(len(es)) + ' 条、来源 ' + str(srcn) + '、key_data ' + str(tk) + '/' +
    str(tl) + '/' + str(sc) + '（key_data/timeline/schools）、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GK', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 1, 'fixed': 1,
    'sources_total': srcn,
    'check_result': 'PASS; 9 道检查全绿（新增 check_docs）',
    'spot_check': '修复 PROGRESS.md 顶部滞后 40 轮的当前状态',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('## 轮次记录', '''## 轮次记录

- **维基百科第 47 轮可用**。**新增第 9 个检查工具 `tools/check_docs.py`**，并借此发现一处**滞后 40 轮的文档错误**。
- **工具功能**：核对文档中"最新一条现状表述"的数字与实际数据是否一致。初版把历史轮次的"现状"也纳入比对，产生 20+ 条**假报警**（那些是当时的真实记录）；改为只核对最后一条后通过。
- **修复的问题**：`PROGRESS.md` 顶部的"当前状态"区块仍停留在**轮次 25**——声称"当前轮次 25／SATURATED=true／总计 135 条、来源 212 条"，而实际已是 **625 条／732 来源／639 页**，**滞后整 40 轮**。
  - 已重写为自动与真实数据一致，并标注"以 `check_docs.py` 核对"
  - 这印证了 round 65 的教训：**验证机制此前只检查条目内容，不检查项目文档本身**
- README 登记第 9 道检查。
- 九道检查：check／check_links／check_quality／check_kd／check_polnum／check_sources／check_body_num／**check_docs**。
''', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GG-GJ｜2026-11-24｜状态：625条；13个薄弱条目已补内容**',
              '**续作GK｜2026-11-24｜状态：625条；新增 check_docs，修复滞后40轮的文档状态**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
