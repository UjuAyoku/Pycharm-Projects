# Exercise 5
"""
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
"""


def multiples(limit):
    result = 0
    for number in range(0, limit + 1):
        if number % 3 == 0 or number % 5 == 0:
            result += number
    return result
