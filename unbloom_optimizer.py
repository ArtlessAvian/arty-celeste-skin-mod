colors = [0xA0DEFF, 0x82ABD7, 0xFFFFFF, 0xB3B3B3, 0xFFFF94]

def hex_to_channels(val):
    # Yes, i know that the first mod and the last divide do nothing.
    r = (val // 0x010000) % 0x100
    g = (val // 0x000100) % 0x100
    b = (val // 0x000001) % 0x100
    return (r, g, b)

colors = list(hex_to_channels(x) for x in colors)

def loss(base, x):
    the_usual = tuple(min(round(channel * 1.2), 0xFF) for channel in x) 
    old_site = tuple(min(round(channel * 1.5), 0xFF) for channel in x)

    # NOT A GOOD LOSS FUNCTION
    # Boring least squares with some weights
    out = 0
    for (a, b, c, d) in zip(base, x, the_usual, old_site):
        out += (a - b)**2
        out += (a - c)**2 * 5
        out += (a - d)**2
    return out


for color in colors:
    print("-----")
    print(color)

    # Brute forcer. Not a good idea, but it works.
    best_color, best_loss = min((loss(color, x), x) for x in (hex_to_channels(y) for y in range(0xFFFFFF + 1)))

    print(best_color, best_loss)
