"""
https://acmp.ru/index.asp?main=task&id_task=53
"""
n, m = map(int, input().split())
c = 0
r = 0
g = 0
b = 0
for i in range(n):
    for j in range(m):
        if (i + 1) * (j + 1) % 5 == 0:
            b += 1
        elif (i + 1) * (j + 1) % 3 == 0:
            g += 1
        elif (i + 1) * (j + 1) % 2 == 0:
            r += 1
        else:
            c += 1
print('RED :', r)
print('GREEN :', g)
print('BLUE :', b)
print('BLACK :', c)
