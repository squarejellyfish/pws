def go_stairs(steps, broken):
    dp = [1, 1, 2]
    if (1 in broken):
        dp = [1, 0, 1]
    if (2 in broken): dp[2] = 0

    for i in range(3, steps + 1):
        if (i not in broken):
            dp.append(sum(dp[i - 3:i]))
        else: dp.append(0)

    return dp[steps]

a = [int(i) for i in input().split()]
n = a[0]
brokenstep = a[1:]
print(go_stairs(n, brokenstep))
