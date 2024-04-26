nums = input().split()

if (len(nums) < 3):
    print("串列長度不足")
else:
    s = 0
    for num in nums[-3:]:
        try:
            s += int(num)
        except ValueError:
            print("資料型態不為整數")
            break
    else:
        print(s)

