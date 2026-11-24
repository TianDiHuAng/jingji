# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
comp = sum(1 for e in es if e.get('comparison'))
pages = len(glob.glob('site/*.html'))

# 未引用来源（覆盖全部 7 字段）
used = set()


def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'sources' and isinstance(v, list):
                used.update(x for x in v if isinstance(x, str))
            elif k == 'src' and isinstance(v, str):
                used.add(v)
            else:
                walk(v)
    elif isinstance(o, list):
        for it in o:
            walk(it)


for e in es:
    walk(e)
src_ids = {s['id'] for s in srcs}
unused = sorted(src_ids - used)

note = (
    '维基第57轮可用。HE-HF：**合并 29 组重复来源，并记录第 6 次工具缺陷**。'
    '①**发现来源库冗余**：729 条来源中有 **29 组指向同一 URL 却注册了两个 id**——'
    '如 `w-en-argentine-economic-crisis-1999-2002` 与 `w-en-argentine-economic-crisis`、'
    '`w-en-mississippi-company` 与 `w-en-john-law-company`、'
    '`w-en-eurozone-crisis` 与 `w-en-euro-area-crisis` 等。'
    '②第一版重定向脚本只处理 4 个字段，**漏掉 `causal_chain[].sources` 与 `timeline[].sources`**，'
    '导致 **54 处 R4 错误**。'
    '③**实测枚举出全部 7 个引用字段**：`.sources`／`.key_data[].sources`／'
    '`.policy_response[].sources`／`.schools[].sources`／`.schools[].src`／'
    '`.causal_chain[].sources`／`.timeline[].sources`。'
    '④改用**递归遍历 `remap_obj`** 改写任意深度的 `sources`／`src`，不再依赖手写字段列表；'
    '从 git 恢复后重做，最终 0 error。'
    '⑤来源库 **729 → 700** 条，重定向 28 个条目。'
    '⑥**第 6 次工具缺陷记入 BLOCKERS**——与第 5 次是同一错误的复发：'
    '**写脚本前应先枚举，而不是凭记忆**。'
    '当前：条目 ' + str(len(es)) + '、来源 ' + str(len(srcs)) + '（未引用 ' + str(len(unused)) + '）、'
    '页面 ' + str(pages) + '、key_data ' + str(tk) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HE-HF', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 28, 'reviewed': 729, 'fixed': 29,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（来源 729→700）',
    'spot_check': '合并 29 组重复来源；第6次工具缺陷已记录',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **来源：732**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
s = s.replace('- **来源：729**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
add = '''- **维基百科第 57 轮可用（round 76）**。**合并 29 组重复来源，并记录第 6 次工具缺陷**。
- **① 发现来源库冗余**：729 条来源中 **29 组指向同一 URL 却注册了两个 id**：

  | 重复对（举例） |
  |---|
  | `w-en-argentine-economic-crisis-1999-2002` ═ `w-en-argentine-economic-crisis` |
  | `w-en-mississippi-company` ═ `w-en-john-law-company` |
  | `w-en-eurozone-crisis` ═ `w-en-euro-area-crisis` |
  | `w-en-bengal-bubble-of-1769` ═ `w-en-bengal-bubble-1769` |
  | `w-en-shanghai-rubber-stock-market-crisis` ═ `w-en-shanghai-rubber-1910` |

- **② 第 6 次工具缺陷**：第一版重定向脚本只处理 4 个字段，**漏掉 `causal_chain[].sources` 与 `timeline[].sources`**，导致 **54 处 R4 错误**。
- **③ 实测枚举出全部 7 个引用字段**：

  `.sources`／`.key_data[].sources`／`.policy_response[].sources`／`.schools[].sources`／`.schools[].src`／`.causal_chain[].sources`／`.timeline[].sources`

- **④ 改用递归遍历 `remap_obj`** 改写任意深度的 `sources`／`src`，不再依赖手写字段列表；从 git 恢复后重做，最终 **0 error**。
- 来源库 **729 → 700** 条，重定向 28 个条目。
- 这与第 5 次是**同一错误的复发**——写脚本前应先枚举，而不是凭记忆。
- 十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HB-HD｜2026-11-24｜状态：624条；合并重复条目，修复孤儿页面累积**',
              '**续作HE-HF｜2026-11-24｜状态：624条；合并29组重复来源，来源库729→700**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 来源', len(srcs), '| 未引用', len(unused))
