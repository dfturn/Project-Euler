passwords = []
with open('inp_79.txt', 'r') as f:
    for line in f:
        passwords.append([int(c) for c in line])

# Ended up just doing this one by hand....
strict_order = []
for p in passwords:
    for i in range(len(p)):
        pass
            