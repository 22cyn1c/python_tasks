n = int(input())
a = 0
b = 1
t = b
c = 1
if n == 0:
    print(0)
else:
    while n > c:
        b += a
        a = t
        t = b
        c += 1
    print(b)
"""
https://acmp.ru/index.asp?main=task&id_task=147
"""
