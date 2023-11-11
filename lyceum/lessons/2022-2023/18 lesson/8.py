n = int(input())
c = {}
d = 0
b = False
e = []
for i in range(n):
    a = input().split()
    c[i] = a
m = int(input())
for i in range(m):
    a = input()
    for j in range(n):
        if c[j][1] == a:
            e.append(c[j][0])
            b = True
    if not b:
        print('Нет в телефонной книге')
    else:
        print(' '.join(e))
    e = []
    b = False