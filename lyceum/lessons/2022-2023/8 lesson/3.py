n = int(input())
k = 1
s = 1
is_end = False
while True:
    for i in range(s):
        print(k, end=' ')
        k += 1
        if k > n:
            is_end = True
            break
    if is_end:
        break
    print()
    s += 1