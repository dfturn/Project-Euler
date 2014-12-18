import math
import os
import pickle
import time

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
    
primes_file = 'euler_35_primes_to_million.txt'
primes = []
if os.path.exists( primes_file ):
    with open(primes_file, 'rb') as f:
        primes = pickle.load(f)
if len(primes) == 0:
    for i in range(1000000):
        if is_prime(i):
            primes.append(i)
        
    with open(primes_file, 'wb') as f:
        pickle.dump(primes, f)

primes = set(primes)
rot_time = 0
loop_time = 0
def getRotations( prime ):
    start = time.time()
    rotations = [str(prime)]
    for i in range(1,len(rotations[-1])):
        rotations.append(rotations[-1][1:] + rotations[-1][0])
    return map(int, rotations)
    rot_time += time.time() - start

realPrimes = set()
i = 0
for p in primes:
    start = time.time()
    #print rot_time, loop_time
    i += 1
    #if i % 200 == 0: print i
    if p in realPrimes:
        continue
    rotations = getRotations(p)
    if all(map(lambda r: r in primes, rotations)):
        for r in rotations:
            realPrimes.add( r )
    loop_time += time.time() - start
print realPrimes
#realPrimes[] = [p for p in primes if getRotations(p)

    