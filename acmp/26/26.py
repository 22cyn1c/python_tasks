"""
https://acmp.ru/index.asp?main=task&id_task=26
"""
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
i = ((a - d) ** 2 + (b - e) ** 2) ** 0.5
if i <= c + f and f <= i + c and c <= i + f:
    print('YES')
else:
    print('NO')