# This program will calculate how many months it will take to reach your down payment goal
# This update includes getting a salary increase every six months

# Capture the inputs here
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Set Constants
monthly_salary = annual_salary / 12 # Converting annual salary to monthly salary
monthly_savings = monthly_salary * portion_saved # Calculating the monthly savings 
month_counter = 0 # Setting month counter
r = 0.04 # Setting interest rate at 4%
current_savings = 0 # Setting current_savings at $0 to begin with
portion_down_payment = total_cost * 0.25 # Assuming down payment will be 25% of total cost


# Loop -- needs to update & consider salary raises
while current_savings < portion_down_payment: 
    current_savings += current_savings*r/12 # Adding interest to current savings (cumulative)
    current_savings += monthly_savings # Adding fixed monthly savings to current savings before adding to counter
    month_counter += 1 # Increasing month counter
    if month_counter % 6 == 0: # Every 6 months, we're updating the annual_salary value
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved
        #print(f"New salary is: {annual_salary}, and new monthly savings is: {monthly_savings}")
    else:
        pass
else:
    print(f"Number of months: {month_counter}")


# Debuts
#print(f"Your annual salary is: {annual_salary}")
#print(f"Your monthly salary is: {monthly_salary}")
#print(f"Your portion saved is: {portion_saved}")
#print(f"Your monthly savings is: {int(monthly_savings)}")
#print(f"Your total cost is: {total_cost}")
#print(f"Your current savings are: {int(current_savings)}")
#print(f"Your down payment amount is: {int(portion_down_payment)}")