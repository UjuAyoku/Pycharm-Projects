# Task: Convert weight from pounds to kilograms and vice versa
weight = int(input('Weight: ' ))
unit = input('(L)bs or (K)g: ')

# convert weight from lbs to kg
if unit.upper() == 'L':
    converter = weight * 0.45359237
    print(f'Your weight is {converter:.2f} kilos')
else:
    converter = weight / 0.45359237
    print(f'Your weight is {converter:.2f} pounds')
