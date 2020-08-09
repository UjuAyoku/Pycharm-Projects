# Exercise 3
"""
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total 
number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
"""


def speed_checker(speed):
    demerits = 0
    if speed < 70:
        print('Ok')
    elif speed > 70:
        extra = speed - 70
        points = extra // 5
        demerits += points
        print(f'Demerit points: {demerits}')
        if demerits > 12:
            print('License suspended')
