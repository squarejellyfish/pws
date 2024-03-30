def main():
    scores = list(map(int, input().split(",")))
    desire = input()
    score = sum(scores)

    if (desire == "會計系"):
        if (score - scores[-1] < 57):
            print(0)
            return 

        if (scores[0] < 15):
            print(0)
            return 

        print(1)
    elif (desire == "公衛系"):
        if (scores[1] + scores[2] + scores[4] < 38):
            print(0)
            return 
        print(1)
    elif (desire == "經濟系"):
        if (scores[-2] + scores[-1] < 26):
            print(0)
            return 
        if (scores[2] < 15):
            print(0)
            return 

        print(1)
    elif (desire == "資工系"):
        if (scores[1] + scores[-1] < 27):
            print(0)
            return 
        if (scores[2] < 15):
            print(0)
            return 
        print(1)

main()


