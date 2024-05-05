N, k, step = int(input()), int(input()), int(input())

up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = up.lower()
digit = "1234567890"
us, ls, ds = 0, 0, 0

for n in range(N):
    for c in range(k + n):
        if ((n + 1) % 3 == 1):
            print(up[us], end="")
            us = (us + (step)) % 26
        elif ((n + 1) % 3 == 2):
            print(low[ls], end="")
            ls = (ls + (step)) % 26
        elif ((n + 1) % 3 == 0):
            print(digit[ds], end="")
            ds = (ds + (step)) % 10
    print()
