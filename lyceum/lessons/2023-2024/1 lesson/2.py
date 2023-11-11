n = int(input())
i = 0
ii = 0
iii = 0
iv = 0
for f in range(n):
    a = list(map(int, input().split()))
    if a[0] > 0:
        if a[1] > 0:
            i += 1
        elif a[1] < 0:
            iv += 1
        else:
            print(f'({a[0]}, 0)')
    elif a[0] < 0:
        if a[1] > 0:
            ii += 1
        elif a[1] < 0:
            iii += 1
        else:
            print(f'({a[0]}, 0)')
    elif a[0] == 0:
        print(f'(0, {a[1]})')
print(f'I: {i}, II: {ii}, III: {iii}, IV: {iv}.')
