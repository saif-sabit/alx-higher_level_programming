-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
-- Use our database
use 'hbtn_0d_usa';
-- Create table states 
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name NOT NULL VARCHAR(256));