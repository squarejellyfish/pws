from collections import OrderedDict

d = OrderedDict()
while True:
    line = input()
    if (line == "0"): break

    for c in line:
        if (c in d):
            d[c] += 1
        else:
            d[c] = 1

for c, times in d.items():
    print(f"{''.join([c for _ in range(times)])}") 
