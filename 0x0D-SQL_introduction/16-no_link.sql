-- list all records of the table
-- results should display the score and name
-- Records should be listed in descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
