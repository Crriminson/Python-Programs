#Print the first n prime numbers where n is given by the user. 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
num = int(input("Enter the number of prime numbers to print: "))

count = 0 
current_num = 2

while count < num:
    if is_prime(current_num):
        print(current_num, end=" ")
        count += 1
    current_num += 1