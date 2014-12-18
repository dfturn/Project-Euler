def isPandigital(x,y,z):
    tot = str(x)+str(y)+str(z)
    if sorted(tot) == [str(x) for x in range(1,10)]:
        return True
    return False
    
#print isPandigital(39,186,7254)

products = set()
for i in range(1,100):
    for j in range(100,10000):
        z = i * j
        if z not in products and isPandigital(i,j,z):
            products.add(z)
print sum(products)