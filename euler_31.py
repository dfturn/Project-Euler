coins = [200, 100, 50, 20, 10, 5, 2, 1]

def recurse( idx, currentTotal ):
    combos = 0
    if currentTotal % coins[idx] == 0:
        combos += 1
    
    for reduc in range(coins[idx], currentTotal, coins[idx]):
        for i in range(idx+1, len(coins)):
            rec = recurse(i, currentTotal - reduc)
            combos += rec
    return combos

combos = 0 
for i in range(len(coins)):
    combos += recurse(i, 200)
print combos
         
    
