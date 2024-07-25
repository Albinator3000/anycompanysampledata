import pandas as pd

# Load revenue data
revenue_data = pd.read_excel('Revenue_Data.xlsx')

def calculate_total_revenue():
    total_revenue = revenue_data['Revenue'].sum()
    print(f"Total Revenue: ${total_revenue}")

def calculate_monthly_revenue(month):
    monthly_revenue = revenue_data[revenue_data['Month'] == month]['Revenue'].sum()
    print(f"Revenue for {month}: ${monthly_revenue}")

# Example usage
calculate_total_revenue()
calculate_monthly_revenue('Jan')
