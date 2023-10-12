initialnum = int(input('Enter the initial number (n>1): '))

if initialnum < 1:
    raise ValueError

num = initialnum

steps = 0

string = ''

while num != 1:
    string += f'{num} -> '
    if num % 2 == 0:
        num = round(num/2)
    elif num % 2 == 1:
        num = num * 3 + 1
    steps += 1

string += f'1 [{steps}]'

print(string)
    
    