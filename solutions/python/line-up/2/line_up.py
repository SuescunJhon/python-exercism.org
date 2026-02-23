def line_up(name, number):
    ending = 'th'
    
    if number % 100 > 13 or number % 100 < 11:
        if number % 10 == 1:
            ending = 'st'
        elif number % 10 == 2:
            ending = 'nd'
        elif number % 10 == 3:
            ending = 'rd'

    return f"{name}, you are the {number}{ending} customer we serve today. Thank you!"
    
    
