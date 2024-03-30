remains = int(input())
need = int(input())

can = 0
while not remains < need:
    can += remains - remains % need
    new = remains % need + remains // need
    remains = new
can += remains

print(can)
