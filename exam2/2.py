alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = [0 for i in range(26)]

ii = input().upper()
    
for c in ii:
    count[ord(c) - 65] += 1

ans = []
i = 0
while any(count):
    if (i == 26): i = 0
    if (count[i] != 0):
        ans.append(alph[i])
        count[i] -= 1
    i += 1

print(ans)

