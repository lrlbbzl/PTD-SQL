import json

x = json.load(open("./similarity/predict.json", 'r'))
# y = json.load(open('../../../Few-shot-NL2SQL-with-prompting/outputs/fail_examples.json', 'r'))

ls = []
print(len(x))
for l in x:
    temp = l['predict']
    import pdb; pdb.set_trace()
    temp = temp[temp.rfind('SQL query:\n') + len('SQL query:\n') : ]
    l['predict'] = temp
    ls.append(l)
print(len(ls))
print(ls[1])
json.dump(ls, open('new_predict.json', 'w'))
