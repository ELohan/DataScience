Project Title:
Data Cleaning / Engineering Project in SQL.

Description:
Data Generation of non-performing loans using the Python Faker Library,
followed by export and data engineering in MySQL Workbench

Requirements:
Python 3.10
Faker Package
MySQL Workbench

Step By Step:
>Run python file 'generate_npl_data.py' to create CSV file of NPL Loans
>Open mysql file 'npl_loans_clean_fe'
>Run 1st query to create DB called 'npl_debt'
>Right click on the 'npl_debt' DB in Schemas Navigator 
& select Table Data Import Wizard
>Follow Instructions to import the previously created CSV file
> Run the remaining queries in sequence to Clean and Feature Engineer
the data, and create a database in the 3rd normal form