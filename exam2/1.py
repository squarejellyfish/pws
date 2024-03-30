def is_armstrong(num):
    ans = False
    ord_num = num
    s = 0
    dig = 0
    nums = []
    while (num != 0):
        nums.append(num % 10)
        dig += 1
        num //= 10

    for n in nums:
        s += n**dig

    if (s == ord_num): ans = True
     
    return ans

s = int(input())
print(is_armstrong(s))
