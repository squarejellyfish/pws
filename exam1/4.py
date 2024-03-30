ii = [int(x) for x in input().split()]
n, a, b = ii[0], ii[1], ii[2]
ans = [0 for _ in range(a + 1)]

def solve(N, A, B):
    if (ans[A]):
        return 
#    print(f"now: {[N, A, B]}")
    if (N == 0 or N < b):
        if (not ans[A]):
            print([A, B])
            ans[A] = 1
        return

    if (N - a >= 0):
        solve(N - a, A + 1, B)
    if (N - b >= 0):
        solve(N - b, A, B + 1)

solve(n, 0, 0)

