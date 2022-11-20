a, b = map(int, input().split())
c = False
for i in range(1001):
    for j in range(1001):
        if i + j == a and i * j == b:
            print(min(i, j), max(i, j))
            c = True
            break
    if c:
        break
