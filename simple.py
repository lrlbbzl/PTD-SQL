simple_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of set operations. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
## Tables:
Table Available_Policies, columns = [*,Policy_ID,policy_type_code,Customer_Phone]
Table Claims, columns = [*,Claim_ID,FNOL_ID,Effective_Date]
Table Customers, columns = [*,Customer_ID,Customer_name]
Table Customers_Policies, columns = [*,Customer_ID,Policy_ID,Date_Opened,Date_Closed]
Table First_Notification_of_Loss, columns = [*,FNOL_ID,Customer_ID,Policy_ID,Service_ID]
Table Services, columns = [*,Service_ID,Service_name]
Table Settlements, columns = [*,Settlement_ID,Claim_ID,Effective_Date,Settlement_Amount]

## Foreign_keys:
Foreign_keys = [Customers_Policies.Policy_ID = Available_Policies.Policy_ID,Customers_Policies.Customer_ID = Customers.Customer_ID,First_Notification_of_Loss.Customer_ID = Customers_Policies.Customer_ID,First_Notification_of_Loss.Policy_ID = Customers_Policies.Policy_ID,First_Notification_of_Loss.Service_ID = Services.Service_ID,Claims.FNOL_ID = First_Notification_of_Loss.FNOL_ID,Settlements.Claim_ID = Claims.Claim_ID]

## Query:
Which policy type has the most records in the database?

SQL query: SELECT policy_type_code FROM available_policies GROUP BY policy_type_code ORDER BY count(*) DESC LIMIT 1


## Tables:
{}
## Foreign_keys:
{}
## Query:
{}
"""

simple_search_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of set operations. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
{}


Example 2:
{}


Example 3:
{}


Example 4:
{}


Example 5:
{}


Example 6:
{}


{}
Let's think step by step.
"""