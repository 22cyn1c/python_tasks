"""
https://acmp.ru/index.asp?main=task&id_task=844
"""
import math
n, m = map(int, input().split())
if math.sqrt(n * m) // 1 == math.sqrt(n * m):
    print(int(math.sqrt(n * m)))
else:
    print(0)