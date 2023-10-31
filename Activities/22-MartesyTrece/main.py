import math
year = int(input('Enter the year to be checked: '))

#TODO:Handling for leap years.
for i in range(1,366):
    D = i
    if D <= 31:
        M = 1
    elif D <= 59:
        M = 2
    elif D <= 90:
        M = 3
    elif D <= 120:
        M = 4
    elif D <= 151:
        M = 5
    elif D <= 181:
        M = 6
    elif D <= 212:
        M = 7
    elif D <= 243:
        M = 8
    elif D <= 273:
        M = 9
    elif D <= 304:
        M = 10
    elif D <= 334:
        M = 11
    else:
        M = 12

    Y = year
    if M == 1 or M == 2:
        M += 12
        Y -= 1

    K = Y % 100
    C = math.floor(Y // 100)

    W = (D + math.floor(2.6 * M - 5.39) + K + math.floor(K / 4) + math.floor(C / 4) - 2 * C) % 7
    

    if M > 12:
        M -= 12
        Y += 1
    
    print(W,D,M,Y)

    