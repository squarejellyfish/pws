ii = [int(x) for x in input().split()]
n, a, b = ii[0], ii[1], ii[2]

for i in reversed(range(n // a + 1)):
    print([i, (n - i * a) // b])

