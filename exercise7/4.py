book = dict()
while True:
    ip = input()
    if (ip == "end"):
        break

    op = ip[0]
    if (op == "a"):
        name, num = ip.split()[1], ip.split()[2]
        book[name] = num
        book[num] = name
    elif (op == "s"):
        desire = ip.split()[1]
        if (desire in book):
            print(book[desire])
        else: print(f"Cannot find {desire}")

