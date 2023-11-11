a = input()
n = int(input())
if n >= 0:
    while n > len(a):
        n -= len(a)
    print(a[n:] + a[:n])
    print(a)
    print(a[len(a) - n:] + a[:len(a) - n])
else:
    while n < len(a) - 2 * len(a):
        n += len(a)
    print(a[len(a) + n:] + a[:len(a) + n])
    print(a)
    print(a[abs(n):] + a[:abs(n)])