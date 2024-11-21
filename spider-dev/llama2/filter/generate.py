import json

# x = json.load(open('filter.json', 'r'))

# ls = [xx['gold'] for xx in x]
# type = [xx['db_id'] for xx in x]
# a, b = open('dev_gold.txt', 'w'), open('predicted_sql.txt', 'w')

# gold = ['{}\t{}'.format(p, q) for p, q in zip(ls, type)]
# pred = ls
# a.writelines('\n'.join(gold))
# b.writelines('\n'.join(pred))

x = json.load(open('filter.json', 'r'))
y = json.load(open('hardness.json', 'r'))
ls = []
for a, b in zip(x, y):
    a.update({'hardness' : b})
    ls.append(a)
json.dump(ls, open('filter.json', 'w'))