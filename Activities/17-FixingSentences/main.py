initial_phrase = input('Enter your phrase: ')[:-1]
words = initial_phrase.split(' ')

reversed_indexes = []

while True:
    index = input("Enter an index to reverse or # to stop: ")
    if index == '#':
        break
    else:
        reversed_indexes.append(int(index) - 1) #they start counting at 1 smh...


for index in reversed_indexes:
    word = words[index]
    word = word[::-1] #thank you geeksforgeeks

    words[index] =  word

final_phrase = f"{' '.join(words)}."
print(final_phrase)