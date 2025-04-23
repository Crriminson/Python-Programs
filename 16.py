#Write a program to print all factors of a number entered by the user.

num = int(input("Enter a number:"))

factors = set()

for i in range(1, (num // 2) + 1):
    if num % i == 0:
        factors.add(i)
        factors.add(num // i)

factors = sorted(factors)
        
print(f"Factors of {num} are: ")
print(factors)