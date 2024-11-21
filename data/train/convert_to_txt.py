import json
import os
from utils import remove_count_as

predict_path = './simple/true_samples.json'
x = json.load(open(predict_path, 'r'))
fp1, fp2 = open(os.path.join(os.path.dirname(predict_path), 'dev_gold.txt'), 'w'), open(os.path.join(os.path.dirname(predict_path), 'predicted_sql.txt'), 'w')

ls1, ls2 = [], []

for xx in x:
    ls1.append('{}\t{}'.format(xx['predict'], xx['db_id']))
    # if xx['predict'] == "" or xx['predict'] == " ":
    #     xx['predict'] = 'select'
    # xx['predict'] = xx['predict'].replace("\n", "")
    # pred = remove_count_as(xx['predict'])
    ls2.append(xx['predict'])


fp1.writelines('\n'.join(ls1))
fp2.writelines('\n'.join(ls2))

fp1.close()
fp2.close()
