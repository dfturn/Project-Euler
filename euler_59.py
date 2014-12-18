import itertools
input = []
with open('euler_59_input.txt', 'r') as f:
    input = map(int, f.read().split(','))

dictionary = set()
with open('dictionary.txt', 'r') as f:
    for line in f.readlines():
        dictionary.add(line.rstrip())

min = 97
max = 27

def heuristic():
    valids = []
    for c1 in range(min,min+max):
        for c2 in range(min,min+max):
            for c3 in range(min,min+max):
                pw = itertools.cycle([c1,c2,c3])
                word = ''
                chars_to_examine = 20
                failures = 0
                found = 0
                for i in input:
                    word += chr( pw.next() ^ i )
                    exists = False
                    if word[-1] == ' ':
                        word = word[:-1]
                        exists = any(var == word for var in dictionary)
                        word = ''
                    if exists:
                        found += 1
                        word = ''
                    if len(word) == chars_to_examine:
                        word = ''
                        failures += 1
                    if found == 5 and failures == 0:
                        valids.append([c1,c2,c3])
                        #print c1, c2, c3, "is STRONG"
                        break
                    if failures > 5:
                        #print c1, c2, c3, "is weak"
                        break
    return valids
 
def get_answer( li ):
    pw = itertools.cycle(li)
    tot = 0
    for i in input:
        tot += pw.next() ^ i
    return tot

valids = heuristic()
if len(valids) == 1:
    print get_answer(valids[0])
else:
    print "There are multiple possibilities: ", valids
                
