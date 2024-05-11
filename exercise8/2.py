names = input().split()
amount = input().split()

d = {name: am for name, am in zip(names, amount)}

while True:
    try:
        name = input()
        print(d[name])
    except EOFError:
        break
