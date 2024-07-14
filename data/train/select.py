import json
import random 
# words = ['intersect', 'union', 'except', 'group by', 'order by', 'where']
words = ['intersect', 'union', 'except']

# x = json.load(open('./simple/true_samples_2.json', 'r'))
# print(len(x))
# ls = list()
# ls_hard = []
# ls_extra = []
# for a in x:
#     b = a['hardness']
#     if b in ['easy', 'medium']:
#         ls.append(a)
#     if b == 'hard':
#         ls_hard.append(a)
#     if b == 'extra':
#         ls_extra.append(a)
# ls_hard = random.sample(ls_hard, 25)
# ls_extra = random.sample(ls_extra, 21)
# print(len(ls))
# ls.extend(ls_hard)
# ls.extend(ls_extra)
# print(len(ls))
# json.dump(ls, open('./simple/true_samples.json', 'w'))

# x = json.load(open('train_data.json', 'r'))
# ls = []
# for xx in x:
#     for w in words:
#         if w in xx['gold'].lower():
#             xx['tables'] = xx.pop('fields')
#             ls.append(xx)
#             break
# ls = random.sample(ls, 80)
# json.dump(ls, open('../pre/ptd_data.json', 'w'))

type = ['combination', 'simple', 'filter', 'complex']
for t in type:
    x = json.load(open('{}/true_samples.json'.format(t), 'r'))
    print('{}: {}'.format(t, len(x)))    