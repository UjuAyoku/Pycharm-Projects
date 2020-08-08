# convert numbers to words
phone = input('Phone: ')

digit_mapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}

words = ''
for number in phone:
    words += digit_mapping.get(number, '!') + ' '  # to space out the words
print(words)
