def f(n):
    if (not n): return 0
    if (n == 1): return 1

    return n * f(n - 2) - f(n - 1)

print(f(int(input())))
