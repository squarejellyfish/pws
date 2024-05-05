subjects = "ABCDEFG"
years_left = {c: 0 for c in subjects}
passed = {c: 0 for c in subjects}

year, ans = 1, 0
while True:
    try:
        sub = set(input().split())
        year_passed = input().split()
        if (year_passed[0] == '0'):
            year_passed = []
        year_passed = set(year_passed)
    except EOFError:
        break

    for s in subjects:
        years_left[s] -= 1
        if (years_left[s] <= 0):
            passed[s] = 0

    for yp in year_passed:
        years_left[yp] = 4
        passed[yp] = 1

    for s in sub.difference(year_passed):
        years_left[s] = 0
        passed[s] = 0

    # print(years_left)
    # print(passed)

    for s in subjects:
        if (not passed[s]):
            break
    else:
        if (ans == 0):
            # print(f"passed at {year}")
            ans = year 

    year += 1

if (ans):
    print(ans)
else:
    output = sorted([s for s in subjects if passed[s]])
    if (output):
        print(*output, sep=" ")
    else:
        print(None)
