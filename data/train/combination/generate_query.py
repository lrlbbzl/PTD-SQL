import json

# prompt = """## Tables:
# {}

# ## Foreign_keys:
# {}

# ## Query:
# {}

# Let's think step by step."""
# x = json.load(open('false_samples.json', 'r'))
# while True:
#     idx = int(input())
#     s = x[idx]
#     a = s['fields'].strip()
#     b = s['foreign_keys'].strip()
#     b = b[len('Foreign_keys = ') :]
#     c = s['question']
#     print(prompt.format(a, b, c))
#     print()

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
