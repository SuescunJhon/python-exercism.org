COLORS = {'black': 0,
         'brown': 1,
         'red': 2,
         'orange': 3,
         'yellow': 4,
         'green': 5,
         'blue': 6,
         'violet': 7,
         'grey': 8,
         'white': 9}

def zeros_prefix(num_zeros):
    if 8 < num_zeros < 13:
        return num_zeros - 9, 'giga'
    if num_zeros > 5: 
        return num_zeros - 6, 'mega'
    if num_zeros > 2:
        return num_zeros - 3, 'kilo'
    return num_zeros, ''

def label(colors):
    zeros = COLORS[colors[2]]
    two_bands = int(f"{COLORS[colors[0]]}{COLORS[colors[1]]}")
    if colors[1] == 'black':
        two_bands //= 10
        zeros += 1
    power, prefix = zeros_prefix(zeros)
    number = two_bands * (10**power)
    return f"{number} {prefix}ohms"
    