# Write a program to check if a number is a perfect number.

# A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
# For example, the first perfect number is 6, which is the sum of its divisors 1, 2, and 3.

num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(f"{num} is a perfect number.")    
else:
    print(f"{num} is not a perfect number.")