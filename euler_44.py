import itertools
import math
def isPent(p):
    n = (math.sqrt(24*p + 1) + 1)/6
    if n.is_integer():
        return True
    return False

def work():
    maxim = 100000
    step_size = 5
    pents = [n*(3*n-1)/2 for n in xrange(1,maxim+1)]
    minimum = float('inf')
    for radius in xrange(1,maxim):
        #print radius
        for i in xrange(0,maxim-radius*step_size):
            for j in xrange(i+1+(radius-1)*step_size, min(maxim,i+1+radius*step_size)):
                try:
                    pent1 = pents[i]
                    pent2 = pents[j]
                    if isPent(pent1 + pent2) and isPent(pent2 - pent1):
                        print pent1, pent2
                        if pent2-pent1 < minimum:
                            minimum = pent2-pent1
                            print minimum
                except Exception:
                    print i,j
work()

