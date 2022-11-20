"""
https://acmp.ru/index.asp?main=task&id_task=777
"""
a, b = map(int, input().split())
if b - a >= 0:
    print(b - a)
else:
    print(12- a + b)