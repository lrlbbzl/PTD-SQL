import json

# x = json.load(open('test_data.json', 'r'))

# y = open('test_data.txt', 'w')

# ls = []

# for idx, a in enumerate(x):
#     ls.append(a['question'])
# y.writelines('\n'.join(ls))
# y.close()

# x = json.load(open('test_type.json', 'r'))

# ls = {}

# for k, v in x.items():
#     if v not in ls:
#         ls.update({v : []})
#     ls[v].append(k)
# json.dump(ls, open('group_type_data.json', 'w'))

x = json.load(open('group_type_data.json', 'r'))['Combination operation']
y = json.load(open('combination.json', 'r'))

y = [p['question'] for p in y]

ls = list(set(x) - set(y))
print(len(ls))
for a in ls:
    print(a)