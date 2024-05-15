import json

data = input()
data = json.loads(data)

curr, curdir = ["home"], data["home"]
while True:
    op = input()
    if (op == "exit"):
        break

    if (op == "pwd"):
        print("/".join(curr))
    elif (op == "ls"):
        output = sorted([d for d in curdir])
        print(",".join(output))
    elif (op.split()[0] == "cd"):
        next = op[3:]
        if (next in curdir):
            curr.append(next)
            curdir = data[next]
        elif (next == ".."):
            if (len(curr) > 1):
                curr.pop(-1)
                curdir = data[curr[-1]]
        else:
            print(f"{op} error")
    elif (op.split()[0] == "mkdir"):
        new = op.split()[1]
        curdir.append(new)
        data[new] = []
    elif (op.split()[0] == "rmdir"):
        name = op.split()[1]
        if (name in curdir):
            curdir.remove(name)
            data.pop(name)
        else:
            print(f"{op} error")

