num1 = input()
num2 = input()
try:
	num1 = int(num1)
	num2 = int(num2)
	print(num1 + num2)
except ValueError:
	print("請輸入阿拉伯數字")

