import json

x, y = json.load(open('true_samples.json', 'r')), json.load(open('false_samples.json', 'r'))
print(len(x))
ls = []
for k in x:
    if k['predict'] != "":
        ls.append(k)
    else:
        p = k['reasoning']
        p = p[p.rfind('SQL query: \n') + len('SQL query: \n'):]
        k['predict'] = p
        ls.append(k)
 
print(len(ls))
json.dump(ls, open('new_success.json', 'w'))