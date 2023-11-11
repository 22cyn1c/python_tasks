n = int(input())
c = []
for i in range(n):
    a = int(input())
    c.append(a)
n = int(input())
b = True
for i in range(len(c) - 1):
    for j in range(i + 1, len(c)):
        if c[i] * c[j] == n:
            print('ДА')
            b = False
            break
    if not b:
        break
if b:
    print('НЕТ')