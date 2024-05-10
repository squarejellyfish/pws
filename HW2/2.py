import re

def get_exchange(money):
    ret = []
    ret.extend([50] * (money // 50))
    money %= 50
    ret.extend([10] * (money // 10))
    money %= 10
    ret.extend([5] * (money // 5))
    money %= 5
    ret.extend([1] * (money // 1))

    return ret

def main():
    puts = [int(x) for x in input().split(",")]
    puts = sorted(puts, reverse=True)
    action = input()

    if (action == "退幣"):
        print(puts)
        return 

    price = int(re.findall("\d+", action)[0])

    total = 0
    output = []
    for i, put in enumerate(puts):
        total += put
        if (total == price):
            output.extend(puts[i+1:])
            break
        
        if (total > price):
            output.extend(puts[i+1:])
            output.extend(get_exchange(total - price))
            break

    output = sorted(output, reverse=True)
    print(output if output else [0])

main()
