import itertools
import re
digits = [str(x) for x in range(10)]

squares = ["%02d" % (x*x) for x in range(1,10)]

def creates(s1, s2, square):
    def sixty_niner(x):
        return '[69]' if ( x == '9' or x == '6' ) else x
    search_string = sixty_niner( s1 )
    search_string += sixty_niner( s2 )
    search_string += '|' + sixty_niner( s2 ) + sixty_niner( s1 )
    return re.match(search_string, square)

def matches( c1, c2 ):
    for s in squares:
        #print s
        if not [1 for t1 in c1 for t2 in c2 if creates(t1, t2, s) != None]:
            return False
    return True

inp1 = ('0', '5', '6', '7', '8', '9')
inp2 = ('1', '2', '3', '4', '8', '9')
#print matches(inp1, inp2)
def work():
    total = 0
    for cube1 in itertools.combinations(digits,6):
        for cube2 in itertools.combinations(digits,6):
            if matches(cube1, cube2):
                #print cube1, cube2
                total += 1
            else:
                pass
                #print cube1, cube2
    print total / 2
work()