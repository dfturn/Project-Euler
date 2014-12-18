import math
import time
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# Sieve of Eratosthenes. Let's finally use it.
def sieve(n):
    li = [True for x in xrange(0,n)]
    for i in xrange(2,int(math.sqrt(n))+1):
        if li[i]:
            for j in xrange(i**2,n,i):
                li[j] = False
    return [i+2 for i,x in enumerate(li[2:]) if x == True]

primes = sieve(1000000)
longest = 0
#print len(sorted((primes[i:j] for i in range(0,len(primes)) for j in range(i,len(primes)) if sum(primes[i:j]) in primes),cmp=lambda x, y: cmp(len(x), len(y)), reverse=True)[0])
li = []
currentSum = 0
for i in range(len(primes)-1,-1,-1):
    for j in range(1,i-1):
        for k in range(1,i-j-1):
            if sum(primes[i-j-k:i-j+1]) == primes[i]:
                if k > len(li):
                    li = primes[i-j-k:i-j+1]
                    print sum(li), len(li), li
            elif sum(primes[i-j-k:i-j+1]) > primes[i]:
                #print "skipping at", i,j,k
                break
print len(li)


