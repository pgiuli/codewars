valid = ["Rustica", "Romana",
"Prosciutto e funghi", "Funghi",
"Pesto Genovese", "Bianca",
"Carbonara", "Sicilian",
"California", "Hawaiian",
"Pinsa Romana", "Caprese",
"Vegetariana", "Quattro formaggi",
"Diavola", "Pepperoni",
"Quattro stagioni", "Calzone",
"Frutti di mare", "Margherita",
"Prosciutto", "Napoletana"]

validlist = []
invalidlist = []

while True:
    pizza = input('Enter your pizza type: ')
    if pizza == '#':
        break
    else:
        if pizza in valid:
            validlist.append(pizza)
        else:
            invalidlist.append(pizza)

validlist.sort()



print(f"Recieved valid pizza requests: {len(validlist)}")
for entry in validlist:
    print(f"{entry}: {validlist.count(entry)}")
    for i in range(validlist.count(entry)-1):
        validlist.pop(0)
print("---")
print(f"Invalid requests: {invalidlist.__len__()}")
for i in invalidlist:
    print(i)