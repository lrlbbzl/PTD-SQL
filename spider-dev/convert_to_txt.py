import json
import os
from utils import remove_count_as

predict_path = '/root/text2sql/spider-dev/llama2/group_ablation_gpt4/(3,)-0.json'
x = json.load(open(predict_path, 'r'))
fp1 = open(os.path.join(os.path.dirname(predict_path), 'dev_gold.txt'), 'w')
fp2 = open(os.path.join(os.path.dirname(predict_path), 'predicted_sql.txt'), 'w')

ls1, ls2 = [], []

for xx in x:
    ls1.append('{}\t{}'.format(xx['gold'], xx['db_id']))
    pred = xx['predict']
    pred = pred.replace("\n", " ")
    pred = remove_count_as(pred)
    if '\n' in pred:
        pred = pred.replace('\n', ' ')
    if 'left join' in pred:
        pred = pred.replace("left join", "join")
    elif 'LEFT JOIN' in pred:
        pred = pred.replace("LEFT JOIN", 'JOIN')
    if ' <> ' in pred:
        pred.replace(' <> ', ' != ')
    ls2.append(pred)

fp1.writelines('\n'.join(ls1))
fp2.writelines('\n'.join(ls2))

fp1.close()
fp2.close()
