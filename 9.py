#Write a program to create a dictionary with names as keys and marks as values. Print all keys and values.

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

for key in dict1:
    print(f"{key} : {dict1[key]}")