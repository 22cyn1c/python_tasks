"""
https://acmp.ru/index.asp?main=task&id_task=482
"""
n = int(input())
s = ''
t = 0
i = 0
while len(s) < n:
    i += 1
    for j in range(i):
        t += j + 1
        t = str(t)
        s += t
        t = 0
print(s[n - 1])