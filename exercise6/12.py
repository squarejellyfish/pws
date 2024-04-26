from datetime import datetime, timezone, timedelta

time1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S.%f%z")
time2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S.%f%z")
t = datetime.fromtimestamp(float(input()), tz=time1.tzinfo)
diff = time2 - t

print(time1 + diff)
