"""
https://acmp.ru/index.asp?main=task&id_task=794
"""
a, b, c = map(int, input().split())
r = b // c
w = min(c - 1, b)
print((r + w) * a)