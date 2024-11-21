import json

files = ['./combination/combination.json', './complex/complex.json']

output = './filter/filter.json'
golds = []
for file in files:
    for x in json.load(open(file, 'r')):
        golds.append(x['gold'])

ls = []
for x in json.load(open('./all/test_data.json')):
    if x['gold'] not in golds and ('where' in x['gold'].lower()):
        ls.append(x)

json.dump(ls, open(output, 'w'))
