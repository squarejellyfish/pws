def social_distance(x, y):
    if (x == "室內" and y <= 150): return "請維持社交距離"
    elif (x == "室外" and y <= 100): return "請維持社交距離"
    else: return ""

#We will judge your code through following scripts.
x = input()
y = input()
print(social_distance(x, int(y)))

