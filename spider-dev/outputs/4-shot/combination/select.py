import json

x = json.load(open("../group_type_data.json", 'r'))
data = x['Combination operation']
print(len(data))
test_data = json.load(open('../test_data.json', 'r'))
ls = []
for p in test_data:
    if p['question'] in data:
        ls.append(p)
json.dump(ls, open('combination.json', 'w'))            
print(len(ls))            