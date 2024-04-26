pairs = input().split()

d = dict()
for pair in pairs:
    key, val = pair.split(",")[0], pair.split(",")[1]
    d[key] = val

test = input()
print(d[test] if test in d else "單字不存在")
