f = open('inp_67.txt', 'r')

matrix = []
visited = []
distances = []
for line in f:
    matrix.append( map(int, line.rstrip().split(' ') ) )
    visited.append([0 for i in matrix[-1]])
    distances.append([float("inf") for i in matrix[-1]])

for r in matrix:
    print r
print
for r in range(len(matrix)-1, 0, -1):
    for c in range(0,len(matrix[r])-1):
        matrix[r-1][c] += max(matrix[r][c], matrix[r][c+1])
    
for r in matrix:
    print r


