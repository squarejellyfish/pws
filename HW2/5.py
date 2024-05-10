s = input().upper()

count = []
inq, ina = 0, 0
for c in s:
    if (c == 'Q'):
        if (ina):
            count.append(ina)
            ina = 0
        inq += 1
    elif (c == 'A'):
        if (ina):
            ina += 1
        elif (inq):
            count.append(inq)
            ina = 1

if (inq): count.append(inq)

total = 0
n = len(count)
for i in range(1, n - 1, 2):
    total += count[i] * ((count[n - 1] - count[i - 1]) * count[i - 1])

# print(count)
print(total)
