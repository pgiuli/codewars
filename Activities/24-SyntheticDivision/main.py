polinomial = input("Input your polinomial: ")
constant = int(input("Input your constant: "))
list = polinomial.split(' ')
coefs = []
for i in list: coefs.append(int(i))

#print(coefs,constant)


#Apply Ruffini
auxiliars = [0,]
residus = []

for i in range(len(coefs)):
    aux = auxiliars[i]
    residu = coefs[i] + aux
    residus.append(residu)
    auxiliars.append(residu*constant)
    #print(polinomial)
    #print(auxiliars)
    #print(residus)
    
auxiliars[0] = ''
auxiliars.pop()
print(polinomial)
print(auxiliars)
print(residus)

#TODO: Output formatting