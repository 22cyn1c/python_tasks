"""
https://acmp.ru/index.asp?main=task&id_task=9
"""
n = int(input())
a = list(map(int, input().split()))
b = []
d = []
c = 1
t = True
e = False
for i in a:
    if i > 0:
        b.append(i)
for i in a:
    if t:
        if i == max(a) or i == min(a):
            t = False
            e = True
            continue
    if e:
        if i == max(a) or i == min(a):
            t = True
            e = False
        else:
            d.append(i)
for i in d:
    c *= i
print(sum(b), c)