import json, glob, re, os, sys
a, b = int(sys.argv[1]), int(sys.argv[2])
r = []
for f in glob.glob('data/entries/*.json'):
    s = open(f, encoding='utf-8').read()
    n = len(re.findall('待核实', s))
    i = os.path.basename(f)[:-5]
    if n and os.path.exists('_research/wiki_full/' + i + '.txt'):
        r.append((n, i))
r.sort(reverse=True)
print('total', len(r))
pat = re.compile(r'.{0,70}(\$[0-9.,]+ ?(?:b|m|tr)illion|£[0-9.,]+ ?(?:b|m)illion|[0-9.]+ ?%|per cent).{0,40}')
for n, i in r[a:b]:
    d = json.load(open('data/entries/' + i + '.json', encoding='utf-8'))
    print('==', i, d['sources'])
    for k in d.get('key_data', []):
        print(' KD', k.get('label'), k.get('value'))
    t = open('_research/wiki_full/' + i + '.txt', encoding='utf-8').read()
    print(' H', t[:80].replace('\n', ' '))
    for m in list(pat.finditer(t))[:6]:
        print('  ', m.group(0).replace('\n', ' '))
