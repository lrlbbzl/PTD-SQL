import json

ty = ['combination', 'complex', 'filter', 'simple']
mp = {
    'combination' : 0,
    'complex' : 1,
    'filter' : 2,
    'simple' : 3
}

sav = {}

def type_class(x : str):
    ls = []
    for t in ['intersect', 'union', 'except']:
        if t in x.lower():
            ls.append(1)
            break
    for t in ['order by', 'group by']:
        if t in x.lower():
            ls.append(0)
            break
    for t in ['where']:
        if t in x.lower():
            ls.append(2)
    if len(ls) == 0:
        ls.append(3)
    return tuple(ls)

for k, v in mp.items():
    if k == 'simple':
        path = '/root/text2sql/spider-dev/llama2/simple/gpt-4/fix/predict.json'
    else:
        path = '/root/text2sql/spider-dev/llama2/{}/gpt-4/ada_overlap/predict.json'.format(k)
    data = json.load(open(path, 'r'))
    for d in data:
        ls = type_class(d['gold'])
        if ls not in sav:
            sav.update({ls : dict()})
        if v not in sav[ls]:
            sav[ls].update({v : []})
        sav[ls][v].append(d)
for k, v in sav.items():
    for p, q in v.items():
        json.dump(q, open('{}-{}.json'.format(k, p), 'w'))