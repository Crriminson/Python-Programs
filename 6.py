#Write a Python program to demonstrate the use of a list. Perform append, pop, and slicing operations

list = [1, 2, 3, 4, 5]
print("Original list:", list)

# Append operation
list.append(6)
print("List after appending 6:", list)

# Pop operation
popped_element = list.pop()
print("Popped element:", popped_element)
print("List after popping an element:", list)

# Slicing operation
sliced_list = list[1:4]
print("Sliced list (elements from index 1 to 3):", sliced_list)