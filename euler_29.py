from itertools import *
#print [[one,two,five,ten,twenty,fifty,hundred,twoh] for one,two,five,ten,twenty,fifty,hundred,twoh in range(1,201)]

li = [1,2,5,10,20,50,100,200]

#li = [1,2,3]
#indices = [0,0,0]

def powerset(iterable, n):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations_with_replacement(s, r) for r in range(n+1))

num = 0
for i in powerset(li, 50):
    if sum(i) == 200:
        num +=1
print num

#print filter( lambda x: sum(x) == 200, list(combinations_with_replacement([1,2,5,10,20,50,100,200], 100)))
print "finished"