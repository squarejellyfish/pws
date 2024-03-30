def main():
    x = int(input())

    for i in range(2, x):
        if (x % i == 0):
            print(False)
            return

    print(True)

main()

