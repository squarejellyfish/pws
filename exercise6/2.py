datas = input().split()

d = dict()
for data in datas:
    name, info = data.split(",")[0], data.split(",")[1:]

    d[name] = info

s = input()
print(d[s])
