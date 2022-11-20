"""
https://acmp.ru/index.asp?main=task&id_task=711
"""
n, m = map(int, input().split())
set_a = []
t = 0
x = 10000000000
c = 0
for i in range(n):
    a = input()
    set_a.append(a)
    b = list(map(int, input().split()))
    for elem in b:
        t += elem
    if t < x:
        x = t
        c = i
    t = 0
print(set_a[c])