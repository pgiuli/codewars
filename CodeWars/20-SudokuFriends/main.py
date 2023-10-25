import math
test = '9 8 5 6 3 7 2 1 4 1 3 4 8 2 5 7 6 9 2 7 6 4 9 1 3 5 8 3 4 2 1 7 8 6 9 5 6 1 8 9 5 3 4 7 2 7 5 9 2 6 4 1 8 3 5 2 3 7 1 9 8 4 6 8 6 7 5 4 2 9 3 1 4 9 1 3 8 6 5 2 7'

nums = test.split(' ')
#print(nums)
index = 1
friends = 0

for i in nums:
    i = int(i)
    row = math.ceil(index / 9)
    column = index % 9
    if column == 0:
        column = 9
    
    boxrow = math.ceil(row/3)
    boxcol = math.ceil(column/3)

    #WOOOOOOOOOOOOOOOOOOOOo
    box = 0
    if boxrow == 1:
        box = boxcol
    elif boxrow == 2:
        box = 3 + boxcol
    else:
        box = 6 + boxcol

    #print(box)
    if i == row or i == column or i == box:
        friends += 1
    index += 1

#Boxes





print(friends)