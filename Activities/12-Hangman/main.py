word = input('Enter the word to be guessed: ').upper()
tried_string = input('Enter letters to guess: ').upper()
lives = 7

word_letters = []
for i in word:
    word_letters.append(i)
tried_letters = []
for i in tried_string:
    tried_letters.append(i)


print('_' * len(word))

result = []
for letter in tried_letters:
    if letter not in word_letters:
        if lives != 0:
            lives -= 1

for letter in word_letters:
    if letter in tried_letters:
        result.append(letter)
    else:
        result.append('_')

print(''.join(result))

if result == word_letters:
    print('Player wins!')
elif lives > 0:
    print('Word not completed and player is still alive.')
else:
    print('Player Loses.')

print(f'Lives: {lives}')