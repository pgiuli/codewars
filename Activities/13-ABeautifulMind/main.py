
#TODO transformation functions

def base26_to_base10(string):
    chars = []
    for char in string:
        chars.append(char)
    num = 0
    index = len(chars)
    for i in chars:
        index -= 1
        #print(index)
        num += (ord(i) - 64) * (26 ** index)
    return num

def base10_to_base26(num):
    chars = []
    while num > 0:
        chars.append(chr((num % 26) + 64))
        num = num // 26
    chars.reverse()
    chars = ''.join(chars)
    return chars

origin = input('Enter your input: ')

try:
    origin = int(origin)
except:
    origin = origin.upper()
    print(base26_to_base10(origin))
else:
    print(base10_to_base26(origin))
