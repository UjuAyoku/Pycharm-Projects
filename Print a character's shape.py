print("Convert a list to the shape of letter 'F'")
numbers = [6,2,6,2,2]
for x_count in numbers:
    print('X' * x_count)

print('Alternate solution')
#Using an inner loop to solve this:
numbers_1 = [6,2,6,2,6]
for x_count in numbers_1:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)

print("Example 2: convert the list to the shape of letter 'L'")
#convert a list to the shape of letter 'L'
numbers = [2,2,2,6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)