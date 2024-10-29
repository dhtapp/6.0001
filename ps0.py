# Solution to pset0
import math

# Get inputs
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

# Perform calculations
x_raised_y = x**y
log_of_x = math.log2(x)

#Outputs go here
print(f"X**y = {x_raised_y}")
print(f"log(x) = {int(log_of_x)}")