def is_triangle(f):
    def inner(sides):
        a, b, c = sorted(sides)
        return f(sides) and (a + b > c)
    return inner
    
@is_triangle
def equilateral(sides):
    """Return True if the three sides are equal.

    :param sides: List[int] - three sides of a triangle.
    """
    
    return len(set(sides)) == 1

@is_triangle
def isosceles(sides):
    """Return True if at least two sides are equal.

    :param sides: List[int] - three sides of a triangle
    """
    return len(set(sides)) < 3

@is_triangle
def scalene(sides):
    """Return True if all three sides are different.

    :param sides: List[int] - three sides of a triangle
    """

    return len(set(sides)) == 3
