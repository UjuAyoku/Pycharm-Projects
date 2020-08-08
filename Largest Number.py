# find the largest number in a list
numbers = [10, 3, 6, 2]
max_num = numbers[0]  # assume the first element of the list is the max number
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)
