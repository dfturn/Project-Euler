triangle_nums = [n * (n+1) / 2 for n in range(1,27)]
#print len(triangle_nums)
#print sum([ord(c) - 64 for c in 'SKY'])


tot = 0
with open('inp_42.txt', 'r') as f:
    words = map( lambda str: str[1:-1], f.read().split(",") )
    for w in words:
        #print w
        val = sum([ord(c) - 64 for c in w])
        if val in triangle_nums:
            tot += 1
print tot
            