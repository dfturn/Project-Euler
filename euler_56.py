import math

def sumDigits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

def sumStrDigits(s):
    return sum(map(int, s))

#print sumDigits(x)
    
def work():
    maxim = 0
    for a in range(100):
        for b in range(100):
            power = a ** b
            maxim = max(maxim, sumStrDigits("%d" % power))
    print maxim
work()
