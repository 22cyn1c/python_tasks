n = int(input())
a = 0
b = 0
c = 0
co = 0
f = True
while c <= n:
    if f:
        a += 1
        c += a
        c += b
        co += 1
        f = False
        continue
    f = True
    b += 1
    c += b
    c += a
    co += 1
print(co - 1)