import json

# prompt = """## Tables:
# {}

# ## Foreign_keys:
# {}

# ## Query:
# {}

# SQL query: {}"""
# x = json.load(open('../train_data.json', 'r'))
# while True:
#     idx = int(input())
#     s = x[idx]
#     a = s['fields'].strip()
#     b = s['foreign_keys'].strip()
#     b = b[len('Foreign_keys = ') :]
#     c = s['question']
#     print(prompt.format(a, b, c, s['gold']))
#     print()

import json
import random
# x = json.load(open('filter_samples.json', 'r'))
# qs = [q['question'] for q in x]

# how_many = []

# for p in x:
#     if 'how many' in p['question'].lower() and 'count' in p['gold'].lower():
#         how_many.append(p['question'])

# not_in = []
# for p in x:
#     if ' where ' in p['gold'].lower() and ' not in ' in p['gold'].lower():
#         not_in.append(p['question'])

# compare = []
# for p in x:
#     if ' where ' in p['gold'].lower() and ('>=' in p['gold'] or '<=' in p['gold'] or '>' in p['gold'] or '<' in p['gold'] or '!=' in p['gold']):
#         compare.append(p['question'])

# both = []
# for p in x:
#     if ' where ' in p['gold'].lower() and ' and ' in p['gold'].lower():
#         both.append(p['question'])
# how_many_sel = random.sample(how_many, 100)
# not_in_sel = random.sample(not_in, 100)
# compare_sel = random.sample(compare, 100)
# both_sel = random.sample(both, 100)
# tot = set(how_many_sel).union(set(not_in_sel)).union(set(compare_sel)).union(set(both_sel))

# tot = list(tot)
# remain = set(qs).difference(set(tot))
# remain_sel = random.sample(remain, 100)
# tot = list(set(tot) | set(remain_sel))
# print(len(tot))
# samples = [p for p in x if p['question'] in tot ]
# json.dump(samples, open('filter_selected.json', 'w'))

# x = json.load(open('predict.json', 'r'))
# y = json.load(open('success_examples.json', 'r'))

# ls = []
# idx1, idx2 = 0, 0
# while idx1 < len(x) and idx2 < len(y):
#     if x[idx1]['gold'] == y[idx2]['g_str'][0] and x[idx1]['predict'] == y[idx2]['p_str']:
#         temp = x[idx1]
#         temp.update({'predict' : temp['gold']})
#         ls.append(temp)
#         idx1 += 1
#         idx2 += 1
#     else:
#         idx1 += 1
# json.dump(ls, open('true_samples.json', 'w'))

# x = json.load(open('true_samples.json', 'r'))

# ls = [xx['gold'] for xx in x]
# type = [xx['db_id'] for xx in x]
# a, b = open('dev_gold.txt', 'w'), open('predicted_sql.txt', 'w')

# gold = ['{}\t{}'.format(p, q) for p, q in zip(ls, type)]
# pred = ls
# a.writelines('\n'.join(gold))
# b.writelines('\n'.join(pred))

x = json.load(open('true_samples.json', 'r'))
y = json.load(open('hardness.json', 'r'))
ls = []
for a, b in zip(x, y):
    a.update({'hardness' : b})
    ls.append(a)
json.dump(ls, open('true_samples.json', 'w'))