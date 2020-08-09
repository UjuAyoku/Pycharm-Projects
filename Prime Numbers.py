# Exercise 7
"""
Write a function that prints all the prime numbers between 0 and limit.
where limit is a parameter.
"""


def prime_num(limit):
    if limit > 1:  # all prime numbers are greater than 1
        for num in range(2, limit + 1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
    else:
        print(limit, 'is not a prime number')
