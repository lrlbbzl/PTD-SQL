combination_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of combination operations. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
## Tables:
Table gymnast, columns = [*,Gymnast_ID,Floor_Exercise_Points,Pommel_Horse_Points,Rings_Points,Vault_Points,Parallel_Bars_Points,Horizontal_Bar_Points,Total_Points]
Table people, columns = [*,People_ID,Name,Age,Height,Hometown]

## Foreign_keys:
[gymnast.Gymnast_ID = people.People_ID]

## Query:
How many gymnasts are from each hometown?

Let's think step by step.

<1> Operation: the query requires the number of gymnasts from each hometown, so we should apply the 'count' operation to table 'gymnast', and it does not need sort. Since the unit to which the gymnasts being counted in the query belong is hometown and only table 'people' has column 'Hometown', so we should apply the 'group by' operation to column 'Hometown' in table 'people'. 

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. Due to the direct foreign key connection between table 'gymnast' and 'people', we need to use tables ['gymnast', 'people']. 

<3> SQL Generation: The query requires number of gymnasts from each hometown, so we should select the count and 'hometown' in people.

SQL query: SELECT T2.Hometown ,  COUNT(*) FROM gymnast AS T1 JOIN people AS T2 ON T1.Gymnast_ID  =  T2.People_ID GROUP BY T2.Hometown


Example 2:
## Tables:
Table county, columns = [*,County_Id,County_name,Population,Zip_code]
Table election, columns = [*,Election_ID,Counties_Represented,District,Delegate,Party,First_Elected,Committee]
Table party, columns = [*,Party_ID,Year,Party,Governor,Lieutenant_Governor,Comptroller,Attorney_General,US_Senate]

## Foreign_keys
[election.District = county.County_Id,election.Party = party.Party_ID]

## Query:
Show the name of each party and the corresponding number of delegates from that party.

Decompose and find the tables to be used:

Let's think step by step.

<1> Operation: The query requires the name of each party and the corresponding number of delegates from that party, so we should apply the 'count' operation to table 'election' for the 'Delegate' column, and it does not need sorting. Since the unit to which the delegates being counted in the query belong is the party and only table 'party' has the column 'Party', so we should apply the 'group by' operation to column 'Party' in table 'party'.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. Due to the direct foreign key connection between table 'election' and 'party'. We need to use tables ['election', 'party'].

<3> SQL Generation: The query requires the name of each party and the corresponding number of delegates from that party, so we should select the 'Party' column in the 'party' table and count the 'Delegate' column in the 'election' table.

SQL query: SELECT T1.Party , COUNT(*) FROM party AS T1 JOIN election AS T2 ON T1.Party_ID = T2.Party GROUP BY T1.Party


Example 3:
## Tables:
Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]

## Foreign_keys:
[farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]

## Query:
Show the status of the city that has hosted the greatest number of competitions.

Decompose and find the tables to be used:

Let's think step by step.

<1> Operation: The query requires the city that has hosted greatest number of competitions, so we should apply the 'count' operation to table 'farm_competition', and sort it in descending order. Since the unit to which the competitions being counted in the query belong is city and only table 'farm_competition' has column 'Host_city_ID', so we should apply the 'group by' operation to column 'Host_city_ID' in table 'farm_competition'.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the requirements of the query and the foreign key relationships. Due to the direct foreign key connection between table 'city' and 'farm_competition'. We need to use tables ['city', 'farm_competition'].

<3> SQL generation: The query requires the status of the city that has hosted the greatest number of competitions, so we should select the 'Status' column in the 'city' table. The query does not require the count of most competitions, so it is only used for filtering and not selected. 

SQL query: SELECT T1.Status FROM city AS T1 JOIN farm_competition AS T2 ON T1.City_ID  =  T2.Host_city_ID GROUP BY T2.Host_city_ID ORDER BY COUNT(*) DESC LIMIT 1


Example 4:
## Tables:
Table albums, columns = [*,id,title,artist_id]\nTable artists, columns = [*,id,name]
Table customers, columns = [*,id,first_name,last_name,company,address,city,state,country,postal_code,phone,fax,email,support_rep_id]
Table employees, columns = [*,id,last_name,first_name,title,reports_to,birth_date,hire_date,address,city,state,country,postal_code,phone,fax,email]
Table genres, columns = [*,id,name]
Table invoice_lines, columns = [*,id,invoice_id,track_id,unit_price,quantity]
Table invoices, columns = [*,id,customer_id,invoice_date,billing_address,billing_city,billing_state,billing_country,billing_postal_code,total]
Table media_types, columns = [*,id,name]
Table playlist_tracks, columns = [*,playlist_id,track_id]
Table playlists, columns = [*,id,name]
Table sqlite_sequence, columns = [*,name,seq]
Table tracks, columns = [*,id,name,album_id,media_type_id,genre_id,composer,milliseconds,bytes,unit_price]

