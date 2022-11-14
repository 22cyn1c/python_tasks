a = int(input())
b = 1
t = 0
d = 0
c = 1
for i in range(1200000000):
    d = b
    b += t
    t = d
    c += 1
    if a == b:
        print(1)
        print(c)
        break
    if a < b:
        print(0)
        break
''''
https://acmp.ru/index.asp?main=task&id_task=271
'''