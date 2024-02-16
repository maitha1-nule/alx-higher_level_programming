--a querry tha lists all the cities of California that can be found in the database hbtn_0d_usa.
--results stored in assendg order
--not using join
--return true even if available

SELECT 'cities.id', 'cities.name' FROM 'cities', 'states' WHERE 'cities.state_id' = 'states.id' GROUP BY 'cities.id' ASC;
