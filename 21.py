# Create a recursive function to calculate the power a^b (a raised to b).

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
    
power(2, 69)
print(power(2, 69)) 