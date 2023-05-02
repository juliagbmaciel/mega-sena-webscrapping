create database loteria;
use loteria;

CREATE TABLE resultados (
	ano_sorteio int,
    num_sorteio INTEGER NOT NULL PRIMARY KEY,
    num1 INT ,
    num2 INT ,
    num3 INT ,
    num4 INT ,
    num5 INT ,
    num6 INT 
);
SELECT * FROM resultados;
