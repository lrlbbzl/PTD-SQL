freeze_prompt1 = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. 

Example 1:
## Tables:
Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]

## Foreign_keys:
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]

## Query:
List the name, born state and age of the heads of departments ordered by age.

SQL query: SELECT name ,  born_state ,  age FROM head ORDER BY age


Example 2:
## Tables:
Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]

## Foreign_keys:
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]

## Query:
List the creation year, name and budget of each department.

SQL query: SELECT creation ,  name ,  budget_in_billions FROM department


Example 3:
## Tables:
Table race, columns = [*,Race_ID,Name,Class,Date,Track_ID]
Table track, columns = [*,Track_ID,Name,Location,Seating,Year_Opened]

## Foreign_keys:
Foreign_keys = [race.Track_ID = track.Track_ID]

## Query:
Show year where a track with a seating at least 5000 opened and a track with seating no more than 4000 opened.

SQL query: SELECT year_opened FROM track WHERE seating BETWEEN 4000 AND 5000


Example 4:
## Tables:
Table Album, columns = [*,AlbumId,Title,ArtistId]
Table Artist, columns = [*,ArtistId,Name]
Table Customer, columns = [*,CustomerId,FirstName,LastName,Company,Address,City,State,Country,PostalCode,Phone,Fax,Email,SupportRepId]
Table Employee, columns = [*,EmployeeId,LastName,FirstName,Title,ReportsTo,BirthDate,HireDate,Address,City,State,Country,PostalCode,Phone,Fax,Email]
Table Genre, columns = [*,GenreId,Name]
Table Invoice, columns = [*,InvoiceId,CustomerId,InvoiceDate,BillingAddress,BillingCity,BillingState,BillingCountry,BillingPostalCode,Total]
Table InvoiceLine, columns = [*,InvoiceLineId,InvoiceId,TrackId,UnitPrice,Quantity]
Table MediaType, columns = [*,MediaTypeId,Name]
Table Playlist, columns = [*,PlaylistId,Name]
Table PlaylistTrack, columns = [*,PlaylistId,TrackId]
Table Track, columns = [*,TrackId,Name,AlbumId,MediaTypeId,GenreId,Composer,Milliseconds,Bytes,UnitPrice]

## Foreign_keys:
Foreign_keys = [Album.ArtistId = Artist.ArtistId,Customer.SupportRepId = Employee.EmployeeId,Employee.ReportsTo = Employee.EmployeeId,Invoice.CustomerId = Customer.CustomerId,InvoiceLine.TrackId = Track.TrackId,InvoiceLine.InvoiceId = Invoice.InvoiceId,PlaylistTrack.TrackId = Track.TrackId,PlaylistTrack.PlaylistId = Playlist.PlaylistId,Track.MediaTypeId = MediaType.MediaTypeId,Track.GenreId = Genre.GenreId,Track.AlbumId = Album.AlbumId]

## Query:
What are the album titles for albums containing both 'Reggae' and 'Rock' genre tracks?

SQL query: SELECT T1.Title FROM Album AS T1 JOIN Track AS T2 ON T1.AlbumId  =  T2.AlbumId JOIN Genre AS T3 ON T2.GenreID  =  T3.GenreID WHERE T3.Name  =  'Reggae' INTERSECT SELECT T1.Title FROM Album AS T1 JOIN Track AS T2 ON T1.AlbumId  =  T2.AlbumId JOIN Genre AS T3 ON T2.GenreID  =  T3.GenreID WHERE T3.Name  =  'Rock'


Example 5:
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


Example 6:
## Tables:
Table editor, columns = [*,Editor_ID,Name,Age]
Table journal, columns = [*,Journal_ID,Date,Theme,Sales]
Table journal_committee, columns = [*,Editor_ID,Journal_ID,Work_Type]

## Foreign_keys:
Foreign_keys = [journal_committee.Journal_ID = journal.Journal_ID,journal_committee.Editor_ID = editor.Editor_ID]

## Query:
What is the name of the youngest editor?

SQL query: SELECT Name FROM editor ORDER BY Age ASC LIMIT 1


