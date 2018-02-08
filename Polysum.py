import math
def polysum(n,s):
    area=n * (s ** 2) / (4 * math.tan(math.pi / n))
    peri=n*s
    return round(area + (peri*peri), 4)
