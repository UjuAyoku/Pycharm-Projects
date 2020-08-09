# Exercise 2
"""
Write a function called fizz_buzz that takes a number. 
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.
"""


def fizz_buzz(number):
    try:
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        else:
            return number
    except TypeError:
        print('Incorrect input. Enter a number.')
