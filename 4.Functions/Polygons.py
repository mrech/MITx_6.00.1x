# Regular Polygons: polysum

def polysum(n, s):
    '''
    Takes the number of sides 'n' and length 's' of a 
    regular polygon as arguments.

    Returns the sum of the area and the square perimeter 
    of the regular polygon rounded to 4 decimals. 
    '''
    import math

    area = (0.25*n*(s**2))/(math.tan(math.pi/n))
    perimeter = n*s
    sum = area + (perimeter**2)

    return round(sum, 4)
