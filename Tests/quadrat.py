intents = 2
while True:
    if intents > 0:
        num = int(input('Enter a number: '))
        if num > 0:
            print(num**2)
        else:
            intents -= 1
    else:
        break
print("T'has quedat sense intents")