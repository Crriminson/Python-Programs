# Use filter() to filter out even numbers from a given list. 

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda x: x % 2 != 0, list1)

print(f"The even numbers are: {list(even_numbers)}")