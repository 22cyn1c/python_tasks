"""
https://acmp.ru/index.asp?main=task&id_task=850
"""
a, b = map(int, input().split())
if max(a, b) % 2 == 0:
    print(max(a, b) // 2, min(a, b))
else:
    print(max(a, b) // 2 + 1, min(a, b))