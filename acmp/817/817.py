"""
https://acmp.ru/index.asp?main=task&id_task=817
"""
a, b, c, d = map(int, input().split())
print(a * c * d + b * c * d - a * b * c ** 2)