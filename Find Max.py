def find_max(numbers):
    """
    :param numbers: list of numerical values
    :return: maximum value
    """
    max_num = numbers[0]  # assume the first element of the list is the largest number
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num
