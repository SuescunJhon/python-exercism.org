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

TOLERANCES = {'grey': '±0.05%',
             'violet': '±0.1%',
             'blue': '±0.25%',
             'green': '±0.5%',
             'brown': '±1%',
             'red': '±2%',
             'gold': '±5%',
             'silver': '±10%',}

def resistor_label(colors):
    if len(colors) == 1: return '0 ohms' 
    ohms = 0
    prefix = ''
    tolerance = TOLERANCES[colors[-1]]
    
    if len(colors) == 5:
        ohms = int(f"{COLORS[colors[0]]}{COLORS[colors[1]]}{COLORS[colors[2]]}")
        ohms *= 10 ** COLORS[colors[3]]
    else:
        ohms = int(f"{COLORS[colors[0]]}{COLORS[colors[1]]}")
        ohms *= 10 ** COLORS[colors[2]]

    if ohms >= 1_000_000_000:
        prefix = 'giga'
        ohms /= 1_000_000_000
    elif ohms >= 1_000_000:
        prefix = 'mega'
        ohms /= 1_000_000
    elif ohms >= 1_000:
        prefix = 'kilo'
        ohms /= 1_000

    return f"{ohms:g} {prefix}ohms {tolerance}"


