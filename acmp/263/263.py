n, a, b = map(int, input().split())
if n - max(a, b) + min(a, b) < max(a, b) - min(a, b):
    print(n - max(a, b) + min(a, b) - 1)
else:
    print(max(a, b) - min(a, b) - 1)
"""
https://acmp.ru/index.asp?main=task&id_task=263
"""