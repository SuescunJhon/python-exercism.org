def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = sum(factors(number))
    clasifications = {aliquot_sum == number: "perfect",
                     aliquot_sum < number: "deficient",
                     aliquot_sum > number: "abundant"}
    
    return clasifications[True]

def factors(number):
    """Return the factors of a number

    :param number: int
    """
    half = number // 2
    number_factors = [div for div in range(1, half+1) if number % div == 0]
    return number_factors
