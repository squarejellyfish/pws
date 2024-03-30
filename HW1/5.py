n = int(input())
colors = input()
last_time = dict()
ans = 0
t = 0

for color in colors:
    if (color in last_time):
        last_time[color] = t
    else: # color is not used before
        if (len(last_time) == n): # plate is full
            last_time.pop(min(last_time, key=last_time.get))
            ans += 1

        last_time[color] = t
    t += 1

print(ans)
