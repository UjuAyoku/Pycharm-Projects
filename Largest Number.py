#find the largest number in a list
list_1 = [31,5,6,10,3,20]
max_num = list_1[0] #assume the first element of the list is the max number
for number in list_1:
    if number > max_num:
        max_num = number
print(max_num)