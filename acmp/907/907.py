"""
https://acmp.ru/index.asp?main=task&id_task=907
"""
a, b, c = map(int, input().split())
if c * 2 <= min(a, b):
    print('YES')
else:
    print('NO')