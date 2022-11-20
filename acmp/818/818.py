"""
https://acmp.ru/index.asp?main=task&id_task=818
"""
n = int(input())
a = list(map(int, input().split()))
s = 0
for elem in a:
    s += elem
n -= 1
print(s - n)