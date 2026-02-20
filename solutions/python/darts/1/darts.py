import math

def score(x, y):
    """Return the points scored for a single toss

    :param x: float - x coordinate
    :param y: float - y coordinate
    """

    calculated_radius = math.sqrt(x**2 + y**2)

    if calculated_radius <= 1:
        return 10
    elif calculated_radius <= 5:
        return 5
    elif calculated_radius <= 10:
        return 1
    else:
        return 0

    
