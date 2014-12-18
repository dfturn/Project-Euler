from fractions import Fraction

# x and y are 2 digit ints
def stripCommons(x,y):
    strX = list(str(x))
    strY = list(str(y))
    mySet = set(strX) & set(strY)
    for i in mySet:
        strX.remove(i)
        strY.remove(i)

    strX = ''.join(strX)
    strY = ''.join(strY)
    if strX == '': strX = '0'
    if strY == '': strY = '0'
    return (int(strX), int(strY))


accum = Fraction(1,1)
for i in range(10,100):
    for j in range(i+1, 100):
        stripped = stripCommons(i,j)
        try:
            if (i%10 != 0 and j%10!=0) and (i,j) != stripped and Fraction(i,j) == Fraction(stripped[0],stripped[1]):
                accum *= Fraction(i,j)
        except ZeroDivisionError:
            pass

print accum