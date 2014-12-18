import math
import os
import pickle
    
primes_file = 'euler_35_primes_to_million.txt'
primes = []
if os.path.exists( primes_file ):
    with open(primes_file, 'rb') as f:
        primes = pickle.load(f)

for i in xrange(3,1000000):
    if i % 2 == 0 or i in primes:
        continue
    found = False
    for p in primes:
        if p > i or found:
            break
        for x in range(1,int(math.sqrt((i-p)/2))+1):
            if p + 2 * math.pow(x,2) == i:
                found = True
                break
    if not found:
        print i
        break