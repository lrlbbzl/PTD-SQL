paths = [
    '../combination/gpt-4/ada_overlap',
    '../complex/gpt-4/ada_overlap',
    '../filter/gpt-4/ada_overlap',
    '../simple/gpt-4/fix'
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
pred_now, gold_now = open('./gpt-4/predicted_sql.txt', 'w'), open('./gpt-4/dev_gold.txt', 'w')
pred_now.writelines('\n'.join(pred))
gold_now.writelines('\n'.join(gold))