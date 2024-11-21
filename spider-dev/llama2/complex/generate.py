import json

# x = json.load(open('complex.json', 'r'))

# ls = [xx['gold'] for xx in x]
# type = [xx['db_id'] for xx in x]
# a, b = open('dev_gold.txt', 'w'), open('predicted_sql.txt', 'w')

# gold = ['{}\t{}'.format(p, q) for p, q in zip(ls, type)]
# pred = ls
# a.writelines('\n'.join(gold))
# b.writelines('\n'.join(pred))
x, y = json.load(open('complex.json', 'r')), json.load(open('complex_new.json', 'r'))
a = [aa['question'] for aa in x]

for p in y:
    if p['question'] not in a:
        x.append(p)
json.dump(x, open('com.json', 'w'))