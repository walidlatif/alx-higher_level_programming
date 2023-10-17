-- Import in hbtn_0c_0 database this table dump:
-- Displays the average temperature (Fahrenheit) by 
	-- city ordered by temperature (descending)
--SELECT city, AVG(value) AS average
--FROM temperatures
--GROUP BY city
--ORDER BY average DESC;
SELECT `city`, AVG(`value`) 'avg_temp' FROM `temperatures` WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
