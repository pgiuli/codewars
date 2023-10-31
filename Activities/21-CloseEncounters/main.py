#I'm proud of this one, ez points

string = input('Enter the string to be checked: ')

chars = []
for i in string:
    try:
        i = int(i)
        chars.append(i)
    except:
        chars.append(i)

def check(chars):
    #firstnum = 0
    index = 0
    for char in chars:
        if type(char) == int:
            #firstnum = char
            for i in range(index+1, index+3):
                if chars[i] == '#':
                    continue
                else:
                    return False
            if char + chars[index+4] == 10:
                return True
            else:
                return False
        index += 1


print(check(chars))




