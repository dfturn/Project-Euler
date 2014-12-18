print( sum([sum([y*y - (y-1) * x for x in range(3,-1,-1)]) for y in range(3,1003,2)]) + 1)
