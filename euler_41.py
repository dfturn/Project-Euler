from itertools import permutations
import math

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
        
digits = [str(x) for x in range(1,10)]
found = False
for i in range(9,0,-1):
    pandigitals = reversed(list(permutations(digits[:i], i)))
    for p in pandigitals:
        if isPrime(int(''.join(p))):
            print ''.join(p)
            found = True
            break
    if found:
        break
            