## Foreign_keys:
[albums.artist_id = artists.id,employees.reports_to = employees.id,customers.support_rep_id = employees.id,invoices.customer_id = customers.id,tracks.media_type_id = media_types.id,tracks.genre_id = genres.id,tracks.album_id = albums.id,invoice_lines.track_id = tracks.id,invoice_lines.invoice_id = invoices.id,playlist_tracks.track_id = tracks.id,playlist_tracks.playlist_id = playlists.id]

## Query:
A list of the top 10 countries by average invoice size. List country name and average invoice size.

Let's think step by step.

<1> Operation: The query requires the top 10 countries by average invoice size, so we should apply the 'average' operation to the 'total' column in the 'invoices' table and sort it in descending order. Since the unit to which the average invoice size being calculated in the query belongs is the country and only table 'customers' has the column 'country', we should apply the 'group by' operation to the 'country' column in the 'customers' table.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. Due to the direct foreign key connection between table 'invoices' and 'customers', we need to use tables ['invoices', 'customers'].

<3> SQL Generation: The query requires the top 10 countries by average invoice size, so we should select the 'country' column in the 'customers' table and the average of the 'total' column in the 'invoices' table.

SQL query: 
SELECT T1.country, AVG(T2.total) FROM customers AS T1 JOIN invoices AS T2 ON T1.id = T2.customer_id GROUP BY T1.country ORDER BY AVG(T2.total) DESC LIMIT 10


Example 5:
## Tables:
Table aircraft, columns = [*,aid,name,distance]
Table certificate, columns = [*,eid,aid]
Table employee, columns = [*,eid,name,salary]
Table flight, columns = [*,flno,origin,destination,distance,departure_date,arrival_date,price,aid]

## Foreign_keys:
[flight.aid = aircraft.aid,certificate.aid = aircraft.aid,certificate.eid = employee.eid]

## Query:
What is the salaray and name of the employee with the most certificates to fly planes more than 5000?

Let's think step by step.

<1> Operation: The query requires the salary and name of the employee with the most certificates to fly planes with a distance greater than 5000, so we should apply the 'count' operation to the 'certificate' table for the 'eid' column, and find the employee with the highest count. Since the unit to which the certificates being counted in the query belong is the employee, we should apply the 'group by' operation to the 'eid' column in the 'certificate' table. We also need to filter the planes with a distance greater than 5000 in the 'aircraft' table.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. Due to the direct foreign key connections between table 'employee', 'certificate', and 'aircraft', we need to use tables ['employee', 'certificate', 'aircraft'].

<3> SQL Generation: The query requires the salary and name of the employee with the most certificates to fly planes with a distance greater than 5000, so we should select the 'name' and 'salary' columns in the 'employee' table and the 'eid' column in the 'certificate' table.

SQL query: SELECT T1.name, T1.salary FROM employee AS T1 JOIN certificate AS T2 ON T1.eid = T2.eid JOIN aircraft AS T3 ON T2.aid = T3.aid WHERE T3.distance > 5000 GROUP BY T1.eid ORDER BY COUNT(*) DESC LIMIT 1


Example 6:
## Tables:
Table Addresses, columns = [*,address_id,address_content,city,zip_postcode,state_province_county,country,other_address_details]
Table Customer_Addresses, columns = [*,customer_id,address_id,date_address_from,address_type,date_address_to]
Table Customer_Contact_Channels, columns = [*,customer_id,channel_code,active_from_date,active_to_date,contact_number]
Table Customer_Orders, columns = [*,order_id,customer_id,order_status,order_date,order_details]
Table Customers, columns = [*,customer_id,payment_method,customer_name,date_became_customer,other_customer_details]
Table Order_Items, columns = [*,order_id,product_id,order_quantity]
Table Products, columns = [*,product_id,product_details]

## Foreign_keys:
[Customer_Addresses.customer_id = Customers.customer_id,Customer_Addresses.address_id = Addresses.address_id,Customer_Contact_Channels.customer_id = Customers.customer_id,Customer_Orders.customer_id = Customers.customer_id,Order_Items.order_id = Customer_Orders.order_id,Order_Items.product_id = Products.product_id]

## Query:
What are the names of customers using the most popular payment method?

Let's think step by step.

<1> Operation: The query requires the names of customers using the most popular payment method, so we should apply the 'count' operation to the 'Customers' table for the 'payment_method' column, and find the payment method with the highest count. Since the unit to which the payment methods being counted in the query belong is the customer, we should apply the 'group by' operation to the 'payment_method' column in the 'Customers' table.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. In this question, we only need to use table ['Customers'].

<3> SQL Generation: The query requires the names of customers using the most popular payment method, so we should select the 'customer_name' column in the 'Customers' table and the 'payment_method' column in the 'Customers' table.

SQL query: SELECT customer_name FROM Customers WHERE payment_method = (SELECT payment_method FROM Customers GROUP BY payment_method ORDER BY COUNT(*) DESC LIMIT 1)


## Tables:
{}

## Foreign_keys:
{}

## Query:
{}

Let's think step by step.

"""

combination_search_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of combination operations. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
{}


{}
Let's think step by step.

"""