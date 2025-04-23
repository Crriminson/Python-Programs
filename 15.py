#Accept a character from the user and determine whether it’s a vowel or consonant.

char = input("Enter a character: ").lower()

vowels = "aeiou"
alphabet = 'abcdefghijklmnopqrstuvwxyz'


if char in alphabet:
    if char in vowels:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a letter from the English alphabet.")