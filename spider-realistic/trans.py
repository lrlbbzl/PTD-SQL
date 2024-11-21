import json

# x = json.load(open('test_data.json', 'r'))
# y = json.load(open('spider-realistic.json', 'r'))

# mp = {}
# for idx, a in enumerate(x):
#     mp.update({a['gold'] : idx})

# ls = []
# for b in y:
#     temp = x[mp[b['query']]]
#     temp['question'] = b['question']
#     ls.append(temp)
# json.dump(ls, open('test_realistic.json', 'w'))

import os
dir = '../spider-dev/llama2'
name = ['combination', 'complex', 'filter', 'simple']
target = [os.path.join(os.path.join(dir, na), '{}.json'.format(na)) for na in name]
mp = {}
for na, f in zip(name, target):
    x = json.load(open(f, 'r'))
    for xx in x:
        mp.update({xx['gold'] : na})
ans = {x : [] for x in name}
for x in json.load(open('test_realistic.json', 'r')):
    if x['gold'] in mp:
        t = mp[x['gold']]
        ans[t].append(x)
    else:
        print(x['gold'])

for na in name:
    dir = './{}'.format(na)
    if not os.path.exists(dir):
        os.makedirs(dir)
    file = './{}/{}.json'.format(na, na)
    print('{}:{}'.format(na, len(ans[na])))
    json.dump(ans[na], open(file, 'w'))