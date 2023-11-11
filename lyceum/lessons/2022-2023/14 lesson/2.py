n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    if 0 <= i <= 2:
        print(1, end=' ')
    else:
        f1, f2, f3 = f2, f3, f1 + f2 + f3
        print(f3, end=' ')