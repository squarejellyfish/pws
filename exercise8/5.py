from collections import OrderedDict
unique, count = 0, 0

archives = OrderedDict()
while True:
    book = input()
    if (book == "0"):
        break

    if (book not in archives):
        unique += 1
        archives[book] = {"count": 1, "archives": [], "uni": unique}
    else:
        archives[book]["count"] += 1

    count += 1
    code = f"{archives[book]['uni']:03d}" + f"{archives[book]['count']:03d}" + f"{count:04d}"
    archives[book]['archives'].append(code)

for book, prop in archives.items():
    arcs = prop["archives"]
    print(book, end=" ")
    print(*arcs, sep=" ")
