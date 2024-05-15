import json

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# data = open("test.json", "r")
# data = json.load(data)
data = input()
data = json.loads(data)

for book, codes in data.items():
    new = []
    for code in codes:
        new_code = ""
        num = [table[n] for n in numberToBase(int(code[:3]), 26)]
        num = ["A", "A", "A"] + num
        new_code += "".join(num[-3:])
        num = [table[n] for n in numberToBase(int(code[3:6]), 26)]
        num = ["A", "A", "A"] + num
        new_code += "".join(num[-3:])
        num = [table[n] for n in numberToBase(int(code[6:10]), 26)]
        num = ["A", "A", "A", "A"] + num
        new_code += "".join(num[-4:])
        new.append(new_code)
    data[book] = new

output = sorted([b for b in data.keys()])
for book in output:
    print(book, data[book])
