"""
https://acmp.ru/index.asp?main=task&id_task=529
"""
import math


x1, y1, x2, y2 = map(int, input().split())
print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))