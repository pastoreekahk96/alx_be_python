# Calculate monthly income and annuual projected savings.

monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)

simple_annual_interest_rate = 0.05
projected_savings = monthly_savings* 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected saving after one year, with interest, is: ${projected_savings}")