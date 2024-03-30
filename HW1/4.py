alph = "_abcdefghijklmnopqrstuvwxyz"
alph_out = "zabcdefghijklmnopqrstuvwxy"
enc = input()
dec = input()

for i, c in enumerate(reversed(enc)):
    val1 = alph.find(c.lower())
    val2 = alph.find(dec[i].lower())
    if (val1 + val2) % 2 == 0:
        out = (val1 * val2) % 26
        print(alph_out[out].upper(), end='')
    else:
        out = val1 % val2
        print(alph_out[out].lower(), end='')
print()

