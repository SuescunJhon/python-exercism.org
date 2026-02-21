def is_valid(isbn):

    scrubbed = isbn.replace('-', '')
    
    if len(scrubbed) != 10: 
        return False
    
    numbers = []
    for i in range(len(scrubbed) - 1):
        if not scrubbed[i].isdigit(): 
            return False
        numbers.append(int(scrubbed[i]))

    if scrubbed[-1] == 'X':
        numbers.append(10)
    elif scrubbed[-1].isdigit():
        numbers.append(int(scrubbed[-1]))
    else:
        return False

    result = 0
    count = 10
    for num in numbers:
        result += num * count
        count -= 1

    return result % 11 == 0
    