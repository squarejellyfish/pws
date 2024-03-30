food = input()
no = input()

ans = 0
for n in no:
    ans += food.count(n)

print(ans)

