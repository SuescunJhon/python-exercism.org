def is_valid(isbn):
    isbn = list(isbn.replace('-', ''))
    if len(isbn) != 10: return False
    if isbn[-1] == 'X': isbn[-1] = '10'
    if not all(val.isdigit() for val in isbn): return False
    result = sum(int(d) * x for d, x in zip(isbn, range(10, 0, -1)))
    return result % 11 == 0
    