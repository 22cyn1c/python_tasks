n = int(input())
f = []
for i in range(n):
    f.append(input())
b = True
for i in f:
    if 'xxx' in i:
        print('x')
        b = False
        break
    if 'ooo' in i:
        print('o')
        b = False
        break
if b:
    for i in range(n - 2):
        for j in range(n):
            if f[i][j] == f[i + 1][j] == f[i + 2][j] != '.':
                print(f[i][j])
                b = False
        if not b:
            break
if b:
    print('-')
