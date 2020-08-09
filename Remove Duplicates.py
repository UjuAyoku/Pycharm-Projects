# Task: remove the duplicates in a list
numbers = [1, 3, 4, 4, 7, 6, 7]
new_list = []

if not numbers:
    print('Empty list')
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)
