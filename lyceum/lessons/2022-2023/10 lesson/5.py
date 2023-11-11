b = 0
while True:
    a = input()
    if b == 0:
        b += 1
        t = a[len(a) - 1]
        continue
    if t == a[0]:
        t = a[len(a) - 1]
        continue
    else:
        print(a)
        break