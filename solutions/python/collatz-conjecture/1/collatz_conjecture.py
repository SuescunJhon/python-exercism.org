def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    count = 0
    current_value = number
    while current_value != 1:
        if current_value % 2 == 0:
            current_value = current_value / 2
        else:
            current_value = current_value * 3 + 1
        count += 1

    return count
