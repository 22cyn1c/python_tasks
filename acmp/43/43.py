k = input()
n = len(k)
z = 0
t = 0
for i in range(n):
    a = i
    if k[a] == '0':
        z += 1
        if t < z:
            t = z
    if k[a] == '1':
        z = 0
print(t)
'''
https://acmp.ru/index.asp?main=task&id_task=43
'''