n = int(input())
t = 0
b = -1
for i in range(n):
    v, s = map(int, input().split())
    if s == 1 and v > t:
        t = v
        b = i + 1
print(b)
"""
https://acmp.ru/index.asp?main=task&id_task=131
"""