keywords = []
while True:
    x = input('Enter keyword, shift number or # to finish: ')
    if x == '#':
        break
    try:
        x = int(x)
    except:
        keywords.append(x)
    else:
        shift = x

print(keywords,shift)

for i in range(shift):
    keywords.insert(len(keywords)-1,keywords.pop(0))

for i in keywords:
    print(keywords[i])