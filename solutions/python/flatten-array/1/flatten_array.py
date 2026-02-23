def flatten(iterable):
    if not iterable:
        return iterable

    first = iterable[0]
    rest = iterable[1:]

    if type(first) == list:
        return flatten(first) + flatten(rest)

    if first is None:
        return flatten(rest)
        
    return [first] + flatten(rest)

    