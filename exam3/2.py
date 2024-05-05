s1, s2 = input(), input()

if (len(s1) == len(s2)):
    d, d2 = {}, {}
    for i, c in enumerate(s1):
        if (c not in d):
            d[c] = s2[i]
            if (s2[i] not in d2):
                d2[s2[i]] = c
            else:
                if (d2[s2[i]] != c):
                    print(False)
                    break

        if (d[c] != s2[i]):
            print(False)
            break
    else:
        output = [(key, val) for key, val in d.items()]
        output.sort()
        print(output)
else:
    print(False)