## Tables:
{}
## Foreign_keys:
{}
## Query:
{}"""


freeze_prompt2 = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. 

Example 1:
## Tables:
Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]

## Foreign_keys:
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]

## Query:
List the creation year, name and budget of each department.

SQL query: SELECT creation ,  name ,  budget_in_billions FROM department


Example 2:
## Tables:
Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]

## Foreign_keys:
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]

## Query:
List the name, born state and age of the heads of departments ordered by age.

SQL query: SELECT name ,  born_state ,  age FROM head ORDER BY age


Example 3:
## Tables:
Table Club, columns = [*,ClubID,ClubName,ClubDesc,ClubLocation]
Table Member_of_club, columns = [*,StuID,ClubID,Position]
Table Student, columns = [*,StuID,LName,Fname,Age,Sex,Major,Advisor,city_code]

## Foreign_keys:
Foreign_keys = [Member_of_club.ClubID = Club.ClubID,Member_of_club.StuID = Student.StuID]

## Query:
Find the description of the club "Pen and Paper Gaming".

SQL query: SELECT clubdesc FROM club WHERE clubname  =  "Pen and Paper Gaming"


Example 4:
## Tables:
Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]

## Foreign_keys:
Foreign_keys = [farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]

## Query:
List the official names of cities that have not held any competition.

SQL query: SELECT Official_Name FROM city WHERE City_ID NOT IN (SELECT Host_city_ID FROM farm_competition)


Example 5:
## Tables:
Table Accounts, columns = [*,account_id,customer_id,account_name,other_account_details]
Table Customers, columns = [*,customer_id,customer_first_name,customer_last_name,customer_address,customer_phone,customer_email,other_customer_details]
Table Customers_Cards, columns = [*,card_id,customer_id,card_type_code,card_number,date_valid_from,date_valid_to,other_card_details]
Table Financial_Transactions, columns = [*,transaction_id,previous_transaction_id,account_id,card_id,transaction_type,transaction_date,transaction_amount,transaction_comment,other_transaction_details]

## Foreign_keys:
Foreign_keys = [Financial_Transactions.account_id = Accounts.account_id,Financial_Transactions.card_id = Customers_Cards.card_id]

## Query:
What is the transaction type that has processed the greatest total amount in transactions?

SQL query: SELECT transaction_type FROM Financial_transactions GROUP BY transaction_type ORDER BY sum(transaction_amount) DESC LIMIT 1


Example 6:
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
{}"""


freeze_prompt3 = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. 

Example 1:
## Tables:
Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]

## Foreign_keys:
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]

## Query:
List the creation year, name and budget of each department.

SQL query: SELECT creation ,  name ,  budget_in_billions FROM department


Example 2:
## Tables:
Table department, columns = [*,Department_ID,Name,Creation,Ranking,Budget_in_Billions,Num_Employees]
Table head, columns = [*,head_ID,name,born_state,age]
Table management, columns = [*,department_ID,head_ID,temporary_acting]

## Foreign_keys:
Foreign_keys = [management.head_ID = head.head_ID,management.department_ID = department.Department_ID]

## Query:
List the name, born state and age of the heads of departments ordered by age.

SQL query: SELECT name ,  born_state ,  age FROM head ORDER BY age


Example 3:
## Tables:
Table station, columns = [*,id,name,lat,long,dock_count,city,installation_date]
Table status, columns = [*,station_id,bikes_available,docks_available,time]
Table trip, columns = [*,id,duration,start_date,start_station_name,start_station_id,end_date,end_station_name,end_station_id,bike_id,subscription_type,zip_code]
Table weather, columns = [*,date,max_temperature_f,mean_temperature_f,min_temperature_f,max_dew_point_f,mean_dew_point_f,min_dew_point_f,max_humidity,mean_humidity,min_humidity,max_sea_level_pressure_inches,mean_sea_level_pressure_inches,min_sea_level_pressure_inches,max_visibility_miles,mean_visibility_miles,min_visibility_miles,max_wind_Speed_mph,mean_wind_speed_mph,max_gust_speed_mph,precipitation_inches,cloud_cover,events,wind_dir_degrees,zip_code]

