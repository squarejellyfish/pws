from datetime import datetime, timedelta

y, m, d = map(int, input().split())
delt = int(input())

date = datetime(y, m, d)
date = date + timedelta(days=delt)

print(date.date())
