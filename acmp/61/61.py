a, b= input().split()
a = int(a)
b = int(b)
c, d= input().split()
c = int(c)
d = int(d)
m, n= input().split()
m = int(m)
n = int(n)
k, l= input().split()
k = int(k)
l = int(l)
if a + c + m + k > b + d + n + l:
    print(1)
elif a + c + m + k < b + d + n + l:
    print(2)
else:
    print('DRAW')
'''
https://acmp.ru/index.asp?main=task&id_task=61
'''