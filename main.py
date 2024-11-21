import json 
import time
import openai
import os
import sys
import argparse
from tqdm import tqdm
import torch
import torch.nn.functional as F

from complex import complex_prompt, complex_search_prompt
from combination import combination_prompt, combination_search_prompt
from filter import filter_prompt, filter_search_prompt
from simple import simple_prompt, simple_search_prompt

from matching import auto_prompting
from similarity import TextDataset, CustomBertModel
from utils import move_to_cuda
from freeze import freeze_prompt1, freeze_prompt2, freeze_prompt3, freeze_prompt4

freeze_prompt = complex_prompt

shot_prompt = """## Tables:
{}
## Foreign_keys:
{}
## Query:
{}

Let's think step by step.

{}"""

simple_shot_prompt = """## Tables:
{}
## Foreign_keys:
{}
## Query:
{}

SQL query: {}"""

single_prompt = """## Tables:
{}
## Foreign_keys:
{}
## Query:
{}
"""


API_KEY = 'YOUR_OPENAI_API_KEY'
os.environ["OPENAI_API_KEY"] = API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.chatanywhere.com.cn/v1"
OPENAI_MODEL = 'gpt-3.5-turbo'


search_prompt = complex_search_prompt
type_prompt = complex_prompt

def GPT_generation(prompt):
  response = openai.ChatCompletion.create(
    model=OPENAI_MODEL,
    messages=[{"role": "user", "content": prompt}],
    n = 1,
    stream = False,
    temperature=0.0,
    max_tokens=500,
    top_p = 1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop = ["Q:"]
  )
  return response['choices'][0]['message']['content'], response['usage']['total_tokens']

def generate_single_prompt(x, simple=False):
    foreign_keys = x['foreign_keys']
    foreign_keys = foreign_keys[foreign_keys.find('Foreign_keys = ') + len('Foreign_keys = ') : ]
    if not simple:
      if 'fields' in x:
         if 'reasoning' in x:
            return shot_prompt.format(x['fields'], foreign_keys, x['question'], x['reasoning'])
         else:
            return shot_prompt.format(x['fields'], foreign_keys, x['question'], x['predict'])
      return single_prompt.format(x['tables'], foreign_keys, x['question'])
    if 'fields' in x:    
      return simple_shot_prompt.format(x['fields'], foreign_keys, x['question'], x['predict'])
    return single_prompt.format(x['tables'], foreign_keys, x['question'])


def question_to_item(x, data):
   for xx in data:
      if xx['question'] == x:
         return xx

