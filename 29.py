# Write a Python Program that does the following task Ask the user to enter a number as an input Use math module to calculate Square root of a number. 

import math

num = float(input("Enter a number: "))

sqrt_num = math.sqrt(num)
print(f"The square root of {num} is {sqrt_num:.2f}")