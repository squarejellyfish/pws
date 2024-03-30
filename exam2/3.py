def main():
    ii, iii = input().replace("(", "").replace(")", "").split()

    pos1, pos2 = list(map(float, ii.split(","))), list(map(float, iii.split(",")))

    if (pos1[0] - pos2[0] == 0):
        print(None)
        return 
    a = round((pos1[1] - pos2[1]) / (pos1[0] - pos2[0]), 2)
    b = round(pos1[1] - a*pos1[0], 2)

    if (a == 0):
        print("y=0.0x+{:}".format(b))
    elif (b == 0):
        print("y={:}x+0.0".format(a))
    else:
        print("y={:}x{:+}".format(a, b))

main()
