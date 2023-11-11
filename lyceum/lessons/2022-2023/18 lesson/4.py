a = input().split()
c = {}
for i in a:
    if i not in c:
        c[i] = 1
        print(c[i], end=' ')
    else:
        c[i] += 1
        print(c[i], end=' ')