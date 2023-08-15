-- create DB
Create database npl_debt;

-- use DB
USE npl_debt;

-- select all
SELECT * FROM npl_debt;

-- alter our column names - swap balance and limit column names- it is more realistic for balance figure to exceed the limit figure for NPL loans
ALTER TABLE npl_debt RENAME COLUMN Loan_balance TO Loan_limit_;
ALTER TABLE npl_debt RENAME COLUMN Loan_limit TO Loan_balance;
ALTER TABLE npl_debt RENAME COLUMN Loan_limit_ TO Loan_limit;

-- select all to check change has implemented
SELECT * FROM npl_debt;

-- drop Arrears column as the values were randomly generated and we want to calculate them accurately
ALTER TABLE npl_debt DROP COLUMN Arrears;

-- re- add an arrears column
ALTER TABLE npl_debt
ADD Arrears int;

-- disable mysql safe updates to allow query to execute
SET SQL_SAFE_UPDATES = 0;

-- Calculate and update the 'Arrears' column with accurate values by finding difference between Balance & Limit
UPDATE npl_debt
SET Arrears = loan_limit - loan_balance; 

-- Calculate and update the 'Arrears' column with accurate values (Remove the - operator)
UPDATE npl_debt
SET Arrears = Arrears * -1

-- re-enable mysql safe updates as this is a worthwhile feature
SET SQL_SAFE_UPDATES = 1;

-- select all to check change has implemented
SELECT * FROM npl_debt;

-- reorder columns for better visibility
alter table npl_debt MODIFY Arrears int after Loan_balance;

-- Rename all columns that contain Mysql keywords - this will make it easier to create our tables
ALTER TABLE npl_debt
CHANGE COLUMN `Start Date` Start_Date DATE,
CHANGE COLUMN `End Date` End_Date DATE,
CHANGE COLUMN `Account Number` Account_Number int,
CHANGE COLUMN `Customer First Name` Cust_First_Name text,
CHANGE COLUMN `Customer Last Name` Cust_Last_Name text,
CHANGE COLUMN `Loan Type` Loan_Type text,
CHANGE COLUMN `Security Address Line 1` Security_Address_Line_1 text,
CHANGE COLUMN `Security Address Line 2` Security_Address_Line_2 text,
CHANGE COLUMN `Security Address County` Security_Address_County text,
CHANGE COLUMN `Address Line 1` Address_Line_1 text,
CHANGE COLUMN `Address Line 2` Address_Line_2 text;

-- create a database in 3rd Normal Form -- 3 tables-- loans, customers, securities
-- create table called loans
CREATE TABLE Loans AS
SELECT Loan_limit, Loan_balance, Arrears, Account_Number, Start_Date, End_Date, Loan_Type
FROM npl_debt;

-- create table called customers
CREATE TABLE Customers AS
SELECT Cust_First_Name, Cust_Last_Name, Gender, Address_Line_1, Address_Line_2, County
FROM npl_debt;

-- create table called securities
CREATE TABLE Securities AS
SELECT Security_Address_Line_1, Security_Address_Line_2, Security_Address_County
FROM npl_debt;

-- Select all from each of our newly created tables
SELECT * FROM Loans
SELECT * FROM Customers
SELECT * FROM Securities

-- Add new primary key columns to the tables
ALTER TABLE loans
ADD Loan_id INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE Customers
ADD Customer_id INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE Securities
ADD Security_id INT AUTO_INCREMENT PRIMARY KEY;

-- Alter the loans table to add foreign keys
ALTER TABLE loans
ADD Customer_id INT,
ADD FOREIGN KEY (Customer_id) REFERENCES Customers(Customer_id),
ADD Security_id INT,
ADD FOREIGN KEY (Security_id) REFERENCES Securities(Security_id);

-- Select all from each of our newly created tables
SELECT * FROM Loans
SELECT * FROM Customers
SELECT * FROM Securities
