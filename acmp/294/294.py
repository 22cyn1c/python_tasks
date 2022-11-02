k, l, m = map(int, input().split())
n, o, p = map(int, input().split())
summa = k * (l / 100) * m
summa += n * (o / 100) * p
s = k - k * (l / 100)
ss = n - n * (o / 100)
if s > ss:
    summa += (s - ss) * m
elif ss > s:
    summa += (ss - s) * p
print(int(summa))
"""
https://acmp.ru/index.asp?main=task&id_task=294
"""