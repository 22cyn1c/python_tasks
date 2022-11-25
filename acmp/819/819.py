"""
https://acmp.ru/index.asp?main=task&id_task=819
"""
a, b, c = map(int, input().split())
print(2 * (a * b + a * c + b * c), a * b * c)