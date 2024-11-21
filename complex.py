complex_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of set operations. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.


Example 1:
## tables:
Table aircraft, columns = [*,aid,name,distance]
Table certificate, columns = [*,eid,aid]
Table employee, columns = [*,eid,name,salary]
Table flight, columns = [*,flno,origin,destination,distance,departure_date,arrival_date,price,aid]

## foreign_keys
[flight.aid = aircraft.aid,certificate.aid = aircraft.aid,certificate.eid = employee.eid]

## query
Show names for all employees who have certificates on both Boeing 737-800 and Airbus A340-300.

Let's think step by step.

<1> Question Decomposition: In this step, we contemplate how to decompose the query. The query emphasizes intersection logic, so we can decompose the question into two subproblems: 1. what are the names of employees who have certificates on Boeing 737-800; 2. what are the names of employees who have certificates on Airbus A340-300.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the requirements of the query and the foreign key relationships. To complete the first subproblem, we need to use table 'employee' and 'aircraft'. since table 'employee' and table 'aircraft' do not have a direct foreign key connection, we need to use tables ['employee', 'certificate', 'aircraft']. To complete the second subproblem, we need to use tables ['employee', 'certificate', 'aircraft'] in the same reason.

<3> Operation: Use 'where' to filter using column 'name' in table 'aircraft'.

<4> SQL Generation: Use 'intersect' operation to connect the queries of subproblems to form the final SQL statement.

SQL query: SELECT T1.name FROM Employee AS T1 JOIN Certificate AS T2 ON T1.eid  =  T2.eid JOIN Aircraft AS T3 ON T3.aid  =  T2.aid WHERE T3.name  =  "Boeing 737-800" INTERSECT SELECT T1.name FROM Employee AS T1 JOIN Certificate AS T2 ON T1.eid  =  T2.eid JOIN Aircraft AS T3 ON T3.aid  =  T2.aid WHERE T3.name  =  "Airbus A340-300"


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

SQL query: SELECT T1.name FROM station AS T1 JOIN status AS T2 ON T1.id  =  T2.station_id GROUP BY T2.station_id HAVING avg(bikes_available)  >  10 EXCEPT SELECT name FROM station WHERE city  =  "San Jose"


Example 3:
## Tables:
Table Actual_Order_Products, columns = [*,actual_order_id,product_id]
Table Actual_Orders, columns = [*,actual_order_id,order_status_code,regular_order_id,actual_order_date]
Table Addresses, columns = [*,address_id,address_details,city,zip_postcode,state_province_county,country]
Table Customer_Addresses, columns = [*,customer_id,address_id,date_from,address_type,date_to]
Table Customers, columns = [*,customer_id,payment_method,customer_name,customer_phone,customer_email,date_became_customer]
Table Delivery_Route_Locations, columns = [*,location_code,route_id,location_address_id,location_name]
Table Delivery_Routes, columns = [*,route_id,route_name,other_route_details]
Table Employees, columns = [*,employee_id,employee_address_id,employee_name,employee_phone]
Table Order_Deliveries, columns = [*,location_code,actual_order_id,delivery_status_code,driver_employee_id,truck_id,delivery_date]
Table Products, columns = [*,product_id,product_name,product_price,product_description]
Table Regular_Order_Products, columns = [*,regular_order_id,product_id]
Table Regular_Orders, columns = [*,regular_order_id,distributer_id]
Table Trucks, columns = [*,truck_id,truck_licence_number,truck_details]

## Foreign_keys:
[Regular_Orders.distributer_id = Customers.customer_id,Regular_Order_Products.regular_order_id = Regular_Orders.regular_order_id,Regular_Order_Products.product_id = Products.product_id,Actual_Orders.regular_order_id = Regular_Orders.regular_order_id,Actual_Order_Products.actual_order_id = Actual_Orders.actual_order_id,Actual_Order_Products.product_id = Products.product_id,Customer_Addresses.address_id = Addresses.address_id,Customer_Addresses.customer_id = Customers.customer_id,Delivery_Route_Locations.route_id = Delivery_Routes.route_id,Delivery_Route_Locations.location_address_id = Addresses.address_id,Employees.employee_address_id = Addresses.address_id,Order_Deliveries.driver_employee_id = Employees.employee_id,Order_Deliveries.location_code = Delivery_Route_Locations.location_code,Order_Deliveries.actual_order_id = Actual_Orders.actual_order_id,Order_Deliveries.truck_id = Trucks.truck_id]

## Query:
Find the names of customers who are not living in the state of California.

Let's think step by step.

<1> Question Decomposition: In this step, we contemplate how to decompose the query. The query emphasizes difference set logic, so we can decompose the question into two subproblems: 1. what are the names of all customers; 2. what are the names of customers who are living in the state of California.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the requirements of the query and the foreign key relationships. To complete the first subproblem, we need to use table ['Customers']. To complete the second subproblem, we need to use tables ['Customers', 'Customer_Addresses', 'Addresses'].

