n = int(input())
t = 0
arr = list(map(int, input().split()))
c = 0
for i in range(n):
    if arr[i] > 0:
        c += 1
        if c > t:
            t = c
        continue
    c = 0
print(t)
"""
https://acmp.ru/index.asp?main=task&id_task=264
"""