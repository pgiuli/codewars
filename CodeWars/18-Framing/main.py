phrases = []
while True:
    r = input('Enter a phrase or # to stop')
    if r == '#':
        break
    else:
        phrases.append(r)

output = ['#']



for phrase in phrases:
    words = phrase.split(' ')
    length = 0
    for word in words:
        if len(word) > length: length = len(word)
    length +=2
    if length > len(output[len(output)-1]):
        output[len(output)-1] = '#'*length

    for word in words:
        missing_space = length - 2 - len(word)
        
        output.append(f"#{word}{' '*missing_space}#")
    
    output.append('#'*length)


for i in output:
    print(i)