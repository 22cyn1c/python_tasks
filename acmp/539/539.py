"""
https://acmp.ru/index.asp?main=task&id_task=539
"""
n = int(input())
if n == 1:
    print(0)
else:
    if n % 2 == 0:
        n //= 2
    print(n)
