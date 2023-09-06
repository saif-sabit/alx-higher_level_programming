-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
-- Use our database
use 'hbtn_0d_usa';
-- Create table states 
CREATE TABLE IF NOT EXISTS cities(
        id NOT NULL PRIMARY KEY,
        state_id INT FOREIGN KEY REFERENCES states(id),
        name NOT NULL VARCHAR(256));