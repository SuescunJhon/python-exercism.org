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

def label(colors):
    c = colors
    ohm = int(f"{COLORS[c[0]]}{COLORS[c[1]]}") * (10 ** COLORS[c[2]])
    prefix = ''

    if ohm >= 1_000_000_000:
        prefix = 'giga'
        ohm //= 1_000_000_000
    elif ohm >= 1_000_000:
        prefix = 'mega'
        ohm //= 1_000_000
    elif ohm >= 1_000:
        prefix = 'kilo'
        ohm //= 1_000

    return f"{ohm} {prefix}ohms"