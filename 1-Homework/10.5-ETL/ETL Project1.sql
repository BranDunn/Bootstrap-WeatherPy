CREATE DATABASE home_pop;

USE home_pop;

CREATE TABLE pop(
	id INT PRIMARY KEY,
	period DATE,
	population INT
	)
;

CREATE TABLE home(
id INT PRIMARY KEY,
period DATE,
ownership_rate FLOAT
)
;