import json 
import pandas as pd
import time
import openai
import os
import sys
import argparse
from tqdm import tqdm


API_KEY = 'sk-SWjitJIKQYbpwPyUEDMcyFxRI0Q1fSwnc6mkiOW5AK7tEwxh'
os.environ["OPENAI_API_KEY"] = API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.chatanywhere.com.cn/v1"
OPENAI_MODEL = 'gpt-3.5-turbo'

prompt = """You are a text-to-sql expert. Your task is to classify text-based queries. The types are defined as follows:
1. Set operations, which require complex logical connections between multiple conditions and often involve the use of intersect, except, union, and other operations; 
2. Combination operations, which require grouping of specific objects and finding the maximum value or sorting, often achieved using GROUP BY; 
3. Filtering problems, which select targets based on specific judgment conditions, generally completed using where statements; 
4. Other simple problems, including simple retrieval and sorting.

Your task is to judge the query step by step to see if it belongs to a certain category. For example, if you think the query has the characteristics of the first type, then classify it as the first type without considering the subsequent types. If you think the query does not have the characteristics of the first type but has the second type, then classify it as the second type without considering the subsequent types.

## Example 1:
What are the ids of the students who either registered or attended a course?
Reason: We firstly consider Set operations. The query can be considered union logic which finds students that registered or attended a course, so it is classified as Set operations.
Type: Set operations

## Example 2:
List the states where both the secretary of 'Treasury' department and the secretary of 'Homeland Security' were born.
Reason: We firstly consider Set operations. The query can be considered intersection logic which requires the intersection of states that 'Treasury' and 'Homeland Security' were born, so it is classified as Set operations.
Type: Set operations

## Example 3:
Find all the zip codes in which the max dew point have never reached 70.
Reason: We firstly consider Set operations. The query can be seen as a difference logic, which removes zip codes that have reached a dew point of 70 from all zip codes, so it is classified as Set operations.
Type: Set operations

## Example 4:
Find the name of customers who do not have an saving account.
Reason: We firstly consider Set operations. The query can be consiederd difference logic, which removes customers having an saving account from all customers, so it is classified as Set operations.
Type: Set operations

## Example 5:
Which origin has most number of flights?
Reason: We firstly consider Set operations. This query does not involve logical connection relationships. We secondly consider Combination operations. This query requires statistical counting of flights within different origins, so it is classified as Combination operations.
Type: Combination operations

## Example 6:
Which course is enrolled in by the most students? Give me the course name.
Reason: We firstly consider Set operations. This query does not involve logical connection relationships. We secondly consider Combination operations. This query requires statistical counting of students within different courses, so it is classified as Combination operations.
Type: Combination operations

## Example 7:
Find the name of the train whose route runs through greatest number of stations.
Reason: We firstly consider Set operations. This query does not involve logical connection relationships. We secondly consider Combination operations. This query requires statistical counting of running stations of different trains, so it is classified as Combination operations.

## Example 8:
What are the names of musicals with nominee "Bob Fosse"?
Reason: We firstly consider Set operations. This query does not involve logical connection relationships. We secondly consider Combination operations. This query does not involve group count. We thirdly consider Filtering problems. This query needs to filter musicals based on the name of the nomenee, so it is classified as Filtering problems.
Type: Filtering problems

## Example 9:
How many distinct kinds of camera lenses are used to take photos of mountains in the country 'Ethiopia'? 
Reason: We firstly consider Set operations. This query does not involve logical connection relationships. We secondly consider Combination operations. This query does not involve group count. We thirdly consider Filtering problems. This query needs to filter camera lenses based on the utilization on mountains in country 'Ethiopia', so it is classified as Filtering problems.
Type: Filtering problems

## Example 10:
How many products are there?
Reason: We firstly consider Set operations. This query does not involve logical connection relationships. We secondly consider Combination operations. This query does not involve group count. We thirdly consider Filtering problems. This query does not involve filter criteria. So it is classified as Other simple problems.
Type: Other simple problems

{}
"""

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
  return response['choices'][0]['message']['content']

samples = open('test_data.txt', 'r').readlines()
ls = {}
for x in tqdm(samples):
    query = x.strip()
    final_prompt = prompt.format(query)
    response = None
    while response is None:
        try:
            response = GPT_generation(final_prompt)
        except openai.error.InvalidRequestError:
            json.dump(ls, open('test_type.json', 'w'))
            time.sleep(2)
        except:
            json.dump(ls, open('test_type.json', 'w'))
    single_type = response[response.rfind('Type: ') + len('Type: ') : ]
    ls.update({query : single_type})

json.dump(ls, open('test_type.json', 'w'))