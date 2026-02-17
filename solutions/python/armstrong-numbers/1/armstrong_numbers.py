def is_armstrong_number(number):
    """Return True if the number is an Armstrong number

    :param number: int
    """
    list_numbers = [int(str_num) for str_num in str(number)]
    sum_numbers = sum([num ** len(list_numbers) for num in list_numbers])
    return number == sum_numbers   
