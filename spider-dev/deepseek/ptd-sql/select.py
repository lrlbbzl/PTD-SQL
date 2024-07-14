import json

x = json.load(open('my_ans.json', 'r'))

ls = []
pp = []

for a in x:
    pp.append('{}\t{}'.format(a['gold'], a['id']))
    p = a['pred']
    p = p[p.find('SQL query:') + len('SQL query:'):]
    idx = 0
    while p[idx] != 'S' and p[idx] != 's':
        idx += 1
    p = p[idx:]
    ed = p.find('\n\n')
    p = p[:ed]
    ls.append(p)
fp = open('predicted_sql.txt', 'w')
fp.writelines('\n'.join(ls))
ff = open('dev_gold.txt', 'w')
ff.writelines('\n'.join(pp))
json.dump(ls, open('temp.json', 'w'))