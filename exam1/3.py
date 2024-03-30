x = input().split(", ")
ans = [0, 0] # [heads, legs]

for this in x:
    num, kind = int(this.split()[0]), this.split()[1]
    ans[0] += num # head
    if (kind[0] == 'c'):
        ans[1] += 4 * num
    else:
        ans[1] += 2 * num

print(f"{ans[0]} {'heads' if ans[0] > 1 else 'head'}, {ans[1]} legs.")
