import datetime as dt


date = input().split('.')
n = int(input())
date = date[::-1]
day = dt.datetime(int(date[0]), int(date[1]), int(date[2]))
c = 0
d = []
while c != 2:
    day += dt.timedelta(days=1)
    if day.weekday() != 0 and (day.day + day.month) % n != 0:
        c += 1
        a = str(day.day)
        if len(a) == 1:
            a = '0' + a
        d.append(f'{a} {day.strftime("%B")} {str(day.year)[2:]}')
    else:
        c = 0
        d = []
for i in d:
    print(i)