## Foreign_keys:
Foreign_keys = [status.station_id = station.id]

## Query:
For each trip, return its ending station's installation date.

SQL query: SELECT T1.id ,  T2.installation_date FROM trip AS T1 JOIN station AS T2 ON T1.end_station_id  =  T2.id


Example 4:
## Tables:
Table Club, columns = [*,ClubID,ClubName,ClubDesc,ClubLocation]
Table Member_of_club, columns = [*,StuID,ClubID,Position]
Table Student, columns = [*,StuID,LName,Fname,Age,Sex,Major,Advisor,city_code]

## Foreign_keys:
Foreign_keys = [Member_of_club.ClubID = Club.ClubID,Member_of_club.StuID = Student.StuID]

## Query:
Find the description of the club "Pen and Paper Gaming".

SQL query: SELECT clubdesc FROM club WHERE clubname  =  "Pen and Paper Gaming"


Example 5:
## Tables:
Table Person, columns = [*,name,age,city,gender,job]
Table PersonFriend, columns = [*,name,friend,year]

## Foreign_keys:
Foreign_keys = [PersonFriend.friend = Person.name,PersonFriend.name = Person.name]

## Query:
Who is the oldest person?

SQL query: SELECT name FROM Person WHERE age  =  (SELECT max(age) FROM person)


Example 6:
## Tables:
Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]

## Foreign_keys:
Foreign_keys = [farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]

## Query:
List the official names of cities that have not held any competition.

SQL query: SELECT Official_Name FROM city WHERE City_ID NOT IN (SELECT Host_city_ID FROM farm_competition)


Example 7:
## Tables:
Table Accounts, columns = [*,account_id,customer_id,account_name,other_account_details]
Table Customers, columns = [*,customer_id,customer_first_name,customer_last_name,customer_address,customer_phone,customer_email,other_customer_details]
Table Customers_Cards, columns = [*,card_id,customer_id,card_type_code,card_number,date_valid_from,date_valid_to,other_card_details]
Table Financial_Transactions, columns = [*,transaction_id,previous_transaction_id,account_id,card_id,transaction_type,transaction_date,transaction_amount,transaction_comment,other_transaction_details]

## Foreign_keys:
Foreign_keys = [Financial_Transactions.account_id = Accounts.account_id,Financial_Transactions.card_id = Customers_Cards.card_id]

## Query:
What is the transaction type that has processed the greatest total amount in transactions?

SQL query: SELECT transaction_type FROM Financial_transactions GROUP BY transaction_type ORDER BY sum(transaction_amount) DESC LIMIT 1


