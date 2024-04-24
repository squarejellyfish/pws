ss = input().split(",")

ss.sort(key=lambda x: len(x))
for s in ss:
    print(s)
