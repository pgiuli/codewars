origin = input('Enter your input: ')

try:
    origin = int(origin)
except:
    origin = origin.upper()
    print(origin)
else:
    print(origin)

#TODO transformation functions