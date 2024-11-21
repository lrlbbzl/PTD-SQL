import json

x = json.load(open('predict.json', 'r'))

ls = []
for xx in x:
    if xx['predict'].startswith('siti'):
        temp = xx['predict']
        sql = temp.rfind('SQL query:\n')
        ans = temp[sql + len('SQL query:\n') :]
        xx['predict'] = ans
    ls.append(xx)
json.dump(ls, open('temp.json', 'w'))