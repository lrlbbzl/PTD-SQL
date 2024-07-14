import json

dic = {}

x = json.load(open("./predictions.json", 'r'))
# y = json.load(open('../group_type_data.json', 'r')) # set_operations
# z = json.load(open('../../data/test/complex/complex.json'))

# gt = [p['question'] for p in z]
# dif = list(set(gt) - set(x['Set operation']))
# # dif = list(set(y['Set operations']) - set(x['Set operation']))
# print('\n'.join(dif))
# print(len(dif))

for p in x:
    if p['predict'] not in dic:
        dic.update({p['predict'] : []})
    else:
        dic[p['predict']].append(p['query'])
json.dump(dic, open('group_type_data.json', 'w'))

# for k, v in x.items():
#     print('{}: {}'.format(k, len(v)))