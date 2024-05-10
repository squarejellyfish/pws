from functools import cmp_to_key

# def cmp(p1, p2):
#     if (p1[1] != p2[1]):
#         return -1 if p1[1] < p2[1] else 1
#     elif (int(p1[2]) // 5 != int(p2[2]) // 5) and not (int(p1[2]) // 5 > 10 and int(p2[2]) // 5 > 10):
#
#     elif (int(p1[2]) >= 10 and int(p2[2]) < 10): return -1
#     elif (int(p1[2]) >= 5 and int(p2[2]) < 5): return -1
#     elif (int(p1[3]) % 2 != int(p2[3]) % 2):
#         return -1 if int(p1[3]) % 2 else 1
#     else: return 0

n = int(input())

l = [input().split() for _ in range(n)]

l = sorted(l, key=lambda x: (x[1], -(int(x[2]) >= 10), -(int(x[2]) >= 5), -(int(x[3]) % 2 == 1)))
# l = sorted(l, key=cmp_to_key(cmp))

print(l)
# for ls in l:
#     print(ls[0])
