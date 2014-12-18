import time
start = time.time()

print( sum([sum([ord(c) - 64 for c in name]) * (i+1) for i, name in enumerate( sorted( map( lambda str: str[1:-1], open('names.txt', 'r').read().split(",") ) ) )]) )
print time.time() - start