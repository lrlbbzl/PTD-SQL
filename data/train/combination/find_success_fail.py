import json

x = json.load(open('count_samples.json', 'r'))

y = json.load(open('success_examples.json', 'r'))
ys = []

z = json.load(open('fail_examples.json', 'r'))
zs = []

idx, idx1, idx2 = 0, 0, 0

while idx < len(x) and idx1 < len(y):
    if x[idx]['gold'] == y[idx1]['g_str'][0] and x[idx]['predict'] == y[idx1]['p_str']:
        ys.append(x[idx])
        idx += 1
        idx1 += 1
    else:
        idx += 1

idx = 0
while idx < len(x) and idx2 < len(z):
    if x[idx]['gold'] == z[idx2]['g_str'][0] and x[idx]['predict'] == z[idx2]['p_str']:
        temp = x[idx]
        temp['predict'] = ""
        temp['reasoning'] = ""
        zs.append(temp)
        idx += 1
        idx2 += 1
    else:
        idx += 1

json.dump(ys, open('true_samples.json', 'w'))
json.dump(zs, open('false_samples.json', 'w'))