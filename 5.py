# Accept a string input from the user and print it in uppercase and reversed form.

user_input = input("Please enter a string: ")
uppercase_input = user_input.upper()
reversed_input = user_input[::-1]

print("Uppercase:", uppercase_input)
print("Reversed:", reversed_input)