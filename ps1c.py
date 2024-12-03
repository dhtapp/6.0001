# This program will try to find the best rate of savings to achieve a down payment on a $1M house in 36 months
# Your savings will be within $100 of the target down payment

# Input: Starting salary
starting_salary = float(input("Enter the starting salary: "))

# Constants
down_payment = 1000000 * 0.25 # 25% down payment on $1M house
rate = 0.04 # Annual rate of return on investment
semi_annual_raise = 0.07 # Semi-annual raise percent
time_frame = 36 # Number of months to run this program

# Initial values
low = 0
high = 1
steps = 0
tolerance = 100 # Within $100
best_savings_rate = None

# Bisection search loop
while True:
    # Reset variables for each simulation
    current_savings = 0
    number_of_months = 0
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12
    mid = (low + high) / 2
    monthly_savings = monthly_salary * mid
    
    # Simulate saving for 36 months
    for month in range(1, time_frame, +1):
        current_savings += current_savings * rate / 12 # Monthly return on investment
        current_savings += monthly_savings # Add monthly savings
        
        # Apply semi-annual raise
        if number_of_months % 6 == 0 and number_of_months != 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12 # Recalculate monthly salary after raise
            monthly_savings = monthly_salary * mid
        
    # Check if current savings is within the $100 tolerance
    if abs(current_savings - down_payment) <= tolerance:
        best_savings_rate = mid
        print(f"Best savings rate: {best_savings_rate}")
        print(f"Steps in bisection search: {steps}")
        break  # Exit the loop once we find the rate within tolerance
    
    # If the bounds converge without matching the target, print a message
    if low >= 0.9999: 
        print("It is not possible to pay the down payment in 3 years.")
        best_savings_rate = None
        break
    
    # Adjust bounds for bisection search
    if current_savings < down_payment:
        low = mid # Too little savings, increase the rate
    else:
        high = mid # Too much savings, decrease the rate
        
    steps += 1
    