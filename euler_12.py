import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

#print list(divisorGenerator(100))

val = 0
num_tri = 1
total = 0
while( val == 0 ):
    total += num_tri
    
    if( len(list(divisorGenerator(total))) >= 500 ):
        val = num_tri
    
    num_tri += 1
    if( num_tri % 1000 == 0):
        print "Working: " + str(num_tri)

print total