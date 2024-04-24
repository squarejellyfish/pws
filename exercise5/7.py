nums = input().split()

new = []
for num in nums:
    s = 0
    for n in num:
        s += int(n)
    new.append([int(num), s])

new.sort(key=lambda x: x[1])
print([row[0] for row in new])
