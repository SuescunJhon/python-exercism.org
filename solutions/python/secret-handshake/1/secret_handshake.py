ACTIONS = ['jump', 'close your eyes', 'double blink', 'wink']

def commands(binary_str):
    is_reverse = binary_str[0]
    binary_str = binary_str[1:]
    result = [ACTIONS[i] for i in range(len(binary_str)) if binary_str[i]=='1']
    if is_reverse == '0':
        result.reverse()
    return result
    