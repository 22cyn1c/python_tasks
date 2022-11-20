"""
https://acmp.ru/index.asp?main=task&id_task=514
"""
n = int(input())
t = 0
for i in range(10 ** 6):
    if i == 0:
        continue
    else:
        if n - i >= 0:
            n -= i
            t += 1
        else:
            break
print(t)