a = int(input())
c = 64
b = chr(c)
d = 0
for i in range(a):
    d = str(a - i)
    for j in range(a):
        c += 1
        b = chr(c)
        print(b + d, end=' ')
    c = 64
    print()
