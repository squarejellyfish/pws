nums = [int(x) for x in input().split()]

def play(numbers):
    nextnums = []

    n = len(numbers)
    i, played = 0, 0
    while (i < n - 1):
        if (numbers[i] == numbers[i + 1]):
            nextnums.append(numbers[i] * 2)
            played = 1
            i += 1
        else:
            nextnums.append(numbers[i])
        i += 1
    if (i < n): nextnums.append(numbers[n - 1])
#    print(f"next: {nextnums}")

    if not played: return nextnums
    else: return play(nextnums)

print(play(nums))

