def convert(number):
    """Return the sound of a raindrop for a given number

    :param number: int 
    """
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    
    say = ''.join([
        value
        for key, value 
        in sounds.items()
        if number % key == 0
    ])

    return say or str(number)
