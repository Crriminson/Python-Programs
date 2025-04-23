#Write a program to convert a number from decimal to binary, octal, and hexadecimal. 

num = int(input("Enter a decimal number: "))

binary = bin(num)
octal = oct(num)
hexadecimal = hex(num)

print(f"Binary: {binary[2:]}")
print(f"Octal: {octal[2:]}")
print(f"Hexadecimal: {hexadecimal[2:].upper()}")

# [2:] is used to remove the '0b', '0o', and '0x' prefixes from the binary, octal, and hexadecimal representations respectively.
# The .upper() method is used to convert the hexadecimal representation to uppercase.