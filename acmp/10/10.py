"""
https://acmp.ru/index.asp?main=task&id_task=10
"""
a, b, c, d = map(int, input().split())
e = []
for i in range(-100, 101):
    if (a * (i ** 3)) + (b * (i ** 2)) + (c * i) + d == 0:
        e.append(i)
print(*e)