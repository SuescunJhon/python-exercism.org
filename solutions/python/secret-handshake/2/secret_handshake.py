ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']

def commands(binary_str):
    binary = int(binary_str, 2)
    result = []
    for i, action in enumerate(ACTIONS):
        if 1 & (binary >> i):
            result.append(action)

    if 1 & (binary >> 4):
        result.reverse()

    return result