import datetime

dates = input().split()
#print(dates[2], dates[1], dates[0])
day = datetime.datetime(int(dates[2]),int(dates[0]),int(dates[1]))
#print(day)
print((day.strftime("%A")).upper())