sent = input()

words = sent.split()
wc = len(words)

lets = 0
for word in words:
    for c in word:
        if (c.isalpha()): lets += 1

print(wc)
print(lets)

