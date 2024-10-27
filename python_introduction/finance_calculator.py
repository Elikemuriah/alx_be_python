monthly_income = int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your monthly expenses"))

#CALCULATING MONTHLY SAVINGS AND INTERST

monthly_savings = monthly_income - monthly_expenses
monthly_interest = monthly_savings * 0.05

annual_savings = 12*(monthly_savings + monthly_interest)

print('your annual savings will be', annual_savings)
