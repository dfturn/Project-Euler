dec = ""
for i in range(1,1000000):
    dec += str(i)
print( int(dec[0]) * int(dec[9]) * int(dec[99]) * \
int(dec[999]) * int(dec[9999]) * int(dec[99999]) * int(dec[999999]) )