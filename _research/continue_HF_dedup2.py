# -*- coding: utf-8 -*-
"""续作HF：恢复 sources.json 并用**通用重定向**重做去重（覆盖全部 7 个引用字段）。

教训（第 6 次工具缺陷）：上一版只处理了 sources／key_data／policy_response／schools[src]，
漏掉 causal_chain[].sources 与 timeline[].sources，导致 54 处 R4 错误。

字段全清单（实测）：
  .sources / .key_data[].sources / .policy_response[].sources
  .schools[].sources / .schools[].src
  .causal_chain[].sources / .timeline[].sources
"""
import glob
import json
import subprocess
from collections import Counter, defaultdict

# 1) 从 git 恢复 sources.json（去重前的版本）
raw = subprocess.run(['git', 'show', 'HEAD:data/sources.json'],
                     capture_output=True, text=True, encoding='utf-8')
if raw.returncode == 0 and raw.stdout.strip():
    open('data/sources.json', 'w', encoding='utf-8').write(raw.stdout)
    print('已从 git 恢复 sources.json')
else:
    print('恢复失败，沿用当前文件')

SP = 'data/sources.json'
sj = json.load(open(SP, encoding='utf-8'))
srcs = sj['sources']
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

# 2) 统计引用（覆盖全部字段）
use = Counter()


def walk_collect(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'sources' and isinstance(v, list):
                for x in v:
                    if isinstance(x, str):
                        use[x] += 1
            elif k == 'src' and isinstance(v, str):
                use[v] += 1
            else:
                walk_collect(v)
    elif isinstance(o, list):
        for it in o:
            walk_collect(it)


for e in es:
    walk_collect(e)

# 3) 分组
groups = defaultdict(list)
for s in srcs:
    groups[s['url'].rstrip('/').lower()].append(s['id'])

redirect = {}
for url, ids in groups.items():
    if len(ids) < 2:
        continue
    keep = sorted(ids, key=lambda i: (-use[i], len(i), i))[0]
    for i in ids:
        if i != keep:
            redirect[i] = keep
print('待合并: %d 个来源' % len(redirect))

# 4) 通用重定向
def remap_obj(o):
    """递归改写 sources 列表与 src 字符串。返回是否有改动。"""
    changed = False
    if isinstance(o, dict):
        for k, v in list(o.items()):
            if k == 'sources' and isinstance(v, list):
                out, seen = [], set()
                for x in v:
                    y = redirect.get(x, x) if isinstance(x, str) else x
                    if y not in seen:
                        seen.add(y)
                        out.append(y)
                if out != v:
                    o[k] = out
                    changed = True
            elif k == 'src' and isinstance(v, str) and v in redirect:
                o[k] = redirect[v]
                changed = True
            else:
                if remap_obj(v):
                    changed = True
    elif isinstance(o, list):
        for it in o:
            if remap_obj(it):
                changed = True
    return changed


n_ent = 0
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if remap_obj(d):
        n_ent += 1
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('重定向条目: %d' % n_ent)

# 5) 删除被合并来源
before = len(sj['sources'])
sj['sources'] = [s for s in sj['sources'] if s['id'] not in redirect]
sj['count'] = len(sj['sources'])
json.dump(sj, open(SP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源库: %d → %d' % (before, sj['count']))
