import json, os, glob, re, urllib.parse
S = {s['id']: s for s in json.load(open('data/sources.json', encoding='utf-8'))['sources']}
def slug_of(url):
    m = re.search(r'wikipedia\.org/wiki/([^#?]+)', url or '')
    return urllib.parse.unquote(m.group(1)).replace(' ', '_').lower() if m else None
rows = []
for f in sorted(glob.glob('_research/wiki_full/*.txt')):
    i = os.path.basename(f)[:-4]
    ep = 'data/entries/' + i + '.json'
    if not os.path.exists(ep):
        continue
    d = json.load(open(ep, encoding='utf-8'))
    cand = {slug_of(S[s].get('url')) for s in d.get('sources', []) if s in S and s.startswith('w-en-')}
    cand.discard(None)
    sp = f[:-4] + '.slug'
    slug = open(sp, encoding='utf-8').read().strip().lower() if os.path.exists(sp) else ''
    if not slug:
        rows.append(('NOSLUG', i, '', sorted(cand)))
    elif slug not in cand:
        rows.append(('MISMATCH', i, slug, sorted(cand)))
for r in rows:
    print(*r, sep=' | ')
print('total flagged', len(rows))
