a = int(input())
b = list(map(int, input().split()))
v = 0
c = -1
for i in range(a):
    if c == -1:
        c = b[i]
        continue
    v += (b[i] + c) / 2
    c = b[i]
print(v / (a - 1))
'''
https://acmp.ru/index.asp?main=task&id_task=409
'''