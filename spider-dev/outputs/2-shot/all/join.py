paths = [
    '../combination/ada_overlap',
    '../complex/ada_overlap',
    '../filter/ada_overlap',
    '../simple/fix'
]

pred, gold = [], []

import os
for pa in paths:
    gold_file = os.path.join(pa, 'dev_gold.txt')
    pred_file = os.path.join(pa, 'predicted_sql.txt')
    fp = open(gold_file, 'r').readlines()
    print('{}  {}'.format(gold_file, len(fp)))
    for line in fp:
        gold.append(line.strip())
    for line in open(pred_file, 'r').readlines():
        pred.append(line.strip())
pred_now, gold_now = open('./predicted_sql.txt', 'w'), open('./dev_gold.txt', 'w')
pred_now.writelines('\n'.join(pred))
gold_now.writelines('\n'.join(gold))