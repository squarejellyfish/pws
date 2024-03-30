ranks = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']
def rank(score):
    if (score >= 90):
        return 0
    elif (score >= 85):
        return 1
    elif (score >= 80):
        return 2
    elif (score >= 77):
        return 3
    elif (score >= 73):
        return 4
    elif (score >= 70):
        return 5
    elif (score >= 67):
        return 6
    elif (score >= 63):
        return 7
    elif (score >= 60):
        return 8
    else:
        return 9

homeworks = [int(x) for x in input().split()]
mids = [int(x) for x in input().split()] 
final = int(input())

homeworks.sort(reverse=True)
mids.sort(reverse=True)

cheat = 1 if -1 in homeworks else 0
homeworks.pop(-1)

mids = [100 if m > 100 else m for m in mids]

avg_homeworks = sum(homeworks) / 5
if (avg_homeworks > 100):
    avg_homeworks = 100

total = round((avg_homeworks * 50 + mids[0] * 15 + mids[1] * 10 + final * 25) / 100)
r = rank(total)
if (cheat):
    r = min(r + 2, 9)
print(f"{total} {ranks[r]}")
