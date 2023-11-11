n = int(input())
a = int(input())
while n > 0:
    if 1 <= a <= 3 and n >= a:
        n = n - a
        print(n)
    else:
        print(n)
    if n > 0:
        a = int(input())