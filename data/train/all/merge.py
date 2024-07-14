import json
import torch
data, embeds = [], []

types = ['combination', 'complex', 'filter', 'simple']

for t in types:
    p = torch.load('../{}/train_embeds.json'.format(t))
    a = json.load(open('../{}/true_samples.json'.format(t)))
    data.extend(a)
    embeds.append(p)
embed = torch.cat(embeds, dim=0)
torch.save(embed, 'train_embeds.pt')
json.dump(data, open('true_samples.json', 'w'))