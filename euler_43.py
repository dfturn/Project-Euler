import itertools
p = map(lambda x: ''.join(x), list(itertools.permutations([str(x) for x in range(10)], 10)))
p = itertools.ifilter(lambda x: str(int(x)) == x, p)
divisors = [2,3,5,7,11,13,17]
nums = []
for perm in p:
    for i in range(1,8):
        if int(perm[i:i+3]) % divisors[i-1]:
            break
    else:
        nums.append(perm)
print sum(map(int,nums))