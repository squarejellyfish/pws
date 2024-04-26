import random

seed, n = map(int, input().split())
random.seed(seed)
a, b = random.randint(1, 1000000000), random.randint(1, 1000000000)
c = random.randint(1, 10000)

for i in range(n):
    r = (a * seed + b) % c
    print(r)
    seed = r