Example 8:
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
{}"""


freeze_prompt4 = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of filtering problem. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
## Tables:
Table Allergy_Type, columns = [*,Allergy,AllergyType]
Table Has_Allergy, columns = [*,StuID,Allergy]
Table Student, columns = [*,StuID,LName,Fname,Age,Sex,Major,Advisor,city_code]

## Foreign_keys:
[Has_Allergy.Allergy = Allergy_Type.Allergy,Has_Allergy.StuID = Student.StuID]

## Query:
How many female students have milk or egg allergies?

Let's think step by step.

<1> Decomposition: Firstly, we filter candidates using column 'Sex' in table 'Student' and column 'Allergy' in table 'Has_Allergy'. Secondly, we use 'count' to calculate the number of selected female students.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. Since table 'Student' and table 'Has_Allergy' have direct foreign keys, so we need tables ['Student', 'Has_Allergy'].

<3> SQL Generation: We need to join the 'Student' and 'Has_Allergy' tables on the 'StuID' column. Then, we filter the rows where 'Sex' is 'F' and 'Allergy' is either 'Milk' or 'Eggs'. Finally, we count the number of rows that meet these conditions.

SQL query: SELECT count(*) FROM has_allergy AS T1 JOIN Student AS T2 ON T1.StuID  =  T2.StuID WHERE T2.sex = 'F' AND T1.allergy = 'Milk' or T1.allergy = 'Eggs'


Example 2:
## Tables:
Table station, columns = [*,id,name,lat,long,dock_count,city,installation_date]
Table status, columns = [*,station_id,bikes_available,docks_available,time]
Table trip, columns = [*,id,duration,start_date,start_station_name,start_station_id,end_date,end_station_name,end_station_id,bike_id,subscription_type,zip_code]
Table weather, columns = [*,date,max_temperature_f,mean_temperature_f,min_temperature_f,max_dew_point_f,mean_dew_point_f,min_dew_point_f,max_humidity,mean_humidity,min_humidity,max_sea_level_pressure_inches,mean_sea_level_pressure_inches,min_sea_level_pressure_inches,max_visibility_miles,mean_visibility_miles,min_visibility_miles,max_wind_Speed_mph,mean_wind_speed_mph,max_gust_speed_mph,precipitation_inches,cloud_cover,events,wind_dir_degrees,zip_code]

## Foreign_keys:
[status.station_id = station.id]

## Query:
What are names of stations that have average bike availability above 10 and are not located in San Jose city?

Let's think step by step.

<1> Question Decomposition: In this step, we contemplate how to decompose the query. The query emphasizes difference set logic, so we can decompose decompose the question into two subproblems: 1. what are names of stations that have average bike availability above 10; 2. what are names of stations that are located in San Jose city. 

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the requirements of the query and the foreign key relationships. To complete the first subproblem, we need to use tables ['station', 'status']. To complete the second subproblem, we need to use table ['station'].

<3> Operation: Due to the need for calculating the average bike availability for different stations, we need to perform a 'GROUP BY' operation on the column 'station_id', filter by perform 'HAVING AVG()' on the column 'bikes_available'. 

<4> SQL Generation: Use 'except' operation to connect the queries of subproblems to form the final SQL statement.

SQL query: 
SELECT T1.name FROM station AS T1 JOIN status AS T2 ON T1.id  =  T2.station_id GROUP BY T2.station_id HAVING avg(bikes_available)  >  10 EXCEPT SELECT name FROM station WHERE city  =  "San Jose"


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
Table concert, columns = [*,concert_ID,concert_Name,Theme,Stadium_ID,Year]
Table singer, columns = [*,Singer_ID,Name,Country,Song_Name,Song_release_year,Age,Is_male]
Table singer_in_concert, columns = [*,concert_ID,Singer_ID]
Table stadium, columns = [*,Stadium_ID,Location,Name,Capacity,Highest,Lowest,Average]

## Foreign_keys:
[concert.Stadium_ID = stadium.Stadium_ID,singer_in_concert.Singer_ID = singer.Singer_ID,singer_in_concert.concert_ID = concert.concert_ID]

## Query:
Find the number of concerts happened in the stadium with the highest capacity .

Let's think step by step.

<1> Decomposition: Firstly, we need to find the stadium with the highest capacity. Secondly, we need to filter concerts based on their happened stadium and count them.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. In the first step, we need to select stadium_id with highest capacity from table 'stadium'. In the second step, we need to filter stadium_id from table 'concert' and count them.

<3> SQL Generation: Use 'order by' and 'desc' to select stadium with highest capacity, and then use 'where' to filter concert and count it.

SQL query: select count(*) from concert where stadium_id = (select stadium_id from stadium order by capacity desc limit 1)


## Tables:
{}
## Foreign_keys:
{}
## Query:
{}"""



freeze_prompt5 = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of filtering problem. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
## Tables:
Table Allergy_Type, columns = [*,Allergy,AllergyType]
Table Has_Allergy, columns = [*,StuID,Allergy]
Table Student, columns = [*,StuID,LName,Fname,Age,Sex,Major,Advisor,city_code]

## Foreign_keys:
[Has_Allergy.Allergy = Allergy_Type.Allergy,Has_Allergy.StuID = Student.StuID]

## Query:
How many female students have milk or egg allergies?

Let's think step by step.

<1> Decomposition: Firstly, we filter candidates using column 'Sex' in table 'Student' and column 'Allergy' in table 'Has_Allergy'. Secondly, we use 'count' to calculate the number of selected female students.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. Since table 'Student' and table 'Has_Allergy' have direct foreign keys, so we need tables ['Student', 'Has_Allergy'].

