acronyms = [
    (('National', 'Aeronautics', 'Space', 'Administration'), 'NASA'),
    (('United', 'States'), 'US'),
    (('Code', 'Wars'), 'CW'),
    (('Hewlett', 'Packard'), 'HP')
    ]  

initial_phrase = input('Enter the phrase: ')[:-1]
print(initial_phrase)
words = initial_phrase.split(' ')
print(words)

for word in words:
    for touple in acronyms:
        if word in touple[0]:
            for inword in touple[0]:
                index = words.index(inword)
                words.pop(index)
            words.insert(index,touple[1])

print(words)
final_phrase = ' '.join(words)
print(f'{final_phrase}.')