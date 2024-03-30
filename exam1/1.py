alph = "abcdefghijklmnopqrstuvwxyz"

sentence = input()
ans = ""

for char in sentence:
    if (char.lower() in alph):
        pos = alph.index(char.lower())
        if (char == char.lower()):
            ans += alph[pos - 13]
        else:
            ans += alph[pos - 13].upper()
    else:
        ans += char

print(ans)

