from primePy import primes

def prime_position(num):
    return len(primes.between(1, num)) + 1
def reverse(num):
    return int(str(num)[::-1])

def is_friend(num):
    if primes.check(num) and primes.check(reverse(num)):
        return True
    else:
        return False

def is_close(num):
    if is_friend(num):
        if primes.check(prime_position(num)) and primes.check(prime_position(reverse(num))):
            return True
    else:
        return False

def is_relative(num):
    if is_friend(num):
        diglist1=[]
        diglist2=[]
        for i in str(prime_position(num)):
            diglist1.append(int(i))
        diglist1.sort()
        for i in str(prime_position(reverse(num))):
            diglist2.append(int(i))
        diglist2.sort()
        if diglist1 == diglist2:
            return True
        else:
            return False
        
    else:
        return False

def is_sheldon(num):
    if is_friend(num):
        if prime_position(num) == reverse(prime_position(reverse(num))):
            return True
        else:
            return False
    else:
        return False

#TESTS
print(is_friend(17))
print(is_close(1409))
print(is_relative(769))
print(is_sheldon(73))

test = int(input("Enter a number: "))

quality = ''
if is_friend(test):
    quality = 'Friend'
if is_close(test):
    quality = 'Close Friend'
if is_relative(test):
    quality = 'Relative'
if is_sheldon(test):
    quality = 'Sheldon Prime'
if quality == '':
    quality = 'Regular'

print(f"The number {test} is a: {quality}")