<3> Operation: Use 'where' to filter using column 'state_province_county' in table 'Addresses'.

<4> SQL Generation: Use 'except' operation to connect the queries of subproblems to form the final SQL statement.

SQL query: SELECT customer_name FROM customers EXCEPT SELECT t1.customer_name FROM customers AS t1 JOIN customer_addresses AS t2 ON t1.customer_id  =  t2.customer_id JOIN addresses AS t3 ON t2.address_id  =  t3.address_id WHERE t3.state_province_county  =  'California'


Example 4:
## Tables:
Table circuits, columns = [*,circuitId,circuitRef,name,location,country,lat,lng,alt,url]
Table constructorResults, columns = [*,constructorResultsId,raceId,constructorId,points,status]
Table constructorStandings, columns = [*,constructorStandingsId,raceId,constructorId,points,position,positionText,wins]
Table constructors, columns = [*,constructorId,constructorRef,name,nationality,url]
Table driverStandings, columns = [*,driverStandingsId,raceId,driverId,points,position,positionText,wins]
Table drivers, columns = [*,driverId,driverRef,number,code,forename,surname,dob,nationality,url]
Table lapTimes, columns = [*,raceId,driverId,lap,position,time,milliseconds]
Table pitStops, columns = [*,raceId,driverId,stop,lap,time,duration,milliseconds]
Table qualifying, columns = [*,qualifyId,raceId,driverId,constructorId,number,position,q1,q2,q3]
Table races, columns = [*,raceId,year,round,circuitId,name,date,time,url]
Table results, columns = [*,resultId,raceId,driverId,constructorId,number,grid,position,positionText,positionOrder,points,laps,time,milliseconds,fastestLap,rank,fastestLapTime,fastestLapSpeed,statusId]
Table seasons, columns = [*,year,url]
Table status, columns = [*,statusId,status]

## Foreign_keys:
[races.circuitId = circuits.circuitId,constructorStandings.raceId = races.raceId,constructorStandings.constructorId = constructors.constructorId,results.driverId = drivers.driverId,results.raceId = races.raceId,results.constructorId = constructors.constructorId,driverStandings.driverId = drivers.driverId,driverStandings.raceId = races.raceId,constructorResults.raceId = races.raceId,constructorResults.constructorId = constructors.constructorId,qualifying.driverId = drivers.driverId,qualifying.raceId = races.raceId,qualifying.constructorId = constructors.constructorId,pitStops.driverId = drivers.driverId,pitStops.raceId = races.raceId,lapTimes.driverId = drivers.driverId,lapTimes.raceId = races.raceId]

## Query:
What are the drivers' first, last names and id who had more than 8 pit stops or participated in more than 5 race results?

Let's think step by step.

<1> Question Decomposition: In this step, we contemplate how to decompose the query. The query emphasizes union logic, so we can decompose the question into two subproblems: 1. what are the drivers' first, last names, and id who had more than 8 pit stops; 2. what are the drivers' first, last names, and id who participated in more than 5 race results.

<2> Schema Linking: In this step, we identify the tables and columns that should be used based on the requirements of the query and the foreign key relationships. To complete the first subproblem, we need to use tables ['drivers', 'pitStops']. To complete the second subproblem, we need to use tables ['drivers', 'results'].

<3> Operation: For the first subproblem, we need to perform a 'GROUP BY' operation on the column 'driverId' and filter by performing 'HAVING COUNT()' on the column 'stop'. For the second subproblem, we need to perform a 'GROUP BY' operation on the column 'driverId' and filter by performing 'HAVING COUNT()' on the column 'raceId'.

<4> SQL Generation: Use 'union' operation to connect the queries of subproblems to form the final SQL statement.

SQL query: SELECT T1.forename ,  T1.surname ,  T1.driverid FROM drivers AS T1 JOIN pitstops AS T2 ON T1.driverid  =  T2.driverid GROUP BY T1.driverid HAVING count(*)  >  8 UNION SELECT T1.forename ,  T1.surname ,  T1.driverid FROM drivers AS T1 JOIN results AS T2 ON T1.driverid  =  T2.driverid GROUP BY T1.driverid HAVING count(*)  >  5


## Tables:
{}

## Foreign_keys:
{}

## Query:
{}

Let's think step by step.

"""

complex_search_prompt = """You are a powerful text-to-SQL reasoner. Currently, I am seeking to transform intricate text queries into analytical statements that simplify the creation of SQL statements, leading to the generation of the final SQL query. Our current focus lies in the category of set operations. Please learn from the provided examples, design a detailed plan for the text query, and present the resulting SQL query.

Example 1:
{}

Example 2:
{}

Example 3:
{}

Example 4:
{}

{}
Let's think step by step.
"""