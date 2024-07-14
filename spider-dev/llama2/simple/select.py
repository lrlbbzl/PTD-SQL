import json

x = json.load(open("../group_type_data.json", 'r'))
data = x['Other simple problem']
print(len(data))
complex = json.load(open('../test_data.json', 'r'))
ls = []
for p in complex:
    if p['question'] in data:
        ls.append(p)
json.dump(ls, open('simple.json', 'w'))            
print(len(ls))