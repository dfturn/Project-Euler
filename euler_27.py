import math
import profile
import pstats

primes = {}

def is_prime(n):
    if n <= 1 or n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def worker():
    max_n = 0
    a_coeff = -1000
    b_coeff = -1000
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            i = 0
            while True:
                num = i * i + a * i + b
                if num in primes:
                    tmp = primes[num]
                else:
                    tmp = is_prime(num)
                    primes[num] = tmp
                if not tmp:
                    i -= 1
                    break
                else:
                    i += 1
            if i > max_n:
                max_n = i
                a_coeff = a
                b_coeff = b
        if abs(a) % 100 == 0: print a
    print max_n, a_coeff, b_coeff

profile.run("worker()","profiling_out.txt")

p = pstats.Stats('profiling_out.txt')
p.sort_stats('cumulative').print_stats(10)