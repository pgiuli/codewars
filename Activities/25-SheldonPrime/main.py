from primePy import primes


def is_friend(num):
    if primes.check(num):
        if primes.check(int(str(num)[::-1])):
            return True
        else:
            return False
    else:
        return False
    
print(is_friend(12))

def is_close(num):
    if is_friend(num):
        position = len(primes.between(1, num)) + 1
        if primes.check(position):
            return True
        
print(is_close(1409))
