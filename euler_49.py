import math
import time
import itertools
start = 1000
end = 10000

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

s1 = time.time()
for c in itertools.combinations_with_replacement([x for x in range(0,10)],4):
    perms = list(sorted(map(lambda x: reduce(lambda z, y: int('%d%d' % (z, y)), x), itertools.ifilter( lambda p: p[0] != 0, itertools.permutations(c,4)))))
    for i in range(0,len(perms)):
        for j in range(i+1, len(perms)):
            diff = perms[j] - perms[i]
            if diff != 0:
                try:
                    n = next(x for x in perms[j+1:] if x == (perms[j] + diff))
                    
                    # No exception, assume we found it
                    if all([is_prime(x) for x in [perms[i],perms[j],n]]):
                        print '%d%d%d' % ( n - diff * 2, n - diff, n)
                except StopIteration:
                    pass
print time.time() - s1
            