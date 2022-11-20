"""
https://acmp.ru/index.asp?main=task&id_task=791
"""
n = int(input())
if 1 < n < 8:
    print(n - 1, n + 1, n + 8)
elif 57 < n < 64:
    print(n - 8, n - 1, n + 1)
elif n == 9 or n == 17 or n == 25 or n == 33 or n == 41 or n == 49:
    print(n - 8, n + 1, n + 8)
elif n == 16 or n == 24 or n == 32 or n == 40 or n == 48 or n == 56:
    print(n - 8, n - 1, n + 8)
elif n == 1:
    print(2, 9)
elif n == 8:
    print(7, 16)
elif n == 57:
    print(49, 58)
elif n == 64:
    print(56, 63)
else:
    print(n - 8, n - 1, n + 1, n + 8)