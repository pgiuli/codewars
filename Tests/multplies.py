import math
minimum = int(input())

x = minimum/3

if minimum % 3 == 0:
    y = x
else:
    y = (math.floor(x/3) + 1) * 3

cadena = [y-3, y, y+3]

print(cadena)