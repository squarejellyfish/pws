total = 0
while True:
    num = input().replace(",", "")
    if (num == "end"):
        break
    num = int(num)

    total += num

print(f"{total:,}")
