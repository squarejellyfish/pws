blacktea = (50, 10)
milktea = (20, 30)
total = [0, 0]
yes = 1

for i in range(3):
    today = input()
    if (today[0] == 'B'):
        cup = int(today[1:])
        if (cup * blacktea[0] > 300 or cup * blacktea[1] > 60):
            yes = 0
        total[0] += cup * blacktea[0]
        total[1] += cup * blacktea[1]
    else:
        cup = int(today[1:])
        if (cup * milktea[0] > 300 or cup * milktea[1] > 60):
            yes = 0
        total[0] += cup * milktea[0]
        total[1] += cup * milktea[1]

if (total[0] > 700 or total[1] > 150):
    yes = 0

print("可" if yes else "不可")
