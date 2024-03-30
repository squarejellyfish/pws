letter = input()
sent = input().split()

for i, word in enumerate(sent):
    if (word[0] == letter):
        sent[i] = sent[i].capitalize()

print(" ".join(sent))

