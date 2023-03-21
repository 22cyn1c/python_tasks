n, m = map(int, input().split())
c = 0
r = 0
g = 0
b = 0
for i in range(n):
    for j in range(m):
        c += 1
        if (i + 1) * (j + 1) % 2 == 0:
            c -= 1
            r += 1
            if (i + 1) * (j + 1) % 3 == 0:
                r -= 1
                g += 1
                if (i + 1) * (j + 1) % 5 == 0:
                    g -= 1
                    b += 1
            elif (i + 1) * (j + 1) % 5 == 0:
                r -= 1
                b += 1
        elif (i + 1) * (j + 1) % 3 == 0:
            c -= 1
            g += 1
            if (i + 1) * (j + 1) % 5 == 0:
                g -= 1
                b += 1
        elif (i + 1) * (j + 1) % 5 == 0:
            c -= 1
            b += 1
print('RED :', r)
print('GREEN :', g)
print('BLUE :', b)
print('BLACK :', c)
