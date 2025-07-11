monthly_income = int(input("Enter you monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
fgmonthly_savings = f"${monthly_savings:,.0f}."
projected_savings = monthly_savings * 12 + ( monthly_savings * 12 * 0.05)
fgprojected_savings = f"${projected_savings:,.0f}."
print("Your monthly savings are", fgmonthly_savings)
print("Projected savings after one year, with interest, is:" ,fgprojected_savings)
