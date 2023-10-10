text = input('Input your text: ')

for i in ['a','e','i','o','u','A','E','I','O','U']:
    text = text.replace(i,'*')

print(text)