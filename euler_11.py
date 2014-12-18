f = open('inp_11.txt', 'r')

def getNumbersDown( matrix, x, y ):
    if y < 17:
        return matrix[x][y] * matrix[x][y+1] * matrix[x][y+2] * matrix[x][y+3]
    else:
        return 0

def getNumbersRight( matrix, x, y ):
    if x < 17:
        return matrix[x][y] * matrix[x+1][y] * matrix[x+2][y] * matrix[x+3][y]
    else:
        return 0

def getNumbersDiag( matrix, x, y ):
    if x < 17 and y < 17:
        return matrix[x][y] * matrix[x+1][y+1] * matrix[x+2][y+2] * matrix[x+3][y+3]
    else:
        return 0
        
def getNumbersOtherDiag( matrix, x, y ):
    if x < 17 and y > 2:
        return matrix[x][y] * matrix[x+1][y-1] * matrix[x+2][y-2] * matrix[x+3][y-3]
    else:
        return 0

matrix = []
for line in f:
    matrix.append( map(int, line.rstrip().split(' ') ) )

maxim = 0
for x in range( 20 ):
    for y in range( 20 ):
        maxim = max( maxim, getNumbersDown( matrix, x, y ), getNumbersRight( matrix, x, y ), getNumbersDiag( matrix, x, y ), getNumbersOtherDiag( matrix, x, y ) )
print maxim