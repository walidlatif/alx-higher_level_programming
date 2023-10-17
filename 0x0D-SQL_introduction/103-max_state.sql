-- Import in hbtn_0c_0 database this table dump
-- Displays the max temperature of each state (ordered by State name).
SELECT `state`, MAX(`value`) 'max_temp'
FROM `temperatures`
GROUP BY `state`
ORDER BY `state` ASC;
