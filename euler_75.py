import math
import time
import profile
import pstats
import itertools
import fractions

import multiprocessing
from threading import Thread

max = 1225
tot_max = 1500000
def pyth(n):
    def p(a, b, c):
        if n < a + b + c: return []
        return ([[a, b, c]] if a < b else [[b, a, c]]) \
             + p(a-b-b+c+c, a+a-b+c+c, a+a-b-b+c+c+c) \
             + p(a+b+b+c+c, a+a+b+c+c, a+a+b+b+c+c+c) \
             + p(c+c+b+b-a, c+c+b-a-a, c+c+c+b+b-a-a)
    return p(3, 4, 5)
    
if __name__ ==  '__main__':
    prims = pyth(1500001)
    reals = []
    for trip in prims:
        reals.append(trip)
        for i in range(1500001/sum(trip),1,-1):
            reals.append(map(lambda x: i * x, trip))
    dict = {}
    for r in reals:
        s = sum(r)
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    print len([1 for x in dict.keys() if dict[x] == 1])

    
# Ignore these, old attempts...
def test(q, k_start, k_end):
    vals = {}
    for n in range(1,max):
        for m in range(n+1,max):
            for k in range(k_start,tot_max/(min(n*n,m*m)),k_end):
                if (m-n) % 2 == 0 and fractions.gcd(m,n) == 1:
                    val = sum([k*(m*m-n*n), k*(2*m*n),k*(m*m+n*n)])
                    if val < 1500000:
                        if val in vals:
                            vals[val] += 1
                        else:
                            vals[val] = 0
    q.put(sum([1 for v in iter(vals) if vals[v] == 1]))

def docrap():
    cpus = multiprocessing.cpu_count()
    queues = [multiprocessing.Queue() for i in range(cpus)]
    threads = [multiprocessing.Process(target=test, args=(queues[i],i+1,cpus)) for i in range(cpus)]
    map(multiprocessing.Process.start, threads)
    map(multiprocessing.Process.join, threads)
    print sum([x.get() for x in queues])
   