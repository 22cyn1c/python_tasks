n = int(input())
c = 0
for i in range(n):
    a = int(input())
    if a == 0:
        c += 1
if c > n // 2:
    print(n - c)
else:
    print(c)
"""
https://acmp.ru/index.asp?main=task&id_task=106
"""