def calculator(num1, num2, op):
    ans = 0
    if (op == "+"):
        ans = num1 + num2
    elif (op == "-"):
        ans = num1 - num2
    elif (op == "*"):
        ans = num1 * num2
    elif (op == "/"):
        ans = num1 / num2

    return ans
