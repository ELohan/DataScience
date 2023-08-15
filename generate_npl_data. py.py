import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Number of fake mortgage loans to generate
num_loans = 3000

# Lists to store generated data
loan_balances = [random.randint(80000, 300000) for _ in range(num_loans)]
loan_limits = [balance + random.randint(5000, 50000) for balance in loan_balances]
arrears = [random.randint(0, 10000) for _ in range(num_loans)]
loan_types = ['PPR', 'PPR Topup', 'RIP', 'RIP Topup']
loan_type = [random.choice(loan_types) for _ in range(num_loans)]

start_dates = [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_loans)]
end_dates = [fake.date_between(start_date=start_date, end_date='+40y') for start_date in start_dates]

# Generate fake customer names, gender, and addresses
customer_first_names = [fake.first_name() for _ in range(num_loans)]
customer_last_names = [fake.last_name() for _ in range(num_loans)]
genders = [fake.random_element(['Male', 'Female']) for _ in range(num_loans)]
addresses = [fake.street_address() for _ in range(num_loans)]
address_line_2 = [fake.secondary_address() if random.random() < 0.5 else None for _ in range(num_loans)]
counties = [fake.city() for _ in range(num_loans)]

# Limit the security address county to 50 different names
security_address_counties = random.choices(counties, k=num_loans)

# Create a DataFrame
data = {
    'Loan_balance': loan_balances,
    'Loan_limit': loan_limits,
    'Arrears': arrears,
    'Account Number': range(1001, 1001 + num_loans),
    'Start Date': start_dates,
    'End Date': end_dates,
    'Loan Type': loan_type,
    'Customer First Name': customer_first_names,
    'Customer Last Name': customer_last_names,
    'Gender': genders,
    'Address Line 1': addresses,
    'Address Line 2': address_line_2,
    'County': counties,
    'Security Address Line 1': addresses,  # Use same addresses for simplicity
    'Security Address Line 2': address_line_2,  # Use same address_line_2 for simplicity
    'Security Address County': security_address_counties
}

df = pd.DataFrame(data)

# Export DataFrame to a CSV file
df.to_csv('npl_loans.csv', index=False)
