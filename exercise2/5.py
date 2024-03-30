pw = input()

print(pw.isalnum() and not pw.isnumeric() and not pw.isalpha())
