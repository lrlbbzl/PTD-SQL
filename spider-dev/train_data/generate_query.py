import json

prompt = """## Tables:
{}
## Foreign_keys:
{}
## Query:
{}

SQL query: {}"""
x = json.load(open('./train_data.json', 'r'))


ls = []
while True:
    query = input().strip()
    idx = 0
    tep = None
    for i, k in enumerate(x):
        if k['question'] == query:
            tep = i
            break
    temp = x[tep]
    print(prompt.format(temp['fields'], temp['foreign_keys'], temp['question'], temp['gold']))
