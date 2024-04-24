from math import floor

def square_check(x):
    if (x == 1): return 0

    ret = floor(x**0.5) 
    return ret**2 if ret**2 < x else (ret - 1)**2

n = int(input())
print(square_check(n))

