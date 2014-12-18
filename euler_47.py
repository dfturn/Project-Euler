import os
import pickle
import time
    
primes_file = 'euler_35_primes_to_million.txt'
primes = []
if os.path.exists( primes_file ):
    with open(primes_file, 'rb') as f:
        primes = pickle.load(f)

def primeFactors(n):
    factors = set()
    i = 0
    while True:
        if n % primes[i] == 0:
            n = n/primes[i]
            factors.add(primes[i])
            if n == 1:
                break
        elif primes[i] > n:
            break
        else:
            i += 1
    return factors
    
def work():
    ci = 0
    ns = 4
    for i in xrange(200,1000000):
        facs = primeFactors(i)
        if len(facs) == ns: ci += 1
        else: ci = 0
        if ci == 4:
            print i - 3
            print facs
            break
work()