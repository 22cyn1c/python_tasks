n = int(input())
c = 0
if n > 0:
    for i in range(1, n + 1):
        c += i
    print(c)
elif n < 0:
    for i in range(n, 2):
        c += i
    print(c)
else:
    print(1)
