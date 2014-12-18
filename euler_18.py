f = open('inp_18.txt', 'r')

matrix = []
for line in f:
    matrix.append( map(int, line.rstrip().split(' ') ) )

print matrix

indices = [0 for x in range(15)]


        
def getProduct( matrix, r, c, currentProd ):
    # Assume r and c are valid currently
    # Ensure we only get other valid ones
    if r == len(matrix) - 1:
        return currentProd + matrix[r][c]
    return max( getProduct( matrix, r + 1, c, currentProd + matrix[r][c] ), \
                getProduct( matrix, r + 1, c + 1, currentProd + matrix[r][c] ) )

print getProduct(matrix, 0, 0, 0)