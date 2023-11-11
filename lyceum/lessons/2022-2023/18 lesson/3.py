n = int(input())
c = {}
for i in range(n):
    a = input().split()
    b = a.pop(0)
    c[b] = a
n = int(input())
for i in range(n):
    a = input()
    if a in c:
        print(' '.join(c[a]))
    else:
        print('Нет в словаре')