a = 0
b = 0
c = float(input())
while c > -300:
    a += c
    b += 1
    if c > -300:
        c = float(input())
print(a / b)