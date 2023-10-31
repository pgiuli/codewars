acronyms = [
    ('National Aeronautics Space Administration', 'NASA'),
    ('United States', 'US'),
    ('Code Wars', 'CW'),
    ('Hewlett Packard', 'HP')
    ]  

phrase = input('Enter the phrase: ')
#print(phrase)

#words = phrase.split(' ')
#print(words)

for touple in acronyms:
    if touple[0] in phrase:
        phrase = phrase.replace(touple[0], touple[1])



#Don't look at me weird, it works.
#for word in words:
#    for touple in acronyms:
#        if word in touple[0]:
#            for inword in touple[0]:
#                index = words.index(inword)
#                words.pop(index)
#            words.insert(index,touple[1])


#print(words)

print(phrase)