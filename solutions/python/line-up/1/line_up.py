def line_up(name, number):
    last = str(number)[-1]
    second_last = '' if len(str(number)) == 1 else str(number)[-2]
    ordinal = 'th'

    if second_last != '1':
        if last == '1':
            ordinal = 'st'
        elif last == '2':
            ordinal = 'nd'
        elif last == '3':
            ordinal = 'rd'

    return f"{name}, you are the {number}{ordinal} customer we serve today. Thank you!"
    
    
