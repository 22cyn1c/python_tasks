"""
https://acmp.ru/index.asp?main=task&id_task=766
"""
a, b, c = map(int, input().split())
if a * b >= c:
    print('YES')
else:
    print('NO')