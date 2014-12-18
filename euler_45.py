import itertools
min = 143
max = 100000
triangles = (n*(n+1)/2 for n in xrange(min,max))
pents = (n*(3*n-1)/2 for n in xrange(min, max))
hexes = (n*(2*n-1) for n in xrange(min, max))

tris = list(itertools.takewhile( lambda x: x, triangles ))
#print 40755 in tris
#print list(tris)
ps = list(itertools.takewhile( lambda x: x, pents ))
#print 40755 in ps
#print list(ps)
hs = list(itertools.takewhile( lambda x: x, hexes ))
#print 40755 in hs
#print list(hs)

intersection = set(tris) & set(ps) & set(hs)
print intersection


