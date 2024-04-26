n = int(input())
sentences = []
for i in range(n):
    sentences.append(input().split())

d = {}

for i in sentences:
    for word in i:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

print(d)

