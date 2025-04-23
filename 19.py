# WAP to print prime numbers in the range given by user 

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start_range} and {end_range} are:")

for num in range(start_range, end_range + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end = " ")