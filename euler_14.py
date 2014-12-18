longest_seq = 1
seq_idx = 1
for i in range(1, 1000000):
    iters = 0
    var = i
    while( var != 1 ):
        iters += 1
        if( var % 2 == 0 ):
            var = var / 2
        else:
            var = 3 * var + 1
    if iters > longest_seq:
        longest_seq = iters
        seq_idx = i
print seq_idx