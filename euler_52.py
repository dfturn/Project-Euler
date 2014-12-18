def containSameDigits( x,y ):
    if sorted(str(x)) == sorted(str(y)):
        return True
    return False

multiples = [2,3,4,5,6]
for i in xrange(1000000):
    for m in multiples:
        if not containSameDigits(i, i * m):
            break
    else:
        print i