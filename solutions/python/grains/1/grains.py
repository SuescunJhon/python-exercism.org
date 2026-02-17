def square(number):
    """Calculates the number of grains for a given square.

    :param number: int - number between 1 and 64
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Return the total sum of grains for each square.
    """
    return (2 ** 64) - 1
