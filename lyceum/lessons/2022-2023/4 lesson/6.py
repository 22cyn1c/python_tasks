n = float(input())
a = 0
while n > -1:
    if n > 1000:
        n = n - n * 0.05
        a = a + n
        n = float(input())
    else:
        a = a + n
        n = float(input())
print(a)