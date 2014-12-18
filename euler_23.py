import math
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i and i is not 1:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

abundants = []
for i in range(28123):
    if sum(list(divisorGenerator(i))) > i:
        abundants.append(i)

can_be_sum = [False for i in range(28123)]
for i in abundants:
    if i % 100 == 0: print i
    for j in abundants:
        if i + j < 28123:
            can_be_sum[i + j] = True
print sum([i if not x else 0 for i,x in enumerate(can_be_sum)])

                
        
    