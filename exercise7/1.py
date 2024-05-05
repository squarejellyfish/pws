nums = [int(x) for x in input().split()]

lst, each = [], [nums[0]]
last = nums[0]
for num in nums[1:]:
    if (num > last and num - last == 1): each.append(num)
    else:
        lst.append(each)
        each = [num]
    last = num
lst.append(each)

for l in lst:
    print(*l, sep=" ")
