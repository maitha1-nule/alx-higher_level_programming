--script meant to list cities in the database
--results must be sorted
--reults sorted inassending order

SELECT 'cities.id' 'cities.name' 'states.nam' FROM 'cities', 'states' WHERE 'cities.state_id' = 'states.id' AND 'states.name' = 'California' ORDER BY 'cities.id' ASC;
