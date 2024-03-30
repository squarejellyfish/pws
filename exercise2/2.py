nums = [int(x) for x in input().split()]
n = len(nums)

for i in range(1, n - 1):
    if (nums[i] <= nums[i - 1]):
        print(False)
        break
else:
    print(True)
