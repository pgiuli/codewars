nums = []
while True:
    num = input('Enter a number or # to stop: ')
    if num == '#':
        break
    else:
        nums.append(int(num))

print(nums)


#Sums

for i in range(len(nums)):
    exclnums = nums
    exclnums =  exclnums[:i] + exclnums[i+1 :]

    sumres = 0
    for i in exclnums:
        sumres += i

    print(f'Sum: {sumres}')
    
    multres = 1
    for i in exclnums:
        multres = multres * i
    
    print(f'Mult: {multres}')
