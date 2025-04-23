#Write a program to perform addition, subtraction, multiplication, and division on two numbers entered by the user. 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
try: 
    division = num1 / num2
except ZeroDivisionError:
    division = "Error! Division by zero."

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")        
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")