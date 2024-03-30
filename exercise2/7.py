sent = input().split()

exclude = ["to", "a", "an", "the", "from", "for", "of", "and", "in"]

n = len(sent)
new = ""
for i, word in enumerate(sent):
    if (i == 0):
        new += word.capitalize()
        continue

    if (word not in exclude):
        new += " " + word.capitalize()
    else:
        if (i == n - 1):
            new += " " + word.capitalize()
        else:
            new += " " + word

print(new)
