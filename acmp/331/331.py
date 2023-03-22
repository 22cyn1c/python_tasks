"""
https://acmp.ru/index.asp?main=task&id_task=331
"""
a, b = map(int, input().split(':'))
h, m = map(int, input().split())
a += h
b += m
while b >= 60:
    b -= 60
    a += 1
while a >= 24:
    a -= 24
a = str(a)
b = str(b)
if len(a) == 1:
    a = '0' + a
if len(b) == 1:
    b = '0' + b
print(f"{a}:{b}")
