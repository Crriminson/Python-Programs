#Write a program to check whether a given number is even or odd. 

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else: 
    print(f"{num} is odd")