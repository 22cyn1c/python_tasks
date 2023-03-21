"""
https://acmp.ru/index.asp?main=task&id_task=13
"""
a, b = map(str, input().split())
k = 0
c = 0
for i in range(4):
    for j in range(4):
        if i == j and a[i] == b[j]:
            k += 1
        elif a[i] == b[j]:
            c += 1
print(k, c)