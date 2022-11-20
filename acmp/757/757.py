"""
https://acmp.ru/index.asp?main=task&id_task=757
"""
c, h, o = map(int, input().split())
print(min(c // 2, h // 6, o // 1))