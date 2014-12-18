from __future__ import division
from decimal import *

def checkEqual(iterator):
       return len(set(iterator)) <= 1

def mytest( test_str ):
    for i in range(len(test_str)):
        for length in range(len(test_str)//2,1,-1):
            str1 = test_str[i:i+length]
            str2 = test_str[i+length:i+2*length]
            if str1 == str2:
                return test_str[i:i+length]

all_longest = 0
max_idx = 0
for i in range(983,984):
    getcontext().prec = i * 2
    dec = str(Decimal(1) / Decimal(i))
    if i == 983:
        print dec
    dec = dec[dec.find('.') + 1:]

    longest = 0
    repeating = mytest(dec)
    tmp_repeating = repeating
    while( repeating is not None ):
        tmp_repeating = repeating
        repeating = mytest(repeating)
    repeating = tmp_repeating
    #print repeating, i
    if repeating is not None:
        if checkEqual(repeating):
            longest = 1
        else:
            longest = len(repeating)
    if longest > all_longest:
        all_longest = longest
        max_idx = i
print all_longest, max_idx

