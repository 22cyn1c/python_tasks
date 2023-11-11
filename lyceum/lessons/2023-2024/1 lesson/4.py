a = input().split(' -> ')
n = int(input())
for i in range(n):
    b = input()
    if a.index(b) == 0:
        print(f'{b} -> {a[1]}')
    elif a.index(b) == len(a) - 1:
        print(f'{a[-2]} -> {b}')
    else:
        print(f'{a[a.index(b) - 1]} -> {b} -> {a[a.index(b) + 1]}')