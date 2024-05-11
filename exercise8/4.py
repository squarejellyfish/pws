import json

data = input()
data = json.loads(data)

curr, curdir = ["home"], data["home"]
while True:
    op = input()
    if (op == "quit"):
        break

    if (op == "pwd"):
        print("/".join(curr))
    elif (op == "ls"):
        output = sorted([d for d in curdir.keys()])
        for d in output:
            print(d)
    elif (op[:2] == "cd"):
        next = op[3:]
        if (next in curdir):
            curr.append(next)
            curdir = curdir[next]
        elif (next == ".."):
            curr.pop(-1)
            curdir = data["home"]
            for d in curr[1:]:
                curdir = curdir[d]
        else:
            print("error")
