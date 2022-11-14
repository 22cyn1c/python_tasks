a = input()
c = str()
b = 1
t = 0
d = 0
for i in range(len(a)):
    d = b
    b += t
    t = d
    if b <= len(a):
        c = c + a[b - 1]
print(c)
'''
https://acmp.ru/index.asp?main=task&id_task=322
'''