price = {}
consist = {}
def get_price(item):
    ret = price[item]
    for it in consist[item]:
        ret += get_price(it)
    return ret

n = int(input())
for i in range(n):
    ii = input().split()
    price[ii[0]] = int(ii[1])
    if (len(ii) > 2):
        consist[ii[0]] = ii[2:]
    else: consist[ii[0]] = []

m = int(input())

for i in range(m):
    item = input()
    print(get_price(item))

