def isSubStr(s, t):
    p = 0
    for c in s:
        for i, cc in enumerate(t[p:]):
            if (c == cc):
                p += i + 1
                break
        else: return False

    return True

print(isSubStr("aba", "aabaa"))

