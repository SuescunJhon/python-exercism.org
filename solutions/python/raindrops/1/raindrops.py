def convert(number):
    say = ''
    if number % 3 == 0:
        say += 'Pling'
    if number % 5 == 0:
        say += 'Plang'
    if number % 7 == 0:
        say += 'Plong'
    return say if say else str(number)
