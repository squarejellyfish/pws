import random

random.seed(942)
n = int(input())
if (not n):
    print("吃空氣")
else:
    sam = []
    for i in range(n):
        sam.append(input().split())

    serie = random.choice(sam)
    name, sam = serie[0], serie[1:]
    print(name, random.choice(sam))
