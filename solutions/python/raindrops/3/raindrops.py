def convert(number):
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