<3> SQL Generation: We need to join the 'Student' and 'Has_Allergy' tables on the 'StuID' column. Then, we filter the rows where 'Sex' is 'F' and 'Allergy' is either 'Milk' or 'Eggs'. Finally, we count the number of rows that meet these conditions.

SQL query: SELECT count(*) FROM has_allergy AS T1 JOIN Student AS T2 ON T1.StuID  =  T2.StuID WHERE T2.sex = 'F' AND T1.allergy = 'Milk' or T1.allergy = 'Eggs'


Example 2:
## Tables:
Table station, columns = [*,id,name,lat,long,dock_count,city,installation_date]
Table status, columns = [*,station_id,bikes_available,docks_available,time]
Table trip, columns = [*,id,duration,start_date,start_station_name,start_station_id,end_date,end_station_name,end_station_id,bike_id,subscription_type,zip_code]
Table weather, columns = [*,date,max_temperature_f,mean_temperature_f,min_temperature_f,max_dew_point_f,mean_dew_point_f,min_dew_point_f,max_humidity,mean_humidity,min_humidity,max_sea_level_pressure_inches,mean_sea_level_pressure_inches,min_sea_level_pressure_inches,max_visibility_miles,mean_visibility_miles,min_visibility_miles,max_wind_Speed_mph,mean_wind_speed_mph,max_gust_speed_mph,precipitation_inches,cloud_cover,events,wind_dir_degrees,zip_code]

## Foreign_keys:
[status.station_id = station.id]

## Query:
What are names of stations that have average bike availability above 10 and are not located in San Jose city?

Let's think step by step.

<1> Question Decomposition: In this step, we contemplate how to decompose the query. The query emphasizes difference set logic, so we can decompose decompose the question into two subproblems: 1. what are names of stations that have average bike availability above 10; 2. what are names of stations that are located in San Jose city. 

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the requirements of the query and the foreign key relationships. To complete the first subproblem, we need to use tables ['station', 'status']. To complete the second subproblem, we need to use table ['station'].

<3> Operation: Due to the need for calculating the average bike availability for different stations, we need to perform a 'GROUP BY' operation on the column 'station_id', filter by perform 'HAVING AVG()' on the column 'bikes_available'. 

<4> SQL Generation: Use 'except' operation to connect the queries of subproblems to form the final SQL statement.

SQL query: 
SELECT T1.name FROM station AS T1 JOIN status AS T2 ON T1.id  =  T2.station_id GROUP BY T2.station_id HAVING avg(bikes_available)  >  10 EXCEPT SELECT name FROM station WHERE city  =  "San Jose"


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
Table concert, columns = [*,concert_ID,concert_Name,Theme,Stadium_ID,Year]
Table singer, columns = [*,Singer_ID,Name,Country,Song_Name,Song_release_year,Age,Is_male]
Table singer_in_concert, columns = [*,concert_ID,Singer_ID]
Table stadium, columns = [*,Stadium_ID,Location,Name,Capacity,Highest,Lowest,Average]

## Foreign_keys:
[concert.Stadium_ID = stadium.Stadium_ID,singer_in_concert.Singer_ID = singer.Singer_ID,singer_in_concert.concert_ID = concert.concert_ID]

## Query:
Find the number of concerts happened in the stadium with the highest capacity .

Let's think step by step.

<1> Decomposition: Firstly, we need to find the stadium with the highest capacity. Secondly, we need to filter concerts based on their happened stadium and count them.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. In the first step, we need to select stadium_id with highest capacity from table 'stadium'. In the second step, we need to filter stadium_id from table 'concert' and count them.

<3> SQL Generation: Use 'order by' and 'desc' to select stadium with highest capacity, and then use 'where' to filter concert and count it.

SQL query: select count(*) from concert where stadium_id = (select stadium_id from stadium order by capacity desc limit 1)


## Tables:
{}
## Foreign_keys:
{}
## Query:
{}"""