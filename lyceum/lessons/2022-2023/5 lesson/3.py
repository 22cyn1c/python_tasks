n = int(input())
a = int(input())
f = n
while f != 0:
    f = f - a
    print(f)
    if f != 0:
        a = int(input())