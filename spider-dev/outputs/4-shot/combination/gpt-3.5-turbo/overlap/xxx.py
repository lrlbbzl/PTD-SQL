import json

x = json.load(open('predict.json', 'r'))

ls = []

for p in x:
    a = p['predict']
    a = a[a.rfind('SQL query: ') + len('SQL query: ') :]
    b = p['reasoning']
    b = b[:b.rfind('SQL query: ')]
    p['predict'] = a
    p['reasoning'] = b
    ls.append(p)
json.dump(ls, open('new.json', 'w'))