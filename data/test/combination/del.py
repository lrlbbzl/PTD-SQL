import json

x = json.load(open('combination.json', 'r'))
q = [p['gold'] for p in x]

y = json.load(open('../../../classification/combination/auto_select/fail_examples.json', 'r'))
f = [p['g_str'][0] for p in y]

for ls in f:
    if ls not in q:
        print(ls)