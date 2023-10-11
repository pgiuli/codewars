inputletters = input('Enter the readable letters: ')
dictionary = []
for i in inputletters:
    dictionary.append(i)

wordsnum = int(input('Enter the amount of words to be tested: '))

words = []
for i in range(wordsnum):
    word = input('Enter a word: ')
    words.append(word.lower())
print(words)


for testedword in words:
    for letter in testedword:
        if letter not in dictionary:
            print('No')
            break
    else:
        print('Yes')
    