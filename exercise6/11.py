from datetime import datetime, timedelta

d1 = [int(x) for x in input().split()]
d2 = [int(x) for x in input().split()]
date1 = datetime(*d1)
date2 = datetime(*d2)
diff = date1 - date2

print(abs(diff.days))
