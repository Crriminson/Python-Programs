# Write a function that returns the sum and average of a list. 

def sum_and_average(lst):
    total = sum(lst)
    average = total / len(lst) if lst else 0
    return total, average

list1 = [1, 2, 3, 4, 5]

total, average = sum_and_average(list1)

print(f"Sum: {total}, Average: {average}")