def is_triangle(sides):
    """Return True if the sides can form a triangle.

    :param sides: List[int] - three sides of a triangle
    """
    a, b, c = sides
    sides_greater_than_0 = sum([side > 0 for side in sides]) == 3
    side_smaller_than_sum = a + b >= c and a + c >= b and b + c >= a
    return sides_greater_than_0 and side_smaller_than_sum

def equilateral(sides):
    """Return True if the three sides are equal.

    :param sides: List[int] - three sides of a triangle.
    """
    
    a, b, c = sides
    return  is_triangle(sides) and (a == b == c)


def isosceles(sides):
    """Return True if at least two sides are equal.

    :param sides: List[int] - three sides of a triangle
    """
    a, b, c = sides
    return is_triangle(sides) and (a == b or b == c or a == c)


def scalene(sides):
    """Return True if all three sides are different.

    :param sides: List[int] - three sides of a triangle
    """
    a, b, c = sides
    return is_triangle(sides) and (a != b and a != c and b != c)
