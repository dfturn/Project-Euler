size = 21

grid = [[0 for y in range(size)] for x in range(size)]

def pprint( grid ):
    for row in grid:
        for val in row:
            print val,
        print
pprint( grid )
print
grid[0][0] = 1

for r in range(size):
    for c in range(size):
        if grid[r][c] == 0:
            up_paths = 0
            left_paths = 0
            if r > 0:
                up_paths = grid[r-1][c]
            if c > 0:
                left_paths = grid[r][c-1]
            grid[r][c] = up_paths + left_paths
pprint( grid )