def get_hardness(x, data):
   for xx in data:
      if xx['question'] == x:
         return xx['hardness']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-data", default='../text2sql/spider-dev/llama2/simple/simple.json', type=str)
    parser.add_argument("--train-data", default='./data/train/all/true_samples.json', type=str)
    parser.add_argument("--prompt-type", default='ada_overlap', choices=['fix', 'overlap', 'similarity', 'ada', 'ada_overlap'])
    parser.add_argument("--model", default='gpt-3.5-turbo', choices=['gpt-3.5-turbo', 'gpt4'])
    parser.add_argument("--plm-path", default='bert-base-uncased')
    args = parser.parse_args()

    
   #  output_dir = os.path.join(os.path.join(os.path.dirname(args.test_data), args.model), args.prompt_type)
    output_dir = os.path.join(os.path.join(os.path.dirname(args.test_data), 'ablation'), args.prompt_type)
    print(output_dir)
    question_type = args.test_data[args.test_data.rfind('/') + 1 : args.test_data.rfind('.')]
    flag = True if question_type == 'simple' else False
    embeds_train_path, embeds_test_path = os.path.join(os.path.dirname(args.train_data), 'train_embeds.pt'), os.path.join(os.path.dirname(args.test_data), 'test_embeds.json')
    if not os.path.exists(output_dir):
      os.makedirs(output_dir)
    test_data = json.load(open(args.test_data, 'r'))
    train_data = json.load(open(args.train_data, 'r'))
    new_data = []
    output_file = os.path.join(output_dir, 'predict.json')
   #  if os.path.exists(output_file):
   #    new_data = json.load(open(output_file, 'r'))
   #    test_data = test_data[len(new_data):]
    # fixed
    if args.prompt_type == 'fix':
      for x in tqdm(test_data):
          foreign_keys = x['foreign_keys']
          foreign_keys = foreign_keys[foreign_keys.find('Foreign_keys = ') + len('Foreign_keys = ') : ]
          query = freeze_prompt.format(x['tables'], foreign_keys, x['question'])
          response = None
          while response is None:
              try:
                  # import pdb; pdb.set_trace()
                  response = GPT_generation(query)
              except:
                  json.dump(new_data, open(output_file, 'w'))
                  time.sleep(2)
          sql = response.rfind('SQL query: ')
          ans = response[sql + len('SQL query: ') :]
          reason = response[:sql]
          x.update({'reasoning' : reason, 'predict' : ans})
          new_data.append(x)
      json.dump(new_data, open(output_file, 'w'))
       
    ## automation   
    if args.prompt_type == 'overlap':
      matching_list = auto_prompting(test_data, train_data, shots=4)
      # for i, (k, v) in tqdm(enumerate(matching_list.items())):
      #   test_sample = generate_single_prompt(question_to_item(k, test_data), flag)
      #   train_samples = [generate_single_prompt(question_to_item(v[i], train_data), flag) for i in range(len(v))]
      #   final_prompt = search_prompt.format(train_samples[0], train_samples[1], train_samples[2], train_samples[3], test_sample)
      #   response = None
        # while response is None:
        #   try:
        #       response = GPT_generation(final_prompt)
        #   except openai.error.InvalidRequestError:
        #       temp = question_to_item(k, test_data)
        #       foreign_keys = temp['foreign_keys']
        #       response = None
        #       foreign_keys = foreign_keys[foreign_keys.find('Foreign_keys = ') + len('Foreign_keys = ') : ]
        #       final_prompt = type_prompt.format(temp['tables'], foreign_keys, temp['question'])
        #   except:
        #       json.dump(new_data, open(output_file, 'w'))
      #   sql = response.rfind('SQL query:\n')
      #   ans = response[sql + len('SQL query:\n') :]
      #   reason = response[:sql]
      #   temp = test_data[i]
      #   temp.update({'reasoning' : reason, 'predict' : ans})
      #   new_data.append(temp)
      # json.dump(new_data, open(output_file, 'w'))
      dic = dict()
      for i, (k, v) in tqdm(enumerate(matching_list.items())):
        if test_data[i]['hardness'] not in dic:
           dic.update({test_data[i]['hardness'] : {}})
        test_sample = generate_single_prompt(question_to_item(k, test_data), flag)
        train_samples = [generate_single_prompt(question_to_item(v[i], train_data), flag) for i in range(len(v))]
        hardnesses = [get_hardness(v[i], train_data) for i in range(len(v))]
        for h in hardnesses:
           if h not in dic[test_data[i]['hardness']]:
              dic[test_data[i]['hardness']].update({h : 0})
           dic[test_data[i]['hardness']][h] += 1
        final_prompt = search_prompt.format(train_samples[0], train_samples[1], train_samples[2], train_samples[3], test_sample)
      print(dic)

    if args.prompt_type == 'similarity':
       train_question_data = TextDataset(args, 'train')
       test_question_data = TextDataset(args, 'test')
       model = CustomBertModel(args)
       train_loader = torch.utils.data.DataLoader(train_question_data, batch_size=4, shuffle=False, collate_fn=model.collate)
       test_loader = torch.utils.data.DataLoader(test_question_data, batch_size=4, shuffle=False, collate_fn=model.collate)
       ls = []

       for i, batch_dict in enumerate(train_loader):
          # batch_dict = move_to_cuda(batch_dict)
          outputs = model(**batch_dict)
          ls.append(outputs)
       train_embeddings = torch.cat(ls, dim=0)
       ls = []

       for i, batch_dict in enumerate(test_loader):
          # batch_dict = move_to_cuda(batch_dict)
          outputs = model(**batch_dict)
          ls.append(outputs)
       test_embeddings = torch.cat(ls, dim=0)

       norm_train = F.normalize(train_embeddings, dim=1)
       norm_test = F.normalize(test_embeddings, dim=1)
       sim = torch.matmul(norm_test, norm_train.t())  
       select = torch.argsort(sim, dim=1)[:, : 4]
       dic = {}
       for i, x in tqdm(enumerate(test_data)):
          # record hardness 
          hardnesses = [train_data[idx]['hardness'] for idx in select[i]]
          if test_data[i]['hardness'] not in dic:
             dic.update({test_data[i]['hardness'] : {}})
          for h in hardnesses:
           if h not in dic[test_data[i]['hardness']]:
              dic[test_data[i]['hardness']].update({h : 0})
           dic[test_data[i]['hardness']][h] += 1
       print(dic)
      #     test_sample = generate_single_prompt(x, flag)
      #     train_samples = [generate_single_prompt(train_data[idx], flag) for idx in select[i]]
      #     final_prompt = search_prompt.format(train_samples[0], train_samples[1], train_samples[2], train_samples[3], test_sample)
      #     response = None
      #     while response is None:
      #       try:
      #           response = GPT_generation(final_prompt)
      #       except openai.error.InvalidRequestError:
      #           foreign_keys = x['foreign_keys']
      #           response = None
      #           foreign_keys = foreign_keys[foreign_keys.find('Foreign_keys = ') + len('Foreign_keys = ') : ]
      #           final_prompt = type_prompt.format(x['tables'], foreign_keys, x['question'])
      #       except:
      #           json.dump(new_data, open(output_file, 'w'))
      #     sql = response.rfind('SQL query:\n')
      #     ans = response[sql + len('SQL query:\n') :]
      #     reason = response[:sql]
      #     x.update({'reasoning' : reason, 'predict' : ans})
      #     new_data.append(x)
      #  json.dump(new_data, open(output_file, 'w'))
       
    if args.prompt_type == 'ada':
       train_embeds, test_embeds = [], []
       if not os.path.exists(embeds_test_path):
         for a in tqdm(train_data): 
            response = openai.Embedding.create(
               input=a['question'],
               model="text-embedding-ada-002"
            )
            embedding = response['data'][0]['embedding']
            train_embeds.append(torch.tensor(embedding).unsqueeze(0))
         for a in tqdm(test_data):
            response = openai.Embedding.create(
               input=a['question'],
               model="text-embedding-ada-002"
            )
            embedding = response['data'][0]['embedding']
            test_embeds.append(torch.tensor(embedding).unsqueeze(0))
         train_embeddings = torch.cat(train_embeds, dim=0)
         test_embeddings = torch.cat(test_embeds, dim=0)
         torch.save(train_embeddings, embeds_train_path)
         torch.save(test_embeddings, embeds_test_path)
         norm_train = F.normalize(train_embeddings, dim=1)
         norm_test = F.normalize(test_embeddings, dim=1)
         sim = torch.matmul(norm_test, norm_train.t())  
         select = torch.argsort(sim, dim=1)[:, : 4]
         dic = {}
         for i, x in tqdm(enumerate(test_data)):
            # record hardness 
            hardnesses = [train_data[idx]['hardness'] for idx in select[i]]
            if test_data[i]['hardness'] not in dic:
               dic.update({test_data[i]['hardness'] : {}})
            for h in hardnesses:
               if h not in dic[test_data[i]['hardness']]:
                  dic[test_data[i]['hardness']].update({h : 0})
               dic[test_data[i]['hardness']][h] += 1
         print(dic)
       else:
          train_embeddings, test_embeddings = torch.load(embeds_train_path), torch.load(embeds_test_path)
          norm_train = F.normalize(train_embeddings, dim=1)
          norm_test = F.normalize(test_embeddings, dim=1)
          sim = torch.matmul(norm_test, norm_train.t())  
          select = torch.argsort(sim, dim=1)[:, : 6]

          for i, x in tqdm(enumerate(test_data)):
            test_sample = generate_single_prompt(x, flag)
            train_samples = [generate_single_prompt(train_data[idx], flag) for idx in select[i]]
            final_prompt = search_prompt.format(train_samples[0], train_samples[1], train_samples[2], train_samples[3], test_sample)
            response = None
            overlong_num = 0
            while response is None:
               try:
                  response = GPT_generation(final_prompt)
               except openai.error.InvalidRequestError:
                  overlong_num += 1
                  foreign_keys = x['foreign_keys']
                  response = None
                  foreign_keys = foreign_keys[foreign_keys.find('Foreign_keys = ') + len('Foreign_keys = ') : ]
                  final_prompt = type_prompt.format(x['tables'], foreign_keys, x['question'])
               except:
                  json.dump(new_data, open(output_file, 'w'))
            sql = response.rfind('SQL query:\n')
            ans = response[sql + len('SQL query:\n') :]
            reason = response[:sql]
            x.update({'reasoning' : reason, 'predict' : ans})
            new_data.append(x)
          print(overlong_num)
          json.dump(new_data, open(output_file, 'w'))
    if args.prompt_type == 'ada_overlap':

       train_embeds, test_embeds = [], []
       if not os.path.exists(embeds_test_path):
         for a in tqdm(test_data):
            response = openai.Embedding.create(
               input=a['question'],
               model="text-embedding-ada-002"
            )
            embedding = response['data'][0]['embedding']
            test_embeds.append(torch.tensor(embedding).unsqueeze(0))
         test_embeddings = torch.cat(test_embeds, dim=0)
         torch.save(test_embeddings, embeds_test_path)
       if not os.path.exists(embeds_train_path):
         for a in tqdm(train_data): 
            response = openai.Embedding.create(
               input=a['question'],
               model="text-embedding-ada-002"
            )
            embedding = response['data'][0]['embedding']
            train_embeds.append(torch.tensor(embedding).unsqueeze(0))
         train_embeddings = torch.cat(train_embeds, dim=0)
         torch.save(train_embeddings, embeds_train_path)
       if os.path.exists(embeds_train_path) and os.path.exists(embeds_test_path):
          # part1
          train_embeddings, test_embeddings = torch.load(embeds_train_path), torch.load(embeds_test_path)
          norm_train = F.normalize(train_embeddings, dim=1)
          norm_test = F.normalize(test_embeddings, dim=1)
          sim = torch.matmul(norm_test, norm_train.t())  
          select = torch.argsort(sim, dim=1)[:, : 2]
          # part 2
          matching_list = auto_prompting(test_data, train_data, shots=10)
          overlong_num = 0
          token_nums = 0
          for i, x in tqdm(enumerate(test_data)):
          
            test_sample = generate_single_prompt(x, flag)
            train_samples = [generate_single_prompt(train_data[idx], flag) for idx in select[i]]
            train_qs = [train_data[idx]['question'] for idx in select[i]]
            v = matching_list[test_data[i]['question']]
            v = [q for q in v if q not in train_qs]
            train_samples_p2 = [generate_single_prompt(question_to_item(v[i], train_data), flag) for i in range(2)]
            train_samples.extend(train_samples_p2)
            train_samples.extend([test_sample])
            final_prompt = search_prompt.format(*train_samples)

            response = None
            while response is None:
               try:
                  response, num = GPT_generation(final_prompt)
                  token_nums += num
               except openai.error.InvalidRequestError:
                  overlong_num += 1
                  foreign_keys = x['foreign_keys']
                  response = None
                  foreign_keys = foreign_keys[foreign_keys.find('Foreign_keys = ') + len('Foreign_keys = ') : ]
                  final_prompt = type_prompt.format(x['tables'], foreign_keys, x['question'])
               except:
                  json.dump(new_data, open('temp.json', 'w'))
            sql = response.rfind('SQL query: ')
            ans = response[sql + len('SQL query: ') :]
            reason = response[:sql]
            x.update({'reasoning' : reason, 'predict' : ans})
            new_data.append(x)
          print(overlong_num, token_nums)
          json.dump(new_data, open('temp.json', 'w'))
             

          
       
       

