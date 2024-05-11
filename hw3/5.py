words = input().split(",")

while True:
    try:
        ii = input().split()
        guess, res = ii[0], ii[1]

        for i, (c, r) in enumerate(zip(guess, res)):
            if (r == "*"):
                words = [w for w in words if c not in w]
            elif (r == "#"):
                words = [w for w in words if (c in w) and (w[i] != c)]
            elif (r == "@"):
                words = [w for w in words if w[i] == c]
    except EOFError:
        break

words.sort()
if (words):
    print(*words, sep=",")
else:
    print("Fail")
