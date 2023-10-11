word = input('Enter the word to be guessed: ')

lives = 7
#print(lives)
guessed_letters = []
missing_letters = []

for i in word:
    missing_letters.append(i)

def remove_items(test_list, item): 
    res = [i for i in test_list if i != item] 
    return res 

#TODO: Prevent repetition

#print(missing_letters)
while missing_letters.__len__() != 0 and lives > 0:
    guess_letter = input('Enter a letter: ')
    guessed_letters.append(guess_letter)
    #print(guess_letter)
    if guess_letter in missing_letters:
        missing_letters = remove_items(missing_letters, guess_letter)
        print('Correct!')
        #print(missing_letters)
    else:
        lives -= 1
        print(f'You now have {lives} lives.')

if missing_letters.__len__() == 0:
    print('You Win!')

elif lives == 0:
    print('Game Over')
