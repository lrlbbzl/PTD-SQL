import re

def remove_count_as(sql_query):
    temp = sql_query.lower()
    # 使用正则表达式匹配count(*) AS子句
    pattern = r"count\(\*\) as (\w+)"
    count_as = re.search(pattern, temp)

    if count_as:
        # 替换count(*) AS子句为count(*)
        modified_sql = re.sub(pattern, "count(*)", temp)
        # 替换order by子句
        modified_sql = re.sub(f"order by {count_as.group(1)}", "order by count(*)", modified_sql)
        return modified_sql
    else:
        # 如果没有匹配到count(*) AS子句，直接返回原始SQL语句
        return sql_query

# 示例
sql_query = 'select airports.city, count(*) from flights join airports on flights.sourceairport = airports.airportcode group by airports.city order by count(*) desc limit 1'
modified_sql = remove_count_as(sql_query)
print(modified_sql)