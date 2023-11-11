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
        if c[j][2] == a:
            e.append(c[j][0])
            b = True
    for h in range(len(e) - 1):
        for j in range(len(e) - 1 - h):
            if e[j] > e[j + 1]:
                e[j], e[j + 1] = e[j + 1], e[j]
    if not b:
        print()
    else:
        print(' '.join(e))
    e = []
