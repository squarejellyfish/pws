from sys import stdin

output = "-".join([line[:-1] for line in stdin])

print(output)
