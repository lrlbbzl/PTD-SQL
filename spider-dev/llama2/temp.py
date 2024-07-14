dirs = ['combination', 'complex', 'filter', 'simple']

files = ['{}.json'.format(x) for x in dirs]

import os
import json
for d, f in zip(dirs, files):
    read_path = os.path.join(d, f)
    x = json.load(open(read_path, 'r'))
    ls = []
    for id, xx in enumerate(x):
        xx.update({'number' : id})
        ls.append(xx)
    json.dump(ls, open(read_path, 'w'))