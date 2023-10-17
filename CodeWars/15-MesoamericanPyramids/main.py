num = int(input('Enter the amount of pyramids to analyze :'))

items = []
for i in range(num):
    items.append(input('Input pyramid info: '))


for pyramid in items:
    stringlist = pyramid.split(' ')
    name = stringlist.pop(0)
    for i in range(int((len(stringlist)-1)/2)):
        if stringlist[i] != stringlist[-(i+1)]:
            print(f'{name} has NOT the same number of steps for both faces')
            break
        else:
            continue
    else:
        print(f'{name} has the same number of steps for both faces')
