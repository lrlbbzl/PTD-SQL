filter_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of filtering problem. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
## Tables:
Table city, columns = [*,City_ID,Official_Name,Status,Area_km_2,Population,Census_Ranking]
Table competition_record, columns = [*,Competition_ID,Farm_ID,Rank]
Table farm, columns = [*,Farm_ID,Year,Total_Horses,Working_Horses,Total_Cattle,Oxen,Bulls,Cows,Pigs,Sheep_and_Goats]
Table farm_competition, columns = [*,Competition_ID,Year,Theme,Host_city_ID,Hosts]

## Foreign_keys:
[farm_competition.Host_city_ID = city.City_ID,competition_record.Farm_ID = farm.Farm_ID,competition_record.Competition_ID = farm_competition.Competition_ID]

## Query:
Return the hosts of competitions for which the theme is not Aliens?

Let's think step by step.

<1> Decomposition: The query requires filtering on column 'theme', so we should apply the 'where' to column 'theme' and then return the hosts of selected competition.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. Since table 'farm_competition' has columns 'Theme' and 'Hosts', we only need table 'farm_competition'.

<3> SQL Generation: Directly write the sql using 'where'.

SQL query: SELECT Hosts FROM farm_competition WHERE Theme != 'Aliens'


Example 2:
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


Example 3:
## Tables:
Table station, columns = [*,id,name,lat,long,dock_count,city,installation_date]
Table status, columns = [*,station_id,bikes_available,docks_available,time]
Table trip, columns = [*,id,duration,start_date,start_station_name,start_station_id,end_date,end_station_name,end_station_id,bike_id,subscription_type,zip_code]
Table weather, columns = [*,date,max_temperature_f,mean_temperature_f,min_temperature_f,max_dew_point_f,mean_dew_point_f,min_dew_point_f,max_humidity,mean_humidity,min_humidity,max_sea_level_pressure_inches,mean_sea_level_pressure_inches,min_sea_level_pressure_inches,max_visibility_miles,mean_visibility_miles,min_visibility_miles,max_wind_Speed_mph,mean_wind_speed_mph,max_gust_speed_mph,precipitation_inches,cloud_cover,events,wind_dir_degrees,zip_code]

## Foreign_keys:
[status.station_id = station.id]

## Query:
How many trips did not end in San Francisco?

Let's think step by step.

<1> Decomposition: The query requires filtering on trips that did not end in San Francisco. Firstly, we need to identify the stations located in San Francisco. Secondly, we need to filter trips based on their end_station_id.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. In the first step, we need to select id from table 'station' where city = 'San Francisco'. In the second step, we need to select id from table 'trip' and filter by end_station_id.

<3> SQL Generation: Use 'where' to filter stations in San Francisco, and then use 'not in' to filter trips that did not end in San Francisco.

SQL query: SELECT COUNT(*) FROM trip WHERE end_station_id NOT IN (SELECT id FROM station WHERE city = 'San Francisco')


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


Example 5:
## Tables:
Table station, columns = [*,id,name,lat,long,dock_count,city,installation_date]
Table status, columns = [*,station_id,bikes_available,docks_available,time]
Table trip, columns = [*,id,duration,start_date,start_station_name,start_station_id,end_date,end_station_name,end_station_id,bike_id,subscription_type,zip_code]
Table weather, columns = [*,date,max_temperature_f,mean_temperature_f,min_temperature_f,max_dew_point_f,mean_dew_point_f,min_dew_point_f,max_humidity,mean_humidity,min_humidity,max_sea_level_pressure_inches,mean_sea_level_pressure_inches,min_sea_level_pressure_inches,max_visibility_miles,mean_visibility_miles,min_visibility_miles,max_wind_Speed_mph,mean_wind_speed_mph,max_gust_speed_mph,precipitation_inches,cloud_cover,events,wind_dir_degrees,zip_code]

## Foreign_keys:
Foreign_keys = [status.station_id = station.id]

## Query:
Which days had a minimum dew point smaller than any day in zip code 94107, and in which zip codes were those measurements taken?

Let's think step by step.

<1> Decomposition: Firstly, we need to find the minimum dew point in zip code 94107. Secondly, we need to filter days with minimum dew point smaller than the value found in the first step and find the corresponding zip codes.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the first step and the foreign key relationships. In the first step, we need to select min_dew_point_f from table 'weather' where zip_code = 94107. In the second step, we need to filter min_dew_point_f and zip_code from table 'weather'.

<3> SQL Generation: Use 'where' to find the minimum dew point in zip code 94107, and then use 'where' to filter days with minimum dew point smaller than the value found in the first step and select the corresponding zip codes.

SQL query: SELECT date, zip_code FROM weather WHERE min_dew_point_f < (SELECT MIN(min_dew_point_f) FROM weather WHERE zip_code = 94107)


## Tables:
{}
## Foreign_keys:
{}
## Query:
{}

Let's think step by step.

"""


filter_search_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of filtering problem. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
{}


{}
Let's think step by step.